# docker 使用简单总结

by: phecda-xu

##  Images

镜像，虚拟系统源，可以看做是一个系统的软件包

```
查看已下载的镜像：
$ docker images

下载一个镜像（镜像库可以用dockerhub或者企业自建库）

$ docker pull image_name:version
```



## Container

容器，由镜像启动的一个虚拟主机(类似于在一个设备上装一个操作系统)，一个设备上可以基于一个镜像同时启动多个容器，每个容器之间相互隔离。进入容器后就是一个一般的linux系统，用指令操作。我们说使用docker 实际上主要是在容器内进行作业操作。

```
由镜像启动一个新的容器：

$ docker run -it image_name:version [-v main_path:container_path] [-p ip]  /bin/bash

 -v (挂载硬盘，可选项，一般挂载训练数据位置，容器内只存放代码，通过挂载盘访问存放在容器外硬盘上的数据)
 -p (ip端口映射，用于flask服务等)

查看当前已经启动的容器：

$ docker ps

查看历史启动过的容器：

$ docker ps -a

启动关闭的容器：

$ docker start containerID

关闭一个启动的容器：

$ docker stop containerID

删除一个关闭的容器：

$ docker rm containerID

进入一个已经启动的容器：

$ docker exec -it containerID /bin/bash

如果要用GPU，那么上述指令操作时将docker换为nvidia-docker 
```



示例：

```
镜像启动新容器：

$ nvidia-docker run -it kaldiasr/kaldi:gpu-latest -v /home/xhongyang/phecda/data/:/root/data /bin/bash

一般启动成功会直接进入容器内部，如下

root@e78715948e42:/opt/kaldi#

其中 e78715948e42 为容器的ID

-v 设置让你可以在 容器内的 /root/data 地址下看到 服务器 /home/xhongyang/phecda/data/ 地址下的数据

退出并关闭容器：ctrl + D
退出不关闭容器：Ctrl+P+Q

容器没关闭时重新进入容器，直接进：
nvidia-docker exec -it e78 /bin/bash

容器关闭时进入容器，先启动后进：
nvidia-docker start e78
nvidia-docker exec -it e78 /bin/bash
```

