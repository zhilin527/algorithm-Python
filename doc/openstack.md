# 1. 云计算的介绍
## 1.1 iaas和paas和saas
![Image in doc_img_docker may be lost. ]()

iaas: infrastructure as a server, r.g. ECS云服务器  
paas：platform as a server, e.g. docker实现  
saas：software as a server, e.g. 腾讯企业邮箱，云数据库  

# 2. SOA架构

Service-Oriented Architecture  
openstack 的安装参考官方文档：
https://docs.openstack.org/mitaka/zh_CN/install-guide-rdo/

# 3. 安装openstack

## 3.1 安装及配置centos7

1. 安装好两台 centos 虚拟机
2. 设置两台centos虚拟机为固定ip
修改VMware的虚拟网络编辑器
选中NAT模式,修改一些配置,管理员修改,取消使用本地DHCP服务分配ip
子网10.0.0.0 子网掩码255.255.255.0
3. centos中设置网络
vim /etc/sysconfig/network-scripts/ifcfg-ens33
以下列出必修改项，controller：
BOOTPROTO=static
ONBOOT=yes
IPADDR=10.0.0.11
NETMASK=255.255.255.0
GATEWAY=10.0.0.2
DNS1=223.5.5.5

compute1：
BOOTPROTO=static
ONBOOT=yes
IPADDR=10.0.0.31
NETMASK=255.255.255.0
GATEWAY=10.0.0.2
DNS1=223.5.5.5
vmware设置固定ip可参考 https://blog.csdn.net/xukaijj/article/details/78855402

4. 修改主机名
controller：
hostnamectl set-hostname controller
compute1：
hostnamectl set-hostname compute1

5. 设置hosts
controller和compute1：
vim /etc/hosts
增加：
10.0.0.11 controller
10.0.0.31 compute1

## 3.2 配置yum源
1. 挂载光盘
mount /dev/cdrom /mnt
挂载完成后 ll /mnt 检查是否挂载
2. rz 上传openstack_rpm.tar.gz 到/opt，并解压
cd /opt/
tar xf openstack_rpm.tar.gz
ll -h

生成repo配置文件,直接在shell命令执行
echo '[local]
name=local
baseurl=file:///mnt
gpgcheck=0

[openstack]
name=openstack
baseurl=file:///opt/repo
gpgcheck=0' >/etc/yum.repos.d/local.repo

echo 'mount /dev/cdrom /mnt' >>/etc/rc.local
chmod +x /etc/rc.d/rc.local

## 3.3 安装基础服务
在所有节点上执行：
### 3.3.1 时间同步
安装 chrony
yum install chrony -y
控制节点：
vim /etc/chrony.conf 
在server 0前面增加 server ntp6.aliyun.com iburst

增加第 26 行为，允许本地客户端来同步
allow 10.0.0.0/24

systemctl restart chronyd

bug：
一开始centos时间不准确，先将server设置位阿里云ntp服务器，同步一下时间
再将server设置位控制节点

计算节点：
vim /etc/chrony.conf
修改第3行为
server 10.0.0.11 iburst

systemctl restart chronyd

检测：
同时执行date命令查看时间同步

在所有节点上执行：
### 3.3.2 安装openstack客户端和openstack-selinux
yum install python-openstackclient openstack-selinux -y

仅控制节点执行：
### 3.3.3 安装配置mariadb
yum install mariadb mariadb-server python2-PyMySQL -y

echo '[mysqld]
bind-address = 10.0.0.11
default-storage-engine = innodb
innodb_file_per_table
max_connections = 4096
collation-server = utf8_general_ci
character-set-server = utf8' >/etc/my.cnf.d/openstack.cnf

systemctl start mariadb
systemctl enable mariadb

mysql_secure_installation
直接回车
n
y
y
y
y

仅控制节点执行：
### 3.3.4 安装rabbitmq并创建用户
yum install rabbitmq-server -y
systemctl start rabbitmq-server.service
systemctl enable rabbitmq-server.service

rabbitmqctl add_user openstack RABBIT_PASS
rabbitmqctl set_permissions openstack ".*" ".*" ".*"

rabbitmq-plugins enable rabbitmq_management

仅控制节点执行：
### 3.3.5 memcached缓存token
yum install memcached python-memcached -y
sed -i 's#127.0.0.1#10.0.0.11#g' /etc/sysconfig/memcached
systemctl restart memcached.service
systemctl enable memcached.service

### 3.3.6 centos永久关闭防火墙
systemctl stop firewalld.service
systemctl disable firewalld.service
centos 需要关闭防火墙，否则宿主机浏览器访问不了centos起的web服务

## 3.4 安装o版用公网源[额外]
rm -rf /etc/yum.repos.d/local.repo
curl -o /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-7.repo
ll /etc/yum.repos.d/
yum makecache
ll /etc/yum.repos.d/
yum list|grep openstack
yum install centos-release-openstack-ocata.noarch -y

## 3.5 keystone认证服务
功能：认证管理，授权管理，服务目录
- 认证：账户密码
- 授权：授权管理
- 服务目录：电话本

### 3.5.1 openstack服务安装的通用步骤
1. 创库授权
2. 在keystone上创建用户，关联一个角色
3. 在keystone上创建服务，注册api
4. 安装服务相关的软件包
5. 修改配置文件，数据库的连接信息，rabbitmq连接信息，keystone认证信息，其他配置信息
6. 同步数据库，创建表
7. 启动服务

### 3.5.2 安装keystone
1. 创库授权
mysql
CREATE DATABASE keystone;
GRANT ALL PRIVILEGES ON keystone.* TO 'keystone'@'localhost' IDENTIFIED BY 'KEYSTONE_DBPASS';
GRANT ALL PRIVILEGES ON keystone.* TO 'keystone'@'%' IDENTIFIED BY 'KEYSTONE_DBPASS';

