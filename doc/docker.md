# 1. 虚拟机技术
![Image in doc_img_docker may be lost.](https://raw.githubusercontent.com/zhilin527/algorithm-Python/master/doc/doc_img_docker/vm_structure.png)

## 1.1 Hypervisor:虚拟机监视软件
划分为两类：
1.这种直接运行在物理硬件之上的,比如基于内核的虚拟机 KVM, Linux 内核的一个模块
2.运行在另一个操作系统之上，比如 QEMU, WINE, VMware QEMU 多用来做 CPU 仿真, 做调试

## 1.2 Hypervisor 作用
多部署
资源池，共享主机资源
资源隔离

# 2. 容器Docker
![Image in doc_img_docker may be lost.](https://raw.githubusercontent.com/zhilin527/algorithm-Python/master/doc/doc_img_docker/docker.png)

## 2.1 docker应用场景
- 标准化的迁移方式，开发打包资源文件给运维，运维展开放到对应的资源节点的服务器上
- 统一的参数配置，打包时的参数配置都是一样的
- 自动化部署
- 应用集群监控
- 开发和运维之间的沟通桥梁

## 2.2 docker 概述
### 2.2.1 docker作用
- 开发和部署环境不一样，而环境配置十分麻烦
如在Windows上开发，要发布到Linux上运行。Docker给以上问题提出了解决方案：
Java --- Jar(环境）---打包项目带上环境（镜像）---Docker仓库（应用商店）---下载镜像---直接运行
- Docker的思想来自于集装箱，核心思想：隔离。
即将应用打包装箱，每个箱子是互相隔离的，可以将服务器利用到极致。

## 2.3 docker 安装
### 2.3.1 docker的组成
![Image in doc_img_docker may be lost.](https://raw.githubusercontent.com/zhilin527/algorithm-Python/master/doc/doc_img_docker/docker_structure.png)
- **镜像image**
一个模板，可以通过这个模板创建容器，tomcat镜像==>run==>tomcat01容器（提供服务器），
通过这个镜像创建多个容器，最终服务是运行在容器中的。
- **容器container**
启动，停止，删除，基本命令
可以把一个容器理解为一个简易的linux系统
- **仓库reporepository**
仓库就是存放镜像的地方
仓库分为公有仓库和私有仓库。

### 2.3.2 ubuntu 安装命令
- ***卸载旧版本***

```sudo apt-get remove docker docker-engine docker.io containerd runc```
- ***安装依赖***

```sudo apt-get update```\
```sudo apt-get install apt-transport-https ca-certificates curl gnupg lsb-release```

- ***添加docker key***

```curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg```

- ***设置ubuntu系统对应稳定版***

```echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu``` \
```$(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null```

- ***安装docker***

```sudo apt-get update```

```sudo apt-get install docker-ce docker-ce-cli containerd.io```

- ***卸载docker***

```sudo apt-get purge docker-ce docker-ce-cli containerd.io```

```sudo rm -rf /var/lib/docker```

```sudo rm -rf /var/lib/containerd```

- ***运行 hello-world***

- ***使用阿里云容器镜像加速服务***

```https://cr.console.aliyun.com/cn-beijing/instances/mirrors```

阿里云控制台 - 产品与服务 - 弹性计算 - 容器镜像服务 - 镜像工具 - 镜像加速器

- ***docker run 运行流程***

![Image in doc_img_docker may be lost.](https://raw.githubusercontent.com/zhilin527/algorithm-Python/master/doc/doc_img_docker/docker_run.png)

### 2.3.3 底层原理

- ***docker 怎么工作***

![Image in doc_img_docker may be lost.](https://raw.githubusercontent.com/zhilin527/algorithm-Python/master/doc/doc_img_docker/docker_how_to_work.png)

Docker是一个Client-Server结构的系统，以守护进程运行在主机上。通过Socket从客户端进行访问。

- ***docker 为什么比 VM 快***

![Image in doc_img_docker may be lost.](https://raw.githubusercontent.com/zhilin527/algorithm-Python/master/doc/doc_img_docker/docker_and_vm.png)
1. docker 抽象层更少
2. docker 利用的是宿主机的内核，vm 需要 Guest OS

### 2.3.4 安装之后

docker安装完成，一般用户没有权限启动docker服务，只能通过sudo来通过root用户权限来启动docker，此时对于一般用户而言，需要执行docker ps或者docker images命令查看容器或者镜像提示如题所示的错误。

```sudo gpasswd -a $USER docker```
```newgrp docker```

## 2.4 docker 常用命令
### 2.4.1 帮助命令

```docker --help            # 帮助信息```\
```docker info              # 系统信息，包括镜像和容器的数量```
### 2.4.2 镜像命令

- docker images 查看所有本地主机上的镜像

```[root@iZ2zeg4ytp0whqtmxbsqiiZ ~]# docker images```\
```REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE```\
```hello-world         latest              bf756fb1ae65        7 months ago        13.3kB```\
```# 解释```\
```REPOSITORY      # 镜像的仓库```\
```TAG             # 镜像的标签```\
```IMAGE ID        # 镜像的ID```\
```CREATED         # 镜像的创建时间```\
```SIZE            # 镜像的大小```\
```# 可选项```\
```--all , -a      # 列出所有镜像```\
```--quiet , -q    # 只显示镜像的id```

- docker search 查找镜像\
- docker pull 下拉镜像

<code>
下载镜像，docker pull 镜像名[:tag]

[root@iZ2zeg4ytp0whqtmxbsqiiZ ~]# docker pull mysql \
Using default tag: latest           # 如果不写tag，默认就是latest \
latest: Pulling from library/mysql \
bf5952930446: Pull complete         # 分层下载，dockerimages的核心，联合文件系统 \
8254623a9871: Pull complete \
938e3e06dac4: Pull complete \
ea28ebf28884: Pull complete \
f3cef38785c2: Pull complete \
894f9792565a: Pull complete \
1d8a57523420: Pull complete \
6c676912929f: Pull complete \
ff39fdb566b4: Pull complete \
fff872988aba: Pull complete \
4d34e365ae68: Pull complete \
7886ee20621e: Pull complete \
Digest: sha256:c358e72e100ab493a0304bda35e6f239db2ec8c9bb836d8a427ac34307d074ed     # 签名 \
Status: Downloaded newer image for mysql:latest \
docker.io/library/mysql:latest      # 真实地址

等价于 \
docker pull mysql \
docker pull docker.io/library/mysql:latest
 
指定版本下载 \
[root@iZ2zeg4ytp0whqtmxbsqiiZ ~]# docker pull mysql:5.7

5.7: Pulling from library/mysql \
bf5952930446: Already exists \
8254623a9871: Already exists \
938e3e06dac4: Already exists \
ea28ebf28884: Already exists \
f3cef38785c2: Already exists \
894f9792565a: Already exists \
1d8a57523420: Already exists \
5f09bf1d31c1: Pull complete \
1b6ff254abe7: Pull complete \
74310a0bf42d: Pull complete \
d398726627fd: Pull complete \
Digest: sha256:da58f943b94721d46e87d5de208dc07302a8b13e638cd1d24285d222376d6d84 \
Status: Downloaded newer image for mysql:5.7 \
docker.io/library/mysql:5.7
 
查看本地镜像

[root@iZ2zeg4ytp0whqtmxbsqiiZ ~]# docker images \
REPOSITORY          TAG                 IMAGE ID             CREATED             SIZE \
mysql               5.7                 718a6da099d8        6 days ago          448MB \
mysql               latest              0d64f46acfd1        6 days ago          544MB \
hello-world         latest              bf756fb1ae65        7 months ago        13.3kB \
</code>

- 删除镜像

```[root@iZ2zeg4ytp0whqtmxbsqiiZ ~]# docker rmi -f IMAGE ID                        # 删除指定镜像``` \
```[root@iZ2zeg4ytp0whqtmxbsqiiZ ~]# docker rmi -f IMAGE ID1 IMAGE ID2 IMAGE ID3   # 删除多个镜像``` \
```[root@iZ2zeg4ytp0whqtmxbsqiiZ ~]#  docker rmi -f $(docker images -aq)           # 删除所有镜像``` \

### 2.4.3 容器命令

## 2.5 docker 镜像讲解


## 2.6 docker 容器数据卷


## 2.7 DockerFile


## 2.8 docker 网络

docker 的笔记
