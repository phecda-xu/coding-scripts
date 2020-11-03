# pycharm 使用

## 使用flask时debug

```
在server.py中设置断点后用debug模式运行，client.py脚本执行时，无法debug进入server的断点。

File | Settings | Build, Execution, Deployment | Python Debugger | Gevent Compatible  取消该设置。
```

## debug 时出卡在某个断点

```
表现为在某个断点执行后卡住，排除代码错误，死循环等情况。

File | Settings | Build, Execution, Deployment | Python Debugger | Gevent Compatible  勾选该设置。
```
