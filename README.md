# webUIAT
## 技术栈
- python
- selenium

后续会加入vue做展示，包括数据库等

## 思想
- PO
- 关键字驱动

## 宗旨
最简化的元素维护，最便捷的使用体验

## 启动
```shell
# 1.克隆项目
git clone https://github.com/hzylyh/webUIAT.git
cd webUIAT

# 2.新建虚拟环境
python3 -m venv ./venv

# 3.激活虚拟环境
# linux
./venv/bin/activate
# windows
venv\Scripts\activate

# 4.安装依赖
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt

# 5.运行项目
python3 main.py
```

## 使用说明
1 配置application.yml
配置项目路径

2 新建项目目录
在项目目录下新建project.yml,自行添加项目地址
和驱动路径

3 新建目录po和testcase
（1)目录po
主要存放页面对象文件，比如可以把登录页看成一个
页面对象，对象里会有多个属性，比如当前登录页
对象中属性有输入用户名、点击密码、点击登录等

（2）目录testcase
此目录主要用来撰写页面自动化测试用例。
用例字段包括：
1）用例编号：随意输入，比如01
2）用例模块：对应用户的模块名称，比如登录模块
3）用例名称：简单描述下用例
4）用例步骤：具体的用例步骤
5）页面对象：即输入目录po下的页面对象名称，比如
登录页
6）对象属性：输入页面对象对应的属性， 比如页
面对象登录页下的对象属性输入用户名
7）输入值：比如输入用户名这个属性需要输入对
应的值，比如sandy。没有输入值的话，可以为空
8）预期值：此字段主要用来做结果校验，比如
登录到首页后，校验首页标题，就可以用预期值
和实际返回结果进行校验

4 实例讲解
场景描述：打开网站后，输入用户名和密码，点击
登录，进入对应的首页。

第一步：在目录po下新建yml文件，命名为登录页

第二步：根据页面元素定位，撰写文件内容
登录页文件内容如下：
输入用户名:
  type: id
  value: username
  action: input

输入密码:
  type: id
  value: password
  action: input

点击登录:
  type: id
  value: submit1
  action: click

1）输入用户名、输入密码、点击登录都是对象
属性
2）type:id  ---->页面元素根据id进行定位
3）value：xxx   ---->id对应的值
4）action:  -----> 动作，可以是input、
click等

第三步：打开testcase目录下对应的文件，撰写
对应的页面自动化测试用例
1）用例编号：1
2）用例模块：登录
3）用例名称：正常登录
4）用例步骤：输入对应的用户名
5）页面对象：登录页
6）对象属性：输入用户名
7）输入值：wangj
8）预期值：为空

此处一共撰写三条用例，其他两条和上面的类似

第四步：运行程序


## FAQ
如遇到mac无法验证的情况，执行如下命令
```shell
xattr -d com.apple.quarantine chromedriver
```