1. 安装keystone相关软件包
yum install openstack-keystone httpd mod_wsgi -y

3. 修改配置文件
vim /etc/keystone/keystone.conf
grep -Ev '^$|#' /etc/keystone/keystone.conf 输出不是注释和空行的行
grep -Ev '^$|#' /etc/keystone/keystone.conf |wc -l

- 在``[DEFAULT]``部分，定义初始管理令牌的值：
[DEFAULT]
...
admin_token = ADMIN_TOKEN

- 在 [database] 部分，配置数据库访问：
[database]
...
connection = mysql+pymysql://keystone:KEYSTONE_DBPASS@controller/keystone

- 在``[token]``部分，配置Fernet UUID令牌的提供者。
[token]
...
provider = fernet

keystone认证方式：UUID，PKI，Fernet；
都只是生成一段随机字符串的方法，保证唯一，

yum install openstack-utils -y
openstack-config --set /etc/keystone/keystone.conf DEFAULT admin_token ADMIN_TOKEN
openstack-config --set /etc/keystone/keystone.conf database connetion mysql+pymysql://keystone:KEYSTONE_DBPASS@controller/keystone

openstack-config --set /etc/keystone/keystone.conf token provider fernet

校验
md5sum /etc/keystone/keystone.conf
a11e52a3b99acc6dcf0ffa0428ea7a16  /etc/keystone/keystone.conf

4. 同步数据库

mysql keystone -e 'show tables;'
同步之前，结果为空
su -s /bin/sh -c "keystone-manage db_sync" keystone

mysql keystone -e 'show tables;'

5. 初始化Fernet
ll /etc/keystone/
keystone-manage fernet_setup --keystone-user keystone --keystone-group keystone

6. 配置httpd
编辑``/etc/httpd/conf/httpd.conf`` 文件，配置``ServerName`` 选项为控制节点：
echo "ServerName controller" >>/etc/httpd/conf/httpd.conf

用下面的内容创建文件 /etc/httpd/conf.d/wsgi-keystone.conf
Listen 5000
Listen 35357

<VirtualHost *:5000>
    WSGIDaemonProcess keystone-public processes=5 threads=1 user=keystone group=keystone display-name=%{GROUP}
    WSGIProcessGroup keystone-public
    WSGIScriptAlias / /usr/bin/keystone-wsgi-public
    WSGIApplicationGroup %{GLOBAL}
    WSGIPassAuthorization On
    ErrorLogFormat "%{cu}t %M"
    ErrorLog /var/log/httpd/keystone-error.log
    CustomLog /var/log/httpd/keystone-access.log combined

    <Directory /usr/bin>
        Require all granted
    </Directory>
</VirtualHost>

<VirtualHost *:35357>
    WSGIDaemonProcess keystone-admin processes=5 threads=1 user=keystone group=keystone display-name=%{GROUP}
    WSGIProcessGroup keystone-admin
    WSGIScriptAlias / /usr/bin/keystone-wsgi-admin
    WSGIApplicationGroup %{GLOBAL}
    WSGIPassAuthorization On
    ErrorLogFormat "%{cu}t %M"
    ErrorLog /var/log/httpd/keystone-error.log
    CustomLog /var/log/httpd/keystone-access.log combined

    <Directory /usr/bin>
        Require all granted
    </Directory>
</VirtualHost>

7. 启动httpd
systemctl enable httpd.service
systemctl start httpd.service

查看端口：
netstat -lntup

8. 创建服务和注册api

export OS_TOKEN=ADMIN_TOKEN
export OS_URL=http://controller:35357/v3
export OS_IDENTITY_API_VERSION=3

env|grep OS

openstack service create \
--name keystone --description "Openstack Identity" identity

openstack endpoint create --region RegionOne \
 identity public http://controller:5000/v3

openstack endpoint create --region RegionOne \
 identity internal http://controller:5000/v3

openstack endpoint create --region RegionOne \
 identity admin http://controller:35357/v3

9. 创建域，项目，用户，角色
项目以前叫租户，一个公司开了一个租户，租户里面建了多个用户，
openstack domain create --description "Default Domain" default

openstack project create --domain default \
  --description "Admin Project" admin

openstack user create --domain default \
  --password ADMIN_PASS admin

openstack role create admin

关联项目用户角色
openstack role add --project admin --user admin admin

创建 service 项目
openstack project create --domain default \
  --description "Service Project" service

环境变量：
env|grep OS
使某环境变量失效：
1.unset OS_TOKEN
2.logout

export OS_PROJECT_DOMAIN_NAME=default
export OS_USER_DOMAIN_NAME=default
export OS_PROJECT_NAME=admin
export OS_USERNAME=admin
export OS_PASSWORD=ADMIN_PASS
export OS_AUTH_URL=http://controller:35357/v3
export OS_IDENTITY_API_VERSION=3
export OS_IMAGE_API_VERSION=2

配置了上述的环境变量后执行openstack命令
openstack user list

没有配置环境变量则需要带参数
openstack --os-auth-url http://controller:35357/v3 \
  --os-project-domain-name default --os-user-domain-name default \
  --os-project-name admin --os-username admin token issue

创建脚本自动创建环境变量：
vim admin-openrc 并添加如下内容
export OS_PROJECT_DOMAIN_NAME=default
export OS_USER_DOMAIN_NAME=default
export OS_PROJECT_NAME=admin
export OS_USERNAME=admin
export OS_PASSWORD=ADMIN_PASS
export OS_AUTH_URL=http://controller:35357/v3
export OS_IDENTITY_API_VERSION=3
export OS_IMAGE_API_VERSION=2

openstack token issue
报没有参数的错误时，执行source admin-openrc

或者将source admin-openrc 写进 .bashrc 中
vim .bashrc
末尾添加source admin-openrc

再退出登录
logout

## 3.6 glance镜像服务

### 3.6.1 安装glance

1. 创库授权
CREATE DATABASE glance;

