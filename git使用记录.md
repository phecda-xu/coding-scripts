# gitlab-git

## 拉取

```
$ git clone https://github.com/phecda-xu/coding-scripts.git
```

## 新建branch

- 手动新建后更新代码

```
$ git pull
```

## 切换branch

```
$ git checkout dev
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