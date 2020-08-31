# sftp使用记录

sftp 是一个用于在本地主机与服务器主机之间文件传输的工具；

## 安装

SFTP 为SSH的其中一部分，所以安装了ssh的主机基本都可以使用sftp进行文件的传输；

```
$ sudo apt-get install openssh-client
$ sudo apt-get install openssh-server
```

## 访问服务器

```
$ sftp username@127.0.0.1  
# 输入密码后进入
sftp > 
```

## 上传文件

```
$ put 文件路径名 服务器文件路径/
$ put -r 本地文件夹路径名/ 服务器文件夹路径名/
```

## 下载文件

```
$ get 服务器文件路径名 本地路径/
$ get -r 服务器文件夹路径名/ 本地文件夹路径名/
```

## 断开连接

```
$ exit
```