GRANT ALL PRIVILEGES ON glance.* TO 'glance'@'localhost' \
  IDENTIFIED BY 'GLANCE_DBPASS';
GRANT ALL PRIVILEGES ON glance.* TO 'glance'@'%' \
  IDENTIFIED BY 'GLANCE_DBPASS';

2. 在keystone创建glance用户关联角色
openstack user create --domain default --password GLANCE_PASS glance
openstack role add --project service --user glance admin

openstack role assignment list
openstack role list
openstack user list
openstack project list

mysql keystone -e "show tables;"|grep role
mysql keystone -e "show tables;"|grep user
mysql keystone -e "show tables;"|grep project

3. 在keystone上创建服务和注册api
openstack service create --name glance \
  --description "OpenStack Image" image

openstack endpoint create --region RegionOne \
  image public http://controller:9292

openstack endpoint create --region RegionOne \
  image internal http://controller:9292

openstack endpoint create --region RegionOne \
  image admin http://controller:9292

4. 安装服务相关应用软件包
yum install openstack-glance -y

5. 配置文件

两个服务，所以两个配置文件需要修改
文件 /etc/glance/glance-api.conf
openstack-config --set /etc/glance/glance-api.conf  database  connection  mysql+pymysql://glance:GLANCE_DBPASS@controller/glance
openstack-config --set /etc/glance/glance-api.conf  glance_store stores  file,http
openstack-config --set /etc/glance/glance-api.conf  glance_store default_store  file
openstack-config --set /etc/glance/glance-api.conf  glance_store filesystem_store_datadir  /var/lib/glance/images/
openstack-config --set /etc/glance/glance-api.conf  keystone_authtoken auth_uri  http://controller:5000
openstack-config --set /etc/glance/glance-api.conf  keystone_authtoken auth_url  http://controller:35357
openstack-config --set /etc/glance/glance-api.conf  keystone_authtoken memcached_servers  controller:11211
openstack-config --set /etc/glance/glance-api.conf  keystone_authtoken auth_type  password
openstack-config --set /etc/glance/glance-api.conf  keystone_authtoken project_domain_name  default
openstack-config --set /etc/glance/glance-api.conf  keystone_authtoken user_domain_name  default
openstack-config --set /etc/glance/glance-api.conf  keystone_authtoken project_name  service
openstack-config --set /etc/glance/glance-api.conf  keystone_authtoken username  glance
openstack-config --set /etc/glance/glance-api.conf  keystone_authtoken password  GLANCE_PASS
openstack-config --set /etc/glance/glance-api.conf  paste_deploy flavor  keystone

文件 ``/etc/glance/glance-registry.conf``
openstack-config --set /etc/glance/glance-registry.conf  database  connection  mysql+pymysql://glance:GLANCE_DBPASS@controller/glance
openstack-config --set /etc/glance/glance-registry.conf  keystone_authtoken auth_uri  http://controller:5000
openstack-config --set /etc/glance/glance-registry.conf  keystone_authtoken auth_url  http://controller:35357
openstack-config --set /etc/glance/glance-registry.conf  keystone_authtoken memcached_servers  controller:11211
openstack-config --set /etc/glance/glance-registry.conf  keystone_authtoken auth_type  password
openstack-config --set /etc/glance/glance-registry.conf  keystone_authtoken project_domain_name  default
openstack-config --set /etc/glance/glance-registry.conf  keystone_authtoken user_domain_name  default
openstack-config --set /etc/glance/glance-registry.conf  keystone_authtoken project_name  service
openstack-config --set /etc/glance/glance-registry.conf  keystone_authtoken username  glance
openstack-config --set /etc/glance/glance-registry.conf  keystone_authtoken password  GLANCE_PASS
openstack-config --set /etc/glance/glance-registry.conf  paste_deploy flavor  keystone

同步数据库
su -s /bin/sh -c "glance-manage db_sync" glance
忽略输出中任何不推荐使用的信息。
mysql glance -e "show tables;"

启动服务
systemctl start openstack-glance-api.service openstack-glance-registry.service
systemctl enable openstack-glance-api.service openstack-glance-registry.service

检查监听端口
netstat -lntup

上传镜像验证
#wget http://download.cirros-cloud.net/0.3.4/cirros-0.3.4-x86_64-disk.img
#wget http://10.0.0.1/cirros-0.3.4-x86_64-disk.img
将cirros-0.3.4-x86_64-disk.img 上传至centos:/root/

openstack image create "cirros" --file cirros-0.3.4-x86_64-disk.img --disk-format qcow2 \
--container-format bare --public
openstack image list

## 3.7 nova计算服务

- nova-api 服务：接收和响应来自最终用户的计算API请求
- nova-api-metadata 服务：接受来自虚拟机发送的元数据请求
- ``nova-compute``服务：多个，真正管理虚拟机，通过Hypervior的API来创建和销毁虚拟机实例
- ``nova-scheduler``服务：nova调度器，挑选最合适的compute创建虚拟机
- ``nova-conductor``模块：帮助nova-compute代理修改数据库中虚机的状态
- nova-network：早期版本管理虚机的网络
- nova-consoleauth 和 nova-novncproxy：web版的vnc直接操作云主机

### 3.7.1 nova计算服务控制节点
1. 创库授权
CREATE DATABASE nova_api;
CREATE DATABASE nova;

GRANT ALL PRIVILEGES ON nova_api.* TO 'nova'@'localhost' \
  IDENTIFIED BY 'NOVA_DBPASS';
GRANT ALL PRIVILEGES ON nova_api.* TO 'nova'@'%' \
  IDENTIFIED BY 'NOVA_DBPASS';
GRANT ALL PRIVILEGES ON nova.* TO 'nova'@'localhost' \
  IDENTIFIED BY 'NOVA_DBPASS';
GRANT ALL PRIVILEGES ON nova.* TO 'nova'@'%' \
  IDENTIFIED BY 'NOVA_DBPASS';

