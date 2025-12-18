# GitHub Testing
# python_learning_week1
本笔记整理了作者在学习老男孩教育python课程的一些笔记，周数仅代表其录播课程安排，与实际进度不符。

本文档开始写于2025.12.16，后续有所补充

## 基本书写规则
### 单行注释
最前面加#即可，也可以使用快捷键Command + / （下面那个斜线）

### 多行注释
'''

多行文本

'''

## 字符串与文本处理
### 字符串方法
lower() 将字符串变成小写

例如name.lower()
```python
if guess_str.lower() == "q":
  quit_flag = True
  break
```

### 转义字符
\n 换行

\" 显示引号

引号还可以单双配合：
```python
'他说："你好"'
"It's OK"
```
### f-string（字符串中显示变量）:
```python
info = f'''
info of {name}
his age is {age}
his job is {job}
'''
```
## 用户输入与交互
### 普通输入
```python
name = input("please input your name:")
```
### 隐藏输入
```python
import getpass
password = getpass.getpass("please input your password:")
#结构为：模块.函数（），需要import
```

## 异常处理
以下部分放在while循环中使用
```python
try:
    guess = int(guess_str)
except ValueError: #如果有多个异常检测，写成except (ValueError,IndexError):
    print("请输入有效数字")
    continue
```
## 流程控制
### 循环
continue：直接回到本循环开头

break：直接结束本循环

### 循环+else
正常结束循环后（非break出来的）执行else中的代码

## for循环
### for可以遍历的对象：
range，列表，字符串，字典，文件对象

for循环会创建一个变量，且循环结束后会保留其值

# 课后作业及自学
## 不知道放在哪里的一些小碎知识点
.strip()可以将字符串前后两端的空格、换行等无效空白字符去掉，算是一种冗余设计，防止用户误输入

例如“jid”和“jid ”

.lower()可以将字符串转为小写，写到这里想起来了，顺便一提。
```python
for line in lines:
    if not line.strip(): #strip()可以去掉变量中两头的空格、换行等无效空白字符
        continue        #if not xxx: xxx如果为false才进入，字符串如果为空也算一种false
    username, password = line.split(",",1) #最多分割一次
    users[username] = password
```
list()：把一个可遍历的东西，按顺序放进列表
```python
name = list(info.keys()) #此处info是个字典，将字典中的姓名取出并存入列表name
```
enumerate()可以给集合内的项目编号
```python
lst = ["a", "b", "c"]

for i, v in enumerate(lst, start=1): #for 编号，项目 in enumerate（集合， start=几）
    print(i, v)

```
可得到结果：

1 a

2 b

3 c
## 文件（file）
### 打开文件的标准写法
```python
with open("Name of file", "mode", encoding="utf-8") as f:
  #操作文件
```
mode:

r:只读

w:写入（会覆盖）

a:追加（文件不存在则创建，存在则在末尾加）

+号（r+/w+/a+）：可以同时读和写，最常用的是a+，可以读整个文件，同时在最后增加内容

### 文件读取
文件内容:
```
admin
tom
```
```python
data = f.read #一次读完

for line in f: #一行一行读
  print(line)

lines = f.read().splitlines() #读出来是["admin", "tom"]
```
### 文件写入
```python
with open("文件名.txt", "a", encoding="utf-8") as f:
  f.write(text + "\n")
```
### 文件指针位置
文件在进行读取或写入操作后，如果没有重新打开，指针则会停在刚才最后操作处，注意手动将指针移回文件开头

f.seek(0)
### gpt总结：
```
读文件：      open(file, "r")
覆盖写文件：  open(file, "w")
追加写文件：  open(file, "a")

读所有行：    f.read().splitlines()
写一行：      f.write(text + "\n")

+ 表示：      同时读和写（新手少用）
```
## 字典（dict）
```python
users = {
    "admin": "123456",
    "tom": "abc"
    #key : value
}
```

取值:
```python
users["admin"] # 得到：123456
```

判断有没有这个key：
```python
if "tom" in users:
    print("user exists")
```
新增/修改：
```python
users["alice"] = "pwd123"   # 新增
users["tom"] = "newpwd"     # 修改
#字典名["key"]= "value"
```
遍历字典：
```python
for username in users:
    print(username, users[username])
```
把所有key拿出来：

.keys()
```python
provinces = list(regions.keys())
```
