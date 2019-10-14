Issues用来显示别人帮你提交的bug
code代表代码

git  add  文件名.格式  把本地文件添加到暂存区中

git commit  -m " 文件操作说明 "

git   config  --list   查看配置文件

git  clone  "github仓库文件名"

git   status   查看文件的的状态

git  push   同步到github远程仓库

git  reset  -hard HEAD^  "文件名"  撤回指定提交文件到暂存区操作  ，不写文件撤回上一步文件的操作
reset的恢复可简单理解为从commit选择需要回退的版本，然后将对应的版本移动到暂存区，此时，你的本地工作区并没有恢复，
也就是文件没有还原，reset动的是暂存区文件，所以这时本地文件和暂存区文件产生冲突，也就是不相同，所以会提示红色


更改git 中配置文件config[remote "origin"]
	url = https://用户名:密码@github.com/xiaoxiaodechong/test1.git
	fetch = +refs/heads/*:refs/remotes/origin/*

分支管理:未完待续

