Issues用来显示别人帮你提交的bug
code代表代码

git  add  文件名.格式  把本地文件添加到暂存区中

git commit  -m " 文件操作说明 "

git   config  --list   查看配置文件

git -log  打印日志  （显示快照）

git -log  --decorate  显示HEAD 指针指向

git -log  --decorate   --oneline   显示一个快照

git -log  --decorate   --oneline   --graph --all   以图形化显示分支和快照

git  clone  "github仓库文件名"

git   status   查看文件的的状态

git  push   同步到github远程仓库

git  reset  -hard HEAD^  "文件名"  撤回指定提交文件到暂存区操作  ，不写文件撤回上一步文件的操作
reset的恢复可简单理解为从commit选择需要回退的版本，然后将对应的版本移动到暂存区，此时，你的本地工作区并没有恢复，
也就是文件没有还原，reset动的是暂存区文件，所以这时本地文件和暂存区文件产生冲突，也就是不相同，所以会提示红色

更改git 中配置文件config[remote "origin"]
	url = https://用户名:密码@github.com/xiaoxiaodechong/test1.git
	fetch = +refs/heads/*:refs/remotes/origin/*

git  commit --amend 执行选项commit   提交命令 git会更改的最近修改

删除文件  git  rm  文件名  git会和缓存区的文件进行对比，所以要进行返回上一操作 用git -reset --soft HEAD^

***git    checkout  -- 文件名     恢复文件***

git  rm -f  强制删除（删除暂存区和工作区 ）

git    rm  -cached      (删除暂存区文件)

修改名字   mv  旧名字  新名字

分支管理:

主分支  master

创建分支 git  branch  分支名

master.分支名

***git  checkout   分支名 切换分支***

实际开发不止一个分支

合并分支：git  merge 

如果遇到命名相同文件时会报错，请修改冲突文件需要改内容   

消除冲突： git commit  -m  "fix  conflicts"

删除分支   git  branch  -b 分支名

 



 

