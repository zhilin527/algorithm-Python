# 1. Vim
## 1.1 模式
- 一般模式
- 插入模式
- 命令行模式
## 1.2 快捷键
- 拷贝当前行 yy，拷贝当前行向下的5行，包括了当前行 5yy， 粘贴至光标下一行 p
- 删除当前行 yy，删除当前行向下的5行，包括了当前行 5yy
- 文件中查找hello，一般模式输入 /hello， n跳至下一个
- 设置行号，:set nu，取消行号:set nonu ，:9，光标跳到第9行
- 一般模式下，gg 光标跳至第一行，G 光标跳到最后一行
- 撤销动作，u 撤销上一次
- x 删除当前光标字符
- 行首行尾，^ 移动至行首，$ 移动至行尾，和正则匹配意思相符

# 2. Linux目录结构
- /bin 常用的命令，/usr/bin,/usr/local/bin
- /sbin 管理员的管理程序, /usr/sbin,/usr/local/sbin
- /root 系统管理员目录
- /lib 系统开机需要的动态链接库
- /lost+found 一半为空，系统非法关机后，这里存放了一些文件
- /etc 配置文件
- /usr 用户应用程序，类似 windows 的 programfiles
- /boot 系统启动
- /proc 系统内存的映射
- /srv service 的缩写，服务启动后需要提取的数据
- /sys linux内核2.6之后新出现的文件系统sysfs
- /tmp 临时文件
- /dev 设备管理器，硬件用文件的形式存储
- /opt 主机额外安装软件的目录
- /mnt 临时挂载别的文件系统
- /usr/local 主机额外安装软件的安装目录，一般是通过源码编译方式安装的程序

# 3. 关机重启登录注销
- shutdown -h now 立刻关机
- shutdown -h 1 1分钟后关机
- shutdown -r now 立刻重启
- halt 立刻关机
- reboot 重启
- sync 把内存的数据同步到磁盘

# 4. 用户管理
本质是对 /etc/passwd 的更新
## 4.1 添加用户
useradd 用户名
useradd -G 用户名 指定用户组
- useradd milan 创建用户 milan，其家目录为 /home/milan
- useradd -d /home/test milan2, 创建用户 milan2, 指定其家目录为 /home/test

## 4.2 指定修改密码
passwd 用户名
- 没有用户名 默认修改当前登录的用户

## 4.3 删除用户
userdel 用户名
- userdel milan 删除用户milan，但是保留其家目录
- userdel -r milan 删除用户milan，及其家目录

## 4.4 查询用户信息
id 用户名
- id zzl

uid=1000(zzl) gid=1000(zzl) 组=1000(zzl),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),113(lpadmin),128(sambashare),999(docker)

## 4.5 切换用户
su - 用户名

## 4.6 查看当前用户
whoami

# 5. 用户组管理
本质是对 /etc/group 的更新
## 5.1 创建用户组
groupadd 组名

## 5.2 删除用户组
groupdel 组名

# 6. 文件属性查看
## 6.1 查看

drwxr-xr-x   2 root root  4096 8月   6 19:53 bin  
drwxr-xr-x   4 root root  4096 8月   6 19:58 boot  
drwxrwxr-x   2 root root  4096 8月   6 19:39 cdrom  
drwxr-xr-x  21 root root  4360 8月  16 18:45 dev  
drwxr-xr-x 134 root root 12288 8月  16 22:08 etc  
drwxr-xr-x   3 root root  4096 8月  10 21:31 home  
lrwxrwxrwx   1 root root    34 8月   6 19:40 initrd.img -> boot/initrd.img-4.15.0-112-generic  
lrwxrwxrwx   1 root root    34 8月   6 19:38 initrd.img.old -> boot/initrd.img-4.15.0-112-generic  
drwxr-xr-x  22 root root  4096 8月   6 19:41 lib  
drwxr-xr-x   2 root root  4096 8月   6 19:53 lib64  
drwx------   2 root root 16384 8月 root
drwxr-xr-x   2 root root  4096 8月   7  2020 mnt  
drwxr-xr-x   8 root root  4096 8月   8 00:44 opt  
dr-xr-xr-x 238 root root     0 8月  16 18:44 proc  
drwx------   4 root root  4096 8月   7 12:22 root  
drwxr-xr-x  29 root root   940 8月  16 18:45 run  
drwxr-xr-x   2 root root 12288 8月   6 19:54 sbin  
drwxr-xr-x   2 root root  4096 8月   6 19:41 snap  
drwxr-xr-x   2 root root  4096 8月   7  2020 srv  
dr-xr-xr-x  13 root root     0 8月  16 22:10 sys  
drwxrwxrwt  13 root root  4096 8月  16 22:52 tmp  
drwxr-xr-x  12 root root  4096 8月   7  2020 usr  
drwxr-xr-x  14 root root  4096 8月   7  2020 var  
lrwxrwxrwx   1 root root    31 8月   6 19:40 vmlinuz -> boot/vmlinuz-4.15.0-112-generi

