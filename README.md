# ycsb 压测mongodb 性能

#### 项目介绍
实现ycsb对mongodb的自动化压测。

#### 软件架构
ycsb.py -->ycsb.sh


#### 安装教程

1. 安装jdk 版本>1.8
```
javac -version
```
2. 安装ycsb
```
curl -O --location https://github.com/brianfrankcooper/YCSB/releases/download/0.15.0/ycsb-0.15.0.tar.gz
tar xfvz ycsb-0.15.0.tar.gz
cd ycsb-0.15.0
```

#### 使用说明

1. 更改 workloads/workloada 自定义模式
>![workloads/workloada](https://images.gitee.com/uploads/images/2018/0827/141911_e3c48b03_1753909.png "屏幕截图.png")
2. 更改config.ini 配置文件
```
[mongodb]
mongodb_url=
[ycsb]
work=
# list形式 [1,10,20]
recordcount_list=
threads_list= 
```
3. 执行ycsb.py脚本
`python ycsb.py`
>![执行结果](https://images.gitee.com/uploads/images/2018/0827/145933_4e729cc1_1753909.png "屏幕截图.png")

4. 数据统计
>将lujin.txt结果填写如下表格：
![输入图片说明](https://images.gitee.com/uploads/images/2018/0827/150828_48bbc12e_1753909.png "屏幕截图.png")
服务器资源监控图：  
![输入图片说明](https://images.gitee.com/uploads/images/2018/0827/150855_c6be5eb5_1753909.png "屏幕截图.png")
![输入图片说明](https://images.gitee.com/uploads/images/2018/0827/150902_a6f6ef53_1753909.png "屏幕截图.png")
#### 参与贡献

1. Fork 本项目
2. 新建 Feat_xxx 分支
3. 提交代码
4. 新建 Pull Request


#### 码云特技

1. 使用 Readme\_XXX.md 来支持不同的语言，例如 Readme\_en.md, Readme\_zh.md
2. 码云官方博客 [blog.gitee.com](https://blog.gitee.com)
3. 你可以 [https://gitee.com/explore](https://gitee.com/explore) 这个地址来了解码云上的优秀开源项目
4. [GVP](https://gitee.com/gvp) 全称是码云最有价值开源项目，是码云综合评定出的优秀开源项目
5. 码云官方提供的使用手册 [https://gitee.com/help](https://gitee.com/help)
6. 码云封面人物是一档用来展示码云会员风采的栏目 [https://gitee.com/gitee-stars/](https://gitee.com/gitee-stars/)