2. 创建keystone用户角色
openstack user create --domain default \
  --password NOVA_PASS nova

openstack role add --project service --user nova admin

3. 在keystone创建服务和注册api
openstack service create --name nova \
  --description "OpenStack Compute" compute

openstack endpoint create --region RegionOne \
  compute public http://controller:8774/v2.1/%\(tenant_id\)s

openstack endpoint create --region RegionOne \
  compute internal http://controller:8774/v2.1/%\(tenant_id\)s

openstack endpoint create --region RegionOne \
  compute admin http://controller:8774/v2.1/%\(tenant_id\)s

4. 安装软件包
yum install openstack-nova-api openstack-nova-conductor \
  openstack-nova-console openstack-nova-novncproxy \
  openstack-nova-scheduler -y

5. 配置文件

openstack-config --set /etc/nova/nova.conf  DEFAULT enabled_apis  osapi_compute,metadata
openstack-config --set /etc/nova/nova.conf  DEFAULT rpc_backend  rabbit
openstack-config --set /etc/nova/nova.conf  DEFAULT auth_strategy  keystone
openstack-config --set /etc/nova/nova.conf  DEFAULT my_ip  10.0.0.11
openstack-config --set /etc/nova/nova.conf  DEFAULT use_neutron  True
openstack-config --set /etc/nova/nova.conf  DEFAULT firewall_driver  nova.virt.firewall.NoopFirewallDriver
openstack-config --set /etc/nova/nova.conf  api_database connection  mysql+pymysql://nova:NOVA_DBPASS@controller/nova_api
openstack-config --set /etc/nova/nova.conf  database  connection  mysql+pymysql://nova:NOVA_DBPASS@controller/nova
openstack-config --set /etc/nova/nova.conf  glance api_servers  http://controller:9292
openstack-config --set /etc/nova/nova.conf  keystone_authtoken  auth_uri  http://controller:5000
openstack-config --set /etc/nova/nova.conf  keystone_authtoken  auth_url  http://controller:35357
openstack-config --set /etc/nova/nova.conf  keystone_authtoken  memcached_servers  controller:11211
openstack-config --set /etc/nova/nova.conf  keystone_authtoken  auth_type  password
openstack-config --set /etc/nova/nova.conf  keystone_authtoken  project_domain_name  default
openstack-config --set /etc/nova/nova.conf  keystone_authtoken  user_domain_name  default
openstack-config --set /etc/nova/nova.conf  keystone_authtoken  project_name  service
openstack-config --set /etc/nova/nova.conf  keystone_authtoken  username  nova
openstack-config --set /etc/nova/nova.conf  keystone_authtoken  password  NOVA_PASS
openstack-config --set /etc/nova/nova.conf  oslo_concurrency lock_path  /var/lib/nova/tmp
openstack-config --set /etc/nova/nova.conf  oslo_messaging_rabbit   rabbit_host  controller
openstack-config --set /etc/nova/nova.conf  oslo_messaging_rabbit   rabbit_userid  openstack
openstack-config --set /etc/nova/nova.conf  oslo_messaging_rabbit   rabbit_password  RABBIT_PASS

openstack-config --set /etc/nova/nova.conf  vnc vncserver_listen  '$my_ip'
openstack-config --set /etc/nova/nova.conf  vnc vncserver_proxyclient_address  '$my_ip'

6. 同步数据库
su -s /bin/sh -c "nova-manage api_db sync" nova
su -s /bin/sh -c "nova-manage db sync" nova

7. 检查是否成功

mysql nova_api -e "show tables;"
mysql nova -e "show tables;"

8. 启动应用

systemctl enable openstack-nova-api.service \
  openstack-nova-consoleauth.service openstack-nova-scheduler.service \
  openstack-nova-conductor.service openstack-nova-novncproxy.service

systemctl start openstack-nova-api.service \
  openstack-nova-consoleauth.service openstack-nova-scheduler.service \
  openstack-nova-conductor.service openstack-nova-novncproxy.service

nova service-list

### 3.7.2 nova计算服务计算节点

只安装一个服务nova-compute
nova-compute调用libvirtd来创建虚拟机,支持多种虚拟化技术，支持qemu，支持kvm，支持vmware
1. 安装
yum install openstack-nova-compute -y
yum install openstack-utils.noarch -y

2. 配置

openstack-config --set /etc/nova/nova.conf  DEFAULT enabled_apis  osapi_compute,metadata
openstack-config --set /etc/nova/nova.conf  DEFAULT rpc_backend  rabbit
openstack-config --set /etc/nova/nova.conf  DEFAULT auth_strategy  keystone
openstack-config --set /etc/nova/nova.conf  DEFAULT my_ip  10.0.0.31
openstack-config --set /etc/nova/nova.conf  DEFAULT use_neutron  True
openstack-config --set /etc/nova/nova.conf  DEFAULT firewall_driver  nova.virt.firewall.NoopFirewallDriver

openstack-config --set /etc/nova/nova.conf  glance api_servers  http://controller:9292
openstack-config --set /etc/nova/nova.conf  keystone_authtoken  auth_uri  http://controller:5000
openstack-config --set /etc/nova/nova.conf  keystone_authtoken  auth_url  http://controller:35357
openstack-config --set /etc/nova/nova.conf  keystone_authtoken  memcached_servers  controller:11211
openstack-config --set /etc/nova/nova.conf  keystone_authtoken  auth_type  password
openstack-config --set /etc/nova/nova.conf  keystone_authtoken  project_domain_name  default
openstack-config --set /etc/nova/nova.conf  keystone_authtoken  user_domain_name  default
openstack-config --set /etc/nova/nova.conf  keystone_authtoken  project_name  service
openstack-config --set /etc/nova/nova.conf  keystone_authtoken  username  nova
openstack-config --set /etc/nova/nova.conf  keystone_authtoken  password  NOVA_PASS
openstack-config --set /etc/nova/nova.conf  oslo_concurrency lock_path  /var/lib/nova/tmp
openstack-config --set /etc/nova/nova.conf  oslo_messaging_rabbit   rabbit_host  controller
openstack-config --set /etc/nova/nova.conf  oslo_messaging_rabbit   rabbit_userid  openstack
openstack-config --set /etc/nova/nova.conf  oslo_messaging_rabbit   rabbit_password  RABBIT_PASS

