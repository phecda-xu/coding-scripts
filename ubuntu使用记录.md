# ubuntu相关的系统使用记录

## 1、图形界面卡死重启

```
$ sudo service lightdm restart
```

## 2、指令清空垃圾箱

```
安装一个工具
$ sudo apt install trash-cli
清空
$ trash-empty
```

或者

```
$ cd .local/share/Trash/
$ cd files
$ rm -rf *
```

