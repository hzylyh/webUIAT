# webUIAT
## 技术栈
- python
- selenium
- vue3
- typescript
- mysql

## 思想
- PO
- 关键字驱动

## 宗旨
最简化的元素维护，最便捷的使用体验

## 依赖
- Mysql


## 开发环境启动
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

# 5.修改配置
1)修改database/manager.py, 将数据库信息修改为自己的
2)导入数据库脚本, 脚本在sql目录下

# 5.运行后端项目
python3 main.py

# 6.克隆前端项目
git clone https://github.com/hzylyh/ztui-web.git

# 7.安装环境依赖
npm install

# 8.运行前端开发环境
npm run serve

```


## FAQ
如遇到mac无法验证的情况，执行如下命令
```shell
xattr -d com.apple.quarantine chromedriver
```