openstack-config --set /etc/nova/nova.conf  vnc enabled  True
openstack-config --set /etc/nova/nova.conf  vnc vncserver_listen  0.0.0.0
openstack-config --set /etc/nova/nova.conf  vnc vncserver_proxyclient_address  '$my_ip'
openstack-config --set /etc/nova/nova.conf  vnc novncproxy_base_url  http://controller:6080/vnc_auto.html


3. 启动
systemctl enable libvirtd.service openstack-nova-compute.service
systemctl start libvirtd.service openstack-nova-compute.service

## 3.8 neutron网络服务

- neutron-server：端口9696，接收和路由API请求到合适的OpenStack网络插件
- neutron-linuxbridge-agent：负责创建桥接网桥
- neutron-dhcp-agent：负责分配ip
- neutron-metadata-agent：配合nova-matadata-api实现虚拟机的定制化操作
- L3-agent：实现三层网络vxlan(网络层)

### 3.8.1 控制节点

1. 创库授权
CREATE DATABASE neutron;
GRANT ALL PRIVILEGES ON neutron.* TO 'neutron'@'localhost' \
  IDENTIFIED BY 'NEUTRON_DBPASS';
GRANT ALL PRIVILEGES ON neutron.* TO 'neutron'@'%' \
  IDENTIFIED BY 'NEUTRON_DBPASS';

2. 创建keystone用户角色

openstack user create --domain default --password NEUTRON_PASS neutron
openstack role add --project service --user neutron admin   

3. 在keystone创建服务和注册api

openstack service create --name neutron \
  --description "OpenStack Networking" network
openstack endpoint create --region RegionOne \
  network public http://controller:9696
openstack endpoint create --region RegionOne \
  network internal http://controller:9696
openstack endpoint create --region RegionOne \
  network admin http://controller:9696


4. 安装软件包
yum install openstack-neutron openstack-neutron-ml2 \
 openstack-neutron-linuxbridge ebtables -y

5. 配置文件

网络虚拟化机制：linuxbridge 和 openvswtich
公共网络
/etc/neutron/neutron.conf

openstack-config --set /etc/neutron/neutron.conf  DEFAULT core_plugin  ml2
openstack-config --set /etc/neutron/neutron.conf  DEFAULT service_plugins
openstack-config --set /etc/neutron/neutron.conf  DEFAULT rpc_backend  rabbit
openstack-config --set /etc/neutron/neutron.conf  DEFAULT auth_strategy  keystone
openstack-config --set /etc/neutron/neutron.conf  DEFAULT notify_nova_on_port_status_changes  True
openstack-config --set /etc/neutron/neutron.conf  DEFAULT notify_nova_on_port_data_changes  True
openstack-config --set /etc/neutron/neutron.conf  database connection  mysql+pymysql://neutron:NEUTRON_DBPASS@controller/neutron
openstack-config --set /etc/neutron/neutron.conf  keystone_authtoken auth_uri  http://controller:5000
openstack-config --set /etc/neutron/neutron.conf  keystone_authtoken auth_url  http://controller:35357
openstack-config --set /etc/neutron/neutron.conf  keystone_authtoken memcached_servers  controller:11211
openstack-config --set /etc/neutron/neutron.conf  keystone_authtoken auth_type  password
openstack-config --set /etc/neutron/neutron.conf  keystone_authtoken project_domain_name  default
openstack-config --set /etc/neutron/neutron.conf  keystone_authtoken user_domain_name  default
openstack-config --set /etc/neutron/neutron.conf  keystone_authtoken project_name  service
openstack-config --set /etc/neutron/neutron.conf  keystone_authtoken username  neutron
openstack-config --set /etc/neutron/neutron.conf  keystone_authtoken password  NEUTRON_PASS
openstack-config --set /etc/neutron/neutron.conf  nova auth_url  http://controller:35357
openstack-config --set /etc/neutron/neutron.conf  nova auth_type  password 
openstack-config --set /etc/neutron/neutron.conf  nova project_domain_name  default
openstack-config --set /etc/neutron/neutron.conf  nova user_domain_name  default
openstack-config --set /etc/neutron/neutron.conf  nova region_name  RegionOne
openstack-config --set /etc/neutron/neutron.conf  nova project_name  service
openstack-config --set /etc/neutron/neutron.conf  nova username  nova
openstack-config --set /etc/neutron/neutron.conf  nova password  NOVA_PASS
openstack-config --set /etc/neutron/neutron.conf  oslo_concurrency lock_path  /var/lib/neutron/tmp
openstack-config --set /etc/neutron/neutron.conf  oslo_messaging_rabbit rabbit_host  controller
openstack-config --set /etc/neutron/neutron.conf  oslo_messaging_rabbit rabbit_userid  openstack
openstack-config --set /etc/neutron/neutron.conf  oslo_messaging_rabbit rabbit_password  RABBIT_PASS

/etc/neutron/plugins/ml2/ml2_conf.ini 

openstack-config --set /etc/neutron/plugins/ml2/ml2_conf.ini  ml2 type_drivers  flat,vlan
openstack-config --set /etc/neutron/plugins/ml2/ml2_conf.ini  ml2 tenant_network_types 
openstack-config --set /etc/neutron/plugins/ml2/ml2_conf.ini  ml2 mechanism_drivers  linuxbridge
openstack-config --set /etc/neutron/plugins/ml2/ml2_conf.ini  ml2 extension_drivers  port_security
openstack-config --set /etc/neutron/plugins/ml2/ml2_conf.ini  ml2_type_flat flat_networks  provider
openstack-config --set /etc/neutron/plugins/ml2/ml2_conf.ini  securitygroup enable_ipset  True

