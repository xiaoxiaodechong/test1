Issues用来显示别人帮你提交的bug
code代表代码

git  add  文件名.格式  把本地文件添加到暂存区中

git commit  -m " 文件操作说明 "

git   config  --list   查看配置文件

git  clone  "github仓库文件名"

git   status   查看文件的的状态

git  push   同步到github远程仓库

git  reset  HEAD  "文件名"  撤回指定提交文件到暂存区操作  ，不写文件撤回上一步文件的操作


更改git 中配置文件config[remote "origin"]
	url = https://用户名:密码@github.com/xiaoxiaodechong/test1.git
	fetch = +refs/heads/*:refs/remotes/origin/*