10 个字符，第一个，接下来三个为一组  
第一个字符：
- [d] 表示文件夹
- [-] 表示文件
- [l] 链接文档

接下来三个为一组，且均为[rwx]的形式，[r]代表可读read，[w]代表可写write，[x]代表可执行execute  
没有对应权限则为[-]

| 文件类型 | 属主权限 | 属组权限 | 其他用户权限 |
| :------: | :------: | :------: | :----------: |
|    0     |   123    |   456    |     789      |
|    d     |   rwx    |   r-x    |     r-x      |
|   目录   | 读写执行 | 读写执行 |   读写执行   |

## 6.2 修改文件属性
- 更改文件属组
chgrp [-R] 属组名 文件名

- 更改文件属主，也可以同时修改所属组
chown [-R] 属主名：属组名 文件名

- 更改文件 9 个属性
chmod [-R] xyz 文件或者目录

Linux文件属性有两种设置方法，一种是数字，一种是符号  
Linux文件的基本属性就有 9 个，分别是owner/group/others三种身份各自的read/write/execute权限

这 9 个权限是 3 个一组的，可以实用数字代表权限：

r:4   w:2   x:1

每种身份owner/group/others的 3 个权限是累加的，
- owner = rwx = 4+2+1 = 7
- group = rwx = 4+2+1 = 7
- others = --- = 0+0+0 = 0

chmod 770 filename  
chmod 664 test.java

# 7. 文件内容查看
- cat 由第一行开始显示文件内容，用来读文章，读取配置文件
- tac 由最后一行开始显示
- nl 显示的时候，顺道输出行号，看代码的时候，希望显示行号，常用
- more 一页一页的显示文件内容
- less 与more类似，但是更好的是，它可以往前翻页
- head -n 3 只看头3行
- tail -n 3 只看尾巴3行

# 8. 软链接和硬链接

硬链接：ln 原文件 链接文件  
软链接：ln -s 原文件 链接

修改原文件后，链接文件，链接都更改  
删除原文件后，链接文件还能访问，链接失效

# 9. 磁盘管理
## 9.1 磁盘
df -h 显示磁盘使用情况  

挂载外部磁盘  
mount /dev/waibu /mnt/zzl  
umount -f [挂载位置]  
挂载/卸载 磁盘

## 9.2 卸载软件
dpkg --get-selections |grep baidunetdisk  
找出软件包  
dpkg -P baidunetdisk  
卸载软件和配置  

# 10. 进程管理
ps -xx：  
-a 显示当前终端运行的所有进程信息  
-u 以用户的信息显示进程  
-x 显示后台运行进程的参数  

ps -aux | grep xx  
| 管道符，将前一个结果作为第二条语句的参数  

ps -ef | grep xx  
可以查看到父进程的信息  

pstree -pu   
-p  显示父id  
-u  显示用户组  

结束进程  
kill -9 进程id  

查看端口情况  
netstat -anp | grep 8080  
-a  查看已经连接的服务端口（ESTABLISHED）  
-n  
-p  查看所有服务端口（LISTEN，ESTABLISHED） 

lsof -i:8888  
查看端口 8888 的进程情况  