/etc/neutron/plugins/ml2/linuxbridge_agent.ini 

openstack-config --set /etc/neutron/plugins/ml2/linuxbridge_agent.ini  linux_bridge physical_interface_mappings  provider:ens33
openstack-config --set /etc/neutron/plugins/ml2/linuxbridge_agent.ini  securitygroup enable_security_group  True
openstack-config --set /etc/neutron/plugins/ml2/linuxbridge_agent.ini  securitygroup firewall_driver  neutron.agent.linux.iptables_firewall.IptablesFirewallDriver
openstack-config --set /etc/neutron/plugins/ml2/linuxbridge_agent.ini  vxlan enable_vxlan  False

/etc/neutron/dhcp_agent.ini 

openstack-config --set /etc/neutron/dhcp_agent.ini  DEFAULT interface_driver neutron.agent.linux.interface.BridgeInterfaceDriver
openstack-config --set /etc/neutron/dhcp_agent.ini  DEFAULT dhcp_driver neutron.agent.linux.dhcp.Dnsmasq
openstack-config --set /etc/neutron/dhcp_agent.ini  DEFAULT enable_isolated_metadata true

/etc/neutron/metadata_agent.ini 

openstack-config --set /etc/neutron/metadata_agent.ini DEFAULT nova_metadata_ip  controller
openstack-config --set /etc/neutron/metadata_agent.ini DEFAULT metadata_proxy_shared_secret  METADATA_SECRET

再次修改/etc/nova/nova.conf，nova里面配置neutron

openstack-config --set /etc/nova/nova.conf  neutron url  http://controller:9696
openstack-config --set /etc/nova/nova.conf  neutron auth_url  http://controller:35357
openstack-config --set /etc/nova/nova.conf  neutron auth_type  password
openstack-config --set /etc/nova/nova.conf  neutron project_domain_name  default
openstack-config --set /etc/nova/nova.conf  neutron user_domain_name  default
openstack-config --set /etc/nova/nova.conf  neutron region_name  RegionOne
openstack-config --set /etc/nova/nova.conf  neutron project_name  service
openstack-config --set /etc/nova/nova.conf  neutron username  neutron
openstack-config --set /etc/nova/nova.conf  neutron password  NEUTRON_PASS
openstack-config --set /etc/nova/nova.conf  neutron service_metadata_proxy  True
openstack-config --set /etc/nova/nova.conf  neutron metadata_proxy_shared_secret  METADATA_SECRET

6. 同步数据库

ln -s /etc/neutron/plugins/ml2/ml2_conf.ini /etc/neutron/plugin.ini

su -s /bin/sh -c "neutron-db-manage --config-file /etc/neutron/neutron.conf --config-file \
/etc/neutron/plugins/ml2/ml2_conf.ini upgrade head" neutron

mysql neutron -e "show tables;"

7. 启动服务

systemctl restart openstack-nova-api.service
systemctl start neutron-server.service neutron-linuxbridge-agent.service \
neutron-dhcp-agent.service   neutron-metadata-agent.service
systemctl enable neutron-server.service neutron-linuxbridge-agent.service \
neutron-dhcp-agent.service   neutron-metadata-agent.service

8. 检查
neutron agent-list


### 3.8.2 计算节点

1. 安装

yum install openstack-neutron-linuxbridge ebtables ipset -y

2. 配置文件
公共网络
/etc/neutron/neutron.conf

openstack-config --set /etc/neutron/neutron.conf  DEFAULT rpc_backend  rabbit
openstack-config --set /etc/neutron/neutron.conf  DEFAULT auth_strategy  keystone
openstack-config --set /etc/neutron/neutron.conf  keystone_authtoken auth_uri  http://controller:5000
openstack-config --set /etc/neutron/neutron.conf  keystone_authtoken auth_url  http://controller:35357
openstack-config --set /etc/neutron/neutron.conf  keystone_authtoken memcached_servers  controller:11211
openstack-config --set /etc/neutron/neutron.conf  keystone_authtoken auth_type  password
openstack-config --set /etc/neutron/neutron.conf  keystone_authtoken project_domain_name  default
openstack-config --set /etc/neutron/neutron.conf  keystone_authtoken user_domain_name  default
openstack-config --set /etc/neutron/neutron.conf  keystone_authtoken project_name  service
openstack-config --set /etc/neutron/neutron.conf  keystone_authtoken username  neutron
openstack-config --set /etc/neutron/neutron.conf  keystone_authtoken password  NEUTRON_PASS
openstack-config --set /etc/neutron/neutron.conf  oslo_concurrency lock_path  /var/lib/neutron/tmp
openstack-config --set /etc/neutron/neutron.conf  oslo_messaging_rabbit rabbit_host  controller
openstack-config --set /etc/neutron/neutron.conf  oslo_messaging_rabbit rabbit_userid  openstack
openstack-config --set /etc/neutron/neutron.conf  oslo_messaging_rabbit rabbit_password  RABBIT_PASS

scp -rp 10.0.0.11:/etc/neutron/plugins/ml2/linuxbridge_agent.ini /etc/neutron/plugins/ml2/linuxbridge_agent.ini

再次修改/etc/nova/nova.conf，nova里面配置neutron

openstack-config --set /etc/nova/nova.conf  neutron url  http://controller:9696
openstack-config --set /etc/nova/nova.conf  neutron auth_url  http://controller:35357
openstack-config --set /etc/nova/nova.conf  neutron auth_type  password
openstack-config --set /etc/nova/nova.conf  neutron project_domain_name  default
openstack-config --set /etc/nova/nova.conf  neutron user_domain_name  default
openstack-config --set /etc/nova/nova.conf  neutron region_name  RegionOne
openstack-config --set /etc/nova/nova.conf  neutron project_name  service
openstack-config --set /etc/nova/nova.conf  neutron username  neutron
openstack-config --set /etc/nova/nova.conf  neutron password  NEUTRON_PASS

