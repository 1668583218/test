# test
测试
push的时候是main分支，不是天杀的master，干
一.Git 其常用命令介绍
第 1 个命令：git status
在命令行窗口的光标处，输入git status命令，查看仓库的状态：
第 2 个命令：git init
在命令行窗口的光标处，输入git init命令，初始化 Git 仓库：
第 3 个命令：git add
在命令行窗口的光标处，输入git add hit.txt命令，将hit.txt文件添加到 Git 仓库：
第 4 个命令：git commit
在命令行窗口的光标处，输入git commit -m "text commit"命令，将hit.txt文件提交到 Git 仓库：
第 5 个命令：git log
在命令行窗口的光标处，输入git log"命令，打印 Git 仓库提交日志：
第 6 个命令：git branch
在命令行窗口的光标处，输入git branch命令，查看 Git 仓库的分支情况：
第 7 个命令：git checkout
在命令行窗口的光标处，输入git checkout a命令，切换到a分支：
第 8 个命令：git merge
切换到master分支，然后输入git merge a命令，将a分支合并到master分支：
第 9 个命令：git branch -d & git branch -D
在命令行窗口的光标处，输入git branch -d a命令，删除a分支：
第 10 个命令：git tag
在命令行窗口的光标处，输入git tag v1.0命令，为当前分支添加标签：
二、利用 SSH 完成 Git 与 GitHub 的绑定
第 1 步：生成 SSH key
我们要想生成SSH key，首先就得先安装 SSH，对于 Linux 和 Mac 系统，其默认是安装 SSH 的，而对于 Windows 系统，其默认是不安装 SSH 的，不过由于我们安装了 Git Bash，其也应该自带了 SSH. 可以通过在 Git Bash 中输入ssh命令，查看本机是否安装 SSH：
![image](https://user-images.githubusercontent.com/57259494/164389764-9adf9ac1-ab86-4c95-92b2-c39566f2617e.png)
如上图所示，此结果表示我们已经安装 SSH 啦！接下来，输入ssh-keygen -t rsa命令，表示我们指定 RSA 算法生成密钥，然后敲三次回车键，期间不需要输入密码，之后就就会生成两个文件，分别为id_rsa和id_rsa.pub，即密钥id_rsa和公钥id_rsa.pub. 对于这两个文件，其都为隐藏文件，默认生成在以下目录：
Linux 系统：~/.ssh
Mac 系统：~/.ssh
Windows 系统：C:\Documents and Settings\username\\.ssh
Windows 10 ThinkPad：C:\Users\think\.ssh
密钥和公钥生成之后，我们要做的事情就是把公钥id_rsa.pub的内容添加到 GitHub，这样我们本地的密钥id_rsa和 GitHub 上的公钥id_rsa.pub才可以进行匹配，授权成功后，就可以向 GitHub 提交代码啦！
第 2 步：添加 SSH key
![image](https://user-images.githubusercontent.com/57259494/164389950-22d6f423-a752-4b64-b1e7-5949532b7307.png)
如上图所示，进入我们的 GitHub 主页，先点击右上角所示的倒三角▽图标，然后再点击Settins，进行设置页面；点击我们的头像亦可直接进入设置页面：
如上图所示，进入Settings页面后，再点击SSH and GPG Keys进入此子界面，然后点击New SSH key按钮：
如上图所示，我们只需要将公钥id_rsa.pub的内容粘贴到Key处的位置（Titles的内容不填写也没事），然后点击Add SSH key 即可。
第 3 步：验证绑定是否成功
在我们添加完SSH key之后，也没有明确的通知告诉我们绑定成功啊！不过我们可以通过在 Git Bash 中输入ssh -T git@github.com进行测试：
如上图所示，此结果即为Git 与 GitHub 绑定成功的标志。
三、通过 Git 将代码提交到 GitHub
如上图所示，点击 mybatis-tutorial 项目：
![image](https://user-images.githubusercontent.com/57259494/164390306-a43175a8-e647-4a32-b333-2600a601ba66.png)
如上图所示，进入mybatis-tutorial项目后，点击Clone or download，复制上图所示的地址链接。然后，进入我们准备存储 Git 仓库的目录，例如下面我们新建的GitRepo目录， 从此目录进入 Git Bash：
![image](https://user-images.githubusercontent.com/57259494/164390345-8826d606-fc8e-4372-81f2-aa75d210e16a.png)
接下来，输入
git clone https://github.com/guobinhit/mybatis-tutorial.git 
命令，其中clone后面所接的链接为我们刚刚复制的远程仓库的地址：
![image](https://user-images.githubusercontent.com/57259494/164390403-251c9ada-0b24-4cf6-a675-9ac708e0070c.png)
如上图所示，我们已经把远程的mybatis-tutorial仓库clone到本地啦！下面，我们看看clone到本地的仓库内容与远程仓库的内容，是否完全一致：
![image](https://user-images.githubusercontent.com/57259494/164390437-16d54eae-2d34-4c95-97e5-41c687d5d764.png)
如上图所示，显示我们已经把远程仓库mybatis-tutorial的内容都clone到本地啦！接下来，为了方便演示，我们直接把之前重构的「史上最简单的 MyBatis 教程」里面的mybatis-demo项目的代码复制过来：
![image](https://user-images.githubusercontent.com/57259494/164390467-85118568-d046-4e19-a22c-eb9449b15390.png)
如上图所示，我们已经把mybatis-demo项目里面的主要内容src目录和web目录复制过来啦！接下来，从此目录进入 Git Bash，然后输入git status命令查看仓库状态：
![image](https://user-images.githubusercontent.com/57259494/164390504-1761cf86-d35b-4f07-932f-5f62b978c6b6.png)
如上图所示，mybatis-tutorial已经是一个 Git 仓库了，而且在输入git status命令后显示有两个文件未被追踪，也就是我们刚刚复制过来的两个文件没有提交。通过「Git 初体验及其常用命令介绍」，我们已经知道了在真正提交代码之前，需要先进行git add操作：
![image](https://user-images.githubusercontent.com/57259494/164390541-e96fef23-b7b4-4af0-9a39-37ce78db5518.png)
如上图所示，我们已经将src目录add并commit到mybatis-tutorial仓库啦！接下来，我们将web目录提交到仓库，然后输入git log命令查看仓库日志：
![image](https://user-images.githubusercontent.com/57259494/164390589-e5772d51-f23e-4f1e-ab79-27d4c5a30ed8.png)
再输入git status命令查看仓库状态：
![image](https://user-images.githubusercontent.com/57259494/164390631-b078f158-5a36-401b-a48e-14d9ac3affa8.png)
如上图所示，我们已经将mybatis-tutorial仓库里面新添加的两个目录都提交啦！下面，我们将本地仓库的内容push到远程仓库，输入git push origin master命令：
![image](https://user-images.githubusercontent.com/57259494/164390663-eb34aa94-3c1c-418b-822c-bad6f96f1563.png)
如上图所示，在第一次向远程仓库提交代码的时候，需要输入账号及密码进行验证，验证成功后，显示如下结果：
![image](https://user-images.githubusercontent.com/57259494/164390694-094a2de8-db80-44c4-b84c-c5341a87850b.png)
然后，刷新 GitHub 中mybatis-tutorial仓库：
![image](https://user-images.githubusercontent.com/57259494/164390724-ebe3a9bc-5f2b-4c91-9726-c5f01265d73e.png)






