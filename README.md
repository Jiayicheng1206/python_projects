# python_learning_week1
本笔记整理了作者在学习老男孩教育python课程的一些笔记，周数仅代表其录播课程安排，与实际进度不符。

本文档写于2025.12.16

## 基本书写规则
### 单行注释
最前面加#即可，也可以使用快捷键Command + / （下面那个斜线）

### 多行注释
‘’‘

多行文本

’‘’

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
except ValueError:
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