3. 启动

systemctl restart openstack-nova-compute.service

systemctl enable neutron-linuxbridge-agent.service
systemctl start neutron-linuxbridge-agent.service

## 3.9 安装horizon web界面

装在计算节点上
yum install openstack-dashboard -y

控制节点上执行：
neutron agent-list
openstack endpoint list|grep identity

将local_settings拷贝到计算节点
cat local_settings >/etc/openstack-dashboard/local_settings
ll /etc/openstack-dashboard/local_settings
确保apache对该文件有read的权限

启动：
systemctl enable httpd.service
systemctl start httpd.service

启动后打不开 10.0.0.31/dashboard
vim /etc/httpd/conf.d/openstack-dashboard.conf
添加
WSGIApplicationGroup %{GLOBAL}

rpm -qf /etc/httpd/conf.d/openstack-dashboard.conf
查看这个文件属于哪个包

重启apache
systemctl restart httpd

浏览器打开10.0.0.31/dashboard

用户名 admin,密码 ADMIN_PASS,域default

## 3.10 启动一个云主机

控制节点执行：
1. 创建网络，网络名和子网

neutron net-create --shared --provider:physical_network provider --provider:network_type flat oldboy

neutron subnet-create --name oldgirl --allocation-pool \
start=10.0.0.101,end=10.0.0.250 --dns-nameserver 223.5.5.5 \
--gateway 10.0.0.2 oldboy 10.0.0.0/24

vim /etc/neutron/plugins/ml2/ml2_conf.ini
网络名字provider

2. 创建云主机的硬件配置方案

openstack flavor create --id 0 --vcpus 1 --ram 64 --disk 1 m1.nano

openstack flavor list
查看有哪些硬件规格方案

3. 创建密钥对

ssh-keygen -q -N "" -f ~/.ssh/id_rsa
openstack keypair create --public-key ~/.ssh/id_rsa.pub mykey

4. 创建安全组规划

openstack security group rule create --proto icmp default
openstack security group rule create --proto tcp --dst-port 22 default

5. 启动一个实例

#sleep 30
网络id怎么查
neutron net-list

openstack server create --flavor m1.nano --image cirros \
--nic net-id=6b0fc3b2-22de-438f-a058-0d4e1189bcd5 \
--security-group default --key-name mykey oldboy

openstack server list

现在只有一个计算节点10.0.0.31
31上/var/lib/nova/instances/ 路径是实例路径，实例id不同
cd /var/lib/nova/instances/91839b1d-7372-4ac5-828a-0d064e13a0e6/
ll -h
虚拟机起来要有磁盘文件和xml配置文件
qemu-img info disk
磁盘文件是一个动态链接
虚拟机是kvm虚拟的方式
netstat -lntup
是在5900端口起的kvm虚拟机

bug1
web界面进入虚拟机控制台bug：电脑未知contrller
修改宿主机hosts解析添加contrller
C:\Windows\System32\drivers\etc\hosts
添加
10.0.0.11 controller

bug2
web界面控制台 grub bug：
计算节点修改nova的配置：vim /etc/nova/nova.conf
添加
virt_type = qemu
3692 cpu_mode = none
重启计算
systemctl restart libvirtd.service openstack-nova-compute.service
web硬重启实例

实例登录；
用户名cirros
密码cubswin:)
进去之后，
cat /etc/os-release 看实例os版本信息

## 3.11 增加一个计算节点并测试

创建centos作为compute2，10.0.0.32，按照前面conpute1方法设置ip

1. 配置yum源

从31上拉过来openstack_rpm.tar.gz
cd /opt
scp -rp 10.0.0.31:/opt/openstack_rpm.tar.gz .
tar xf openstack_rpm.tar.gz

配置本地yum源
scp -rp 10.0.0.31:/etc/yum.repos.d/local.repo /etc/yum.repos.d/
ll /etc/yum.repos.d/

挂载光盘
mount /dev/cdrom /mnt

挂载光盘开启启动
echo 'mount /dev/cdrom /mnt' >>/etc/rc.local
chmod +x /etc/rc.local

yum makecache
2. 时间同步

yum install chrony -y
vim /etc/chrony.conf
systemctl restart chronyd

3. 安装openstack客户端和openstack-selinux

yum install python-openstackclient openstack-selinux -y

4. 安装nova-compute

yum install openstack-nova-compute -y
yum install openstack-utils.noarch -y

openstack-config --set /etc/nova/nova.conf  DEFAULT rpc_backend  rabbit
openstack-config --set /etc/nova/nova.conf  DEFAULT auth_strategy  keystone
openstack-config --set /etc/nova/nova.conf  DEFAULT my_ip  10.0.0.32
openstack-config --set /etc/nova/nova.conf  DEFAULT use_neutron  True
openstack-config --set /etc/nova/nova.conf  DEFAULT firewall_driver  nova.virt.firewall.NoopFirewallDriver

