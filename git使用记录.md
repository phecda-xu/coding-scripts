# gitlab-git

## git SSH公钥生成

拥有秘钥，就不需要每次下载和上传代码的时候输入账号和密码；

```
$ cd ~/.ssh
$ ssh-keygen -o   # 生成 id_dsa 或 id_rsa 命名的文件，其中一个带有 .pub 扩展名
$ cat ~/.ssh/id_rsa.pub  # 查看ssh 公钥 ，接下来复制公钥发给git管理员就行（其他人的操作，这里暂时不说）
```

## 拉取

```
$ git clone https://github.com/phecda-xu/coding-scripts.git
```

## 新建branch

- 新建分支

```
新建本地分支
$ git checkout -b branch_name
推送到远程(同名)
$ git push origin branch_name:branch_name
```

## 切换branch

```
$ git checkout dev
```

## 删除branch

```
删除本地
$ git branch branch_name -d

删除远程代码仓
$ git push origin --delete branch_name
```

## 合并

- 合并develop 到 master

```
按顺序执行，中间通过 git status 查看当前状态
$ git checkout master
$ git merge develop
$ git commit -m "合并"
$ git status
$ git push
```
- conflict

```
删掉 conflict 部分
git rm <>
git status
git push
```

## 打tag

- 将历史某次commit打上版本tag

```
git tag                                                                          # 查看当前tag
git tag -a v2.0.0  ab33e3c1 -m "5月15日 测试版本"     # -a参数来创建一个带备注的tag，备注信息由-m指定
git push origin v2.0.0
```

## 移除对某个文件的跟踪

- git rm -r --cached

```
git rm -r --cached .   # 移除全部跟踪
git rm -r --cached filename # 移除对某个文件的跟踪

git commit -m "update"
git push
```

## 切换远程仓库地址

- 准备修改

```
git remote set-url origin url
```

- 先删除原本地址，再增加新地址

```
git remote rm origin
git remote add origin https://github.com/phecda-xu/coding-scripts.git
```

- 也可以直接在 .git 文件夹下的config文件中直接修改。

## git pull 冲突解决

- 错误信息

```
error: Your local changes to the following files would be overwritten by merge:
    xxx/xxx/xxx.php
Please, commit your changes or stash them before you can merge.
Aborting
```

- 解决办法

```
git stash  # 将当前的更改存入git栈
git pull
git stash pop # 从git栈中获取最新一次的修改记录，应用到当前的代码中
```

或者

```
git reset --hard # 丢弃当前的所有更改，强制与远程代码仓库对齐
git pull
```
