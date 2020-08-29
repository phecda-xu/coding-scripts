# gitlab-git

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