openstack-config --set /etc/nova/nova.conf  glance api_servers  http://controller:9292
openstack-config --set /etc/nova/nova.conf  keystone_authtoken  auth_uri  http://controller:5000
openstack-config --set /etc/nova/nova.conf  keystone_authtoken  auth_url  http://controller:35357
openstack-config --set /etc/nova/nova.conf  keystone_authtoken  memcached_servers  controller:11211
openstack-config --set /etc/nova/nova.conf  keystone_authtoken  auth_type  password
openstack-config --set /etc/nova/nova.conf  keystone_authtoken  project_domain_name  default
openstack-config --set /etc/nova/nova.conf  keystone_authtoken  user_domain_name  default
openstack-config --set /etc/nova/nova.conf  keystone_authtoken  project_name  service
openstack-config --set /etc/nova/nova.conf  keystone_authtoken  username  nova
openstack-config --set /etc/nova/nova.conf  keystone_authtoken  password  NOVA_PASS
openstack-config --set /etc/nova/nova.conf  oslo_concurrency lock_path  /var/lib/nova/tmp
openstack-config --set /etc/nova/nova.conf  oslo_messaging_rabbit   rabbit_host  controller
openstack-config --set /etc/nova/nova.conf  oslo_messaging_rabbit   rabbit_userid  openstack
openstack-config --set /etc/nova/nova.conf  oslo_messaging_rabbit   rabbit_password  RABBIT_PASS

openstack-config --set /etc/nova/nova.conf  vnc enabled  True
openstack-config --set /etc/nova/nova.conf  vnc vncserver_listen  0.0.0.0
openstack-config --set /etc/nova/nova.conf  vnc vncserver_proxyclient_address  '$my_ip'
openstack-config --set /etc/nova/nova.conf  vnc novncproxy_base_url  http://controller:6080/vnc_auto.html

openstack-config --set /etc/nova/nova.conf  neutron url  http://controller:9696
openstack-config --set /etc/nova/nova.conf  neutron auth_url  http://controller:35357
openstack-config --set /etc/nova/nova.conf  neutron auth_type  password
openstack-config --set /etc/nova/nova.conf  neutron project_domain_name  default
openstack-config --set /etc/nova/nova.conf  neutron user_domain_name  default
openstack-config --set /etc/nova/nova.conf  neutron region_name  RegionOne
openstack-config --set /etc/nova/nova.conf  neutron project_name  service
openstack-config --set /etc/nova/nova.conf  neutron username  neutron
openstack-config --set /etc/nova/nova.conf  neutron password  NEUTRON_PASS

5. 安装neutron-linux-bridge-agent

yum install openstack-neutron-linuxbridge ebtables ipset -y

openstack-config --set /etc/neutron/neutron.conf  DEFAULT rpc_backend  rabbit
openstack-config --set /etc/neutron/neutron.conf  DEFAULT auth_strategy  keystone
openstack-config --set /etc/neutron/neutron.conf  keystone_authtoken auth_uri  http://controller:5000
openstack-config --set /etc/neutron/neutron.conf  keystone_authtoken auth_url  http://controller:35357
openstack-config --set /etc/neutron/neutron.conf  keystone_authtoken memcached_servers  controller:11211
openstack-config --set /etc/neutron/neutron.conf  keystone_authtoken auth_type  password
openstack-config --set /etc/neutron/neutron.conf  keystone_authtoken project_domain_name  default
openstack-config --set /etc/neutron/neutron.conf  keystone_authtoken user_domain_name  default
openstack-config --set /etc/neutron/neutron.conf  keystone_authtoken project_name  service
openstack-config --set /etc/neutron/neutron.conf  keystone_authtoken username  neutron
openstack-config --set /etc/neutron/neutron.conf  keystone_authtoken password  NEUTRON_PASS
openstack-config --set /etc/neutron/neutron.conf  oslo_concurrency lock_path  /var/lib/neutron/tmp
openstack-config --set /etc/neutron/neutron.conf  oslo_messaging_rabbit rabbit_host  controller
openstack-config --set /etc/neutron/neutron.conf  oslo_messaging_rabbit rabbit_userid  openstack
openstack-config --set /etc/neutron/neutron.conf  oslo_messaging_rabbit rabbit_password  RABBIT_PASS

openstack-config --set /etc/neutron/plugins/ml2/linuxbridge_agent.ini  linux_bridge physical_interface_mappings  provider:ens33
openstack-config --set /etc/neutron/plugins/ml2/linuxbridge_agent.ini  securitygroup enable_security_group  True
openstack-config --set /etc/neutron/plugins/ml2/linuxbridge_agent.ini  securitygroup firewall_driver  neutron.agent.linux.iptables_firewall.IptablesFirewallDriver
openstack-config --set /etc/neutron/plugins/ml2/linuxbridge_agent.ini  vxlan enable_vxlan  False

6. 启动服务

systemctl enable libvirtd.service openstack-nova-compute.service
systemctl start libvirtd.service openstack-nova-compute.service

systemctl enable neutron-linuxbridge-agent.service
systemctl start neutron-linuxbridge-agent.service

7. 创建虚拟机检查新计算节点是否可用

控制节点上检查，看看有没有注册compute2
nova service-list
neutron agent-list

新增加的计算节点检测是否可用环节：
将新计算节点添加到一个主机聚集中，在此主机聚集中新创建虚拟机，查看虚机实例是否创建成功

## 3.12 openstack用户项目角色的关系

创建域``default``：openstack domain create --description "Default Domain" default

创建 admin 项目：openstack project create --domain default \
  --description "Admin Project" admin

创建 admin 用户：openstack user create --domain default \
  --password ADMIN_PASS admin

创建 admin 角色：openstack role create admin

添加``admin`` 角色到 admin 项目和用户上：openstack role add --project admin --user admin admin

角色有admin和user，admin用户给普通用户user升级为admin角色后，user居然可以去操作admin，不合理
解决：三种角色，全局admin，普通administrator，user

## 3.13 镜像服务glance迁移

1. 停止控制节点的glance服务
glance现在在控制节点10.0.0.11上，控制节点11上执行
systemctl stop openstack-glance-api.service openstack-glance-registry.service
开机取消
systemctl disable openstack-glance-api.service openstack-glance-registry.service

2. 在compute2上安装mariadb
32上执行
yum install mariadb mariadb-server python2-PyMySQL -y

systemctl start mariadb
systemctl enable mariadb

mysql_secure_installation
直接回车
n
y
y
y
y
3. 恢复glance数据库的数据

控制节点备份数据库








