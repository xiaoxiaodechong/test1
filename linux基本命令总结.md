## linux基本命令总结

#### 1.linux 基本思想：

1.一切皆对象

2.每个软件都有确定的用途

#### 2.shell提示符

1.超级管理员root：#

2.一般对象：$

#### 3.文件的基本命令管理

1.cd命令，切换目录

2.ls命令：查看目录内容

3.pwd：查看当前目录的路径

#### 4.linux的主要文件及其作用：

1./根目录 ，一切文件的源头

2、/root系统管理员的目录

3.bin目录：存放着标准的linux的工具，比如：ls,cd 等 ，也可以自己创建工具

4./etc:主要存放着系统配置方面的文件。你安装了samba这个套件，当你想要修改samba配置文件的时候，你会发现它们(配置文件)就在/etc/samba目录下

5./dev :这里存放着与设备 相关的文件

6./home 这里主要存放着个人数据，具体每个用户的配置文件，用户桌面文件（root用户除外）

7./tmp :临时目录，对于某些程序来说，一些文件被使用一两次之后，就不会被再利用，相当于缓存文件

8./usr在这个目录下，你可以找到那些不适合放在/bin或/etc目录下的额外的工具。比如像游戏阿，一些打印工具拉等等。/usr目录包含了许多子目录： /usr/bin目录用于存放程序;/usr/share用于存放一些共享的数据，比如音乐文件或者图标等等;/usr/lib目录用于存放那些不能直接 运行的，但却是许多程序运行所必需的一些函数库文件。你的软件包管理器(应该是“新立得”吧)会自动帮你管理好/usr目录的。

9./opt 主要存放可选程序你想尝试最新的firefox测试版吗?那就装到/opt目录下吧，这样，当你尝试完，想删掉firefox的时候，你就可 以直接删除它，而不影响系统其他任何设置。安装到/opt目录下的程序，它所有的数据、库文件等等都是放在同个目录下面。

10. /usr/local这里主要存放那些手动安装的软件
11.  /media有些linux的发行版使用这个目录来挂载那些usb接口的移动硬盘(包括U盘)、CD/DVD驱动器等等。

#### 6.linux命令常用分类 

##### 分类一

1.外部命令：属于shell 解释器的一部分：已经调入到内存，文件中找不到

2.外部命令：独立在shell解释器之外的文件 在文件目录/bin下

     查看方式：type -a ls
​      显示：  ls is aliased to `ls --color=auto'
​                    ls is /bin/ls

内部命令：help :使用方式：--help

查看命令使用：man 、info 通常使用info

##### 分类二

功能分类：

###### 1.目录操作：

mkdir -p 创建目录 、删除空目录：rmdir   rmdir -p (parents父母) 删除指定目录和上级目录：

cp 复制目录

###### 2.文件操作：

一.which 查看命令位置：which  命令名

二.touch 创建文件

三.cp 复制文件  cp 文件名   复制到的路径

四.mv 移动文件

五.rm 删除文件  rm  -r (recursive	递归删除目录及其内容)-f(-f, --force		强制删除。忽略不存在的文件，不提示确认)

六.file 查看文件的类型

七.stat 查看文件属性

###### 3.文件查看

1.cat 查看文件内容

2.tac 倒序查看文件内容

3.more 分页显示

4.less 分页显示内容

5.tail 查看文件尾部的内容 默认为十行 ，可以指定看几行

6.head 查看文件的头部行 默认十行，可以指定查看几行

###### 4.文件内容编辑

1.Ctrl +c 取消正在执行的命令

2.ctrl +l清屏

3.ctrl +a  跳转到首行

4.Ctrl +e跳转尾部

5.ctrl+z暂停当前目录送至后台

###### 5.查看用户登入命令：

su  用户切换 

who 当前用户 

w:  当前用户登入的信息和设备

ps:  查看线程  PID号  ps -ef 查看全部线程，以ASCll 码来实现

kill -9 pid号：杀死进程

###### 6.系统管理类命令：

sudo stutdown -h  now  现在关机

sudo stutdown -h +10  十分钟后关机

sudo reboot 重启

###### 7.日期时间管理类命令

date:显示时间

clock：管理硬件时钟

###### 重点 1、Linux系统安装：

查看防火墙：service iptabes status

关闭防火墙：service iptabes stop

启动防火墙：service iptables start

启动mysql：service mysqld start  

关闭mysql：service mysqld stop  

查看mysql:  service mysqld status

#### 



