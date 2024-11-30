---
title: "Cs61a Stage5"
subtitle: ""
description: ""
slug: f38a77
date: 2024-11-30T23:53:36+08:00
lastmod: 2024-11-30T23:53:36+08:00
draft: true

resources:
# 文章特色图片
- name: featured-image
  src: featured-img.webp
# 首页预览特色图片
- name: featured-image-preview
  src: featured-img.webp

# 标签
tags: []
# 分类
categories: [""]
# 合集(如果下面这一行注释掉，就不会显示系列为空了)
# collections: [""]
# 从主页面中去除
hiddenFromHomePage: false
# 从搜索中去除
hiddenFromSearch: false

lightgallery: false

# 否开启表格排序
table:
  sort: false
toc:
  enable: true
  auto: true
expirationReminder:
  enable: false
  # ...
code:
  copy: true
  # ...
edit:
  enable: false
  # ...
math:
  enable: true
  # ...
mapbox:
  accessToken: ""
  # ...
share:
  enable: true
  # ...
comment:
  enable: true
  # ...
library:
  css:
    # someCSS = "some.css"
    # 位于 "assets/"
    # 或者
    # someCSS = "https://cdn.example.com/some.css"
  js:
    # someJS = "some.js"
    # 位于 "assets/"
    # 或者
    # someJS = "https://cdn.example.com/some.js"
seo:
  images: []
  # ...
---


## 函数式编程 Scheme

特点是只使用表达式而不使用语句，特别适合符号计算，并且它处理的数据都是不可变的。

| **特点** | **函数式编程** | **解释型语言** | **编译型语言** |
| --- | --- | --- | --- |
| **核心定义** | 编程范式，基于函数计算模型 | 执行时逐行翻译并执行 | 先编译为机器码后运行 |
| **是否互斥** | 不是语言特性，与实现方式无关 | 是语言特性，与范式无关 | 是语言特性，与范式无关 |
| **常见结合** | 解释型语言和编译型语言均可支持 | 可用于支持函数式编程的语言 | 可用于支持函数式编程的语言 |

### Scheme

表达式一般采用**前缀**的形式进行表示，即运算符在运算数的前面。

这个编程语言十分严格，不过这个严格和 Python 对格式的要求以及 Rust 对类型的要求不同，Scheme 对嵌套也就是括号（作用域）的要求非常高。

就以 实验 9 的问题 3 为例，以下两份代码的效果就完全不同，主要得益于该语言的调用方式，对这个括号的要求非常高。

```scheme
(define (composed f g) 
  (lambda (x) (f (g x)))
)
(define (composed f g) 
  (lambda (x) (f (g(x))))
)
```

这边稍微记录几个比较常用的但是教材文档中没有出现的函数，该部分还是课程给定的文档比较全。

Scheme 语言处理取模数操作：

- **`remainder`**
    
    返回两个数相除的余数，余数的符号与被除数相同。
    
    ```scheme
    (remainder 5 3)  ; 返回 2
    (remainder -5 3) ; 返回 -2
    ```
    
- **`modulo`**
    
    返回两个数相除的余数，余数的符号与除数相同。
    
    ```scheme
    (modulo 5 3)    ; 返回 2
    (modulo -5 3)   ; 返回 1
    ```
    
- **`quotient`**
    
    它返回两个数相除后的整数部分（即商的整数部分）
    

Scheme 中的 **`pair` :**

```scheme
scm> (define x (cons 1 2))
x
scm> (car x)
1
scm> (cdr x)
2
```

## 作业 8: **Scheme List**

由于 Scheme 语言中的 List 并不是非常的智能，所以只能用学习链表的方式来学习该部分。

每一个 List 都由两个部分组成，分别是 `car` 和 `cdr` 组成，分别对应了一般链表中的 `data` 和 `next` 指针，每一个 `cdr` 仍旧是一个 List，介于 Scheme 中的循环比较难以实现，所以还是需要使用递归进行链表的递归和操作。

所以以下的所有程序，均采用链表的方式进行思考。

本节作业需要借助一些工具，比如作业主页中的 [Scheme基本文档](https://cs61a.org/articles/scheme-spec/) 或者一个 ChatGPT，这样比较好进行学习。

### 作业 8. 问题 1: 检测升序

检测升序就需要进行相邻的两个元素的大小关系比较，也就是比较 `(car s)` 和 `(car (cdr s))` 这两个元素的大小。

```scheme
(define (ascending? s) (
  if (or (null? s) (null? (cdr s)))
    #t
  (if (<= (car s) (car (cdr s)))
    (ascending? (cdr s))
    #f
  )
))
```

### 作业 8. 问题 2: 过滤器

看成链表的话，依旧是每次判断 `(car s)` 是否满足 `pred` 函数的要求，该函数是一个返回 `#t` (true) 或者 `#f` (false) 的判断函数。

如果满足条件那么就和后面递归得到的结果连成一个链表；否则就直接返回后面的结果。

```scheme
(define (my-filter pred s) 
  (cond ((null? s) '())
        ((pred (car s)) (cons (car s) (my-filter pred (cdr s))))
        (else (my-filter pred (cdr s)))
  )
) 
```

以上所使用的 `cond` 关键词可以理解成 C++ 中的 `case` ，后面跟的每一个括号中都是一个 `(条件) (语句)` ，最后都不满足就进入 `else` 中的语句。

### 作业 8. 问题 3: 交叉合并

有问题 1 和问题 2 的铺垫，问题 3 就比较简单了，这边不再赘述了。

```scheme
(define (interleave lst1 lst2) 
  (cond ((null? lst1) lst2)
        ((null? lst2) lst1)
        (else (cons (car lst1) (cons (car lst2) (interleave (cdr lst1) (cdr lst2)))))
  )
)
```

### 作业 8. 问题 4: 列表去重

题目给了一个提示，就是使用上面编写的 `my-filter` 函数，就是希望学生使用 Lambda 表达式实现一个上述的 `pred` 函数。

每次遇到一个列表首先保留其最开头的元素 `(car s)` 然后使用 `my-filter` 函数保留不同于`(car s)` 的元素，这个结果当作一个列表进行递归。

有关 Lambda 函数的书写方式

```scheme
(define (no-repeats s) 
  (if (null? s) 
    ()
    (cons (car s) (no-repeats (my-filter (lambda(x) (not (= x (car s)))) (cdr s))))
  )
)
```

## 实验 10: 解释器

使用 Python 写一个 Scheme 语言的解释器。

简单的来讲，就是通过 Python 生成能够让 Scheme 语言编译的语句。

一开始做该部分的实验个人感觉会理解起来稍微有一点困难，但是万幸的是 CS61A 该部分的引导问题写的非常好，而且对于 Scheme 语言的前缀表达性，该实验还是比较能感受到其意义的。

第三个问题需要注意 0 在 Scheme 语言中是 #t，只有 #f 才是 False。

个人觉得本实验的还是非常考验抽象思考的能力的，首先 Scheme 这种函数式编程的方式就对抽象能力有一定的要求，再加上现在通过 Python 这样一个中间解释器来完成 Scheme 的解释，（个人感觉虽然完成了该部分的实验，但写的代码不是特别的优美）

特别是该实验的最后一个问题，需要将声明的对象和值绑定起来，其中就包括了把对象和函数这种抽象绑定起来的过程，该部分的代码的逻辑较为复杂，不过针对 doctest 调试过去还是比较简单的。

## 项目 4: Scheme

首先说一下，本项目是本学期中四个 proj 中最难的，非常考验抽象能力，不过也不用特别的害怕，在写的过程中可以慢慢对整个项目有逐渐清晰的认知。

调用语句和一些特殊形式的语句最终会转变成 Pair 类型。

- Q: What exception should be raised for the expression (1)?
    
    Choose the number of the correct choice:
    
    1. SchemeError("malformed list: (1)")
    2. SchemeError("1 is not callable")
    3. SchemeError("unknown identifier: 1")
    4. AssertionError
    
    在 Scheme 语言中，单独这样一个数字其实是可以的，但是在项目中编写的解释器会让这个归类到一个调用运算中，所以这道题目是选择 1。
    

这个 `scheme_eval` 需要调用 `scheme_apply` 进行运算，简单可以理解成 `eval` 这个函数将 scheme 语句切分成若干个参数，然后给 `apply` 这个运算。

### 问题 1: 构建一个存储环境的数据结构 Frame

可以仔细阅读以下项目的文档对应的内容，首先 Scheme 中也是有作用域这么一个概念的，这个是通过括号进行区分的。

所以我们这个 Frame 结构体也是在完成这么一个问题，如果在当前这个作用域（项目中还称之为 `env` 环境）找不到对应的元素，那么就需要到上一层去寻找 `lookup`，如果找到了全局 `env` 也没找到，那么就需要抛出一个 `SchemeError` 错误。

### 问题 2: 内置的执行函数

首先，我在第一次写这个问题前并没有读懂，只是按照文档中的顺序将所有的代码完成了，现在回来一看还是非常有收获的。

以下面的 Procedure 执行函数为例，这是一类内置的运行过程函数，`py_func` 是一个运算函数，这个函数的传入参数个数是并**不确定的**，然后后面这个 `need_env` 是一个标志该函数是否需要参考当前的外部环境 `env` ，这个外部环境在这里作为最后一个参数传入到 `py_func` 函数中。

```python
class BuiltinProcedure(Procedure):
    """A Scheme procedure defined as a Python function."""
    def __init__(self, py_func, need_env=False, name='builtin'):
        self.name = name
        self.py_func = py_func
        self.need_env = need_env

    def __str__(self):
        return '#[{0}]'.format(self.name)
```

该部分的实验文档中给出了如何编写该部分的代码：

- 将 Scheme 列表转变成 Python 列表：像链表一样将 `args` 中的内容给遍历完后放在一个列表中。
- If `procedure.need_env` is `True`, then add the current environment `env` as the last argument to this Python list. 这里就是上文所说的如果需要外部环境，那么就把这个放在上面这个参数列表的最后。
- 然后调用这个 `py_func` 函数，需要注意异常处理。返回对所有这些参数调用 `procedure.py_func` 的结果。**由于不知道参数的确切数量，请使用 `*args` 表示法： `f（1， 2， 3）` 等效于 `f（*[1， 2， 3]`）。**

该部分的总结是一边写项目一边写的，所以到这一步前面的一些疑惑感觉就得到了解决。（一定要在每一道题目之前把对应的 `-u` 问题给回答了，非常有助于理解）

### 问题 3: 调用内置执行函数进行运算

根据项目的文档，需要先把传入的参数的第一个符号 `operator` 转换成对应的 `Procedure` ，转换后才能调用问题 2 中完成的程序进行运算。

需要注意一点这个 `operator` 也有可能是一个运算后得到的结果，递归调用 `scheme_eval` 函数就可以将符号转换成对应的过程对象，转换后可以通过 `scheme_utils.py` 中的函数进行检验是否是 `Procedure` 对象。

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/944c3f74-fe35-4956-9820-c6a974769279/716e0f7c-262c-4453-ba76-c5097b6ef96f/image.png)

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/944c3f74-fe35-4956-9820-c6a974769279/3e4101b8-8ca1-4bc6-b02b-eb6ac8494fed/image.png)

然后就是将需要运算的参数都处理出来，这个结果也有可能有嵌套，所以该部分也需要递归调用 `scheme_eval` 函数进行运算，根据文档中的提示，可以调用 `Pair` 的 `map` 函数将里面所有的元素运算一遍。

```python
# BEGIN PROBLEM 3
"*** YOUR CODE HERE ***"
procedure = scheme_eval(first, env)
scheme_params = rest.map(lambda x: scheme_eval(x, env))
return scheme_apply(procedure, scheme_params, env)
# END PROBLEM 3
```

如果可以独立完成独立以上的两个问题，那么接下来的第四个问题应该比较简单了。

### 问题 8: make_child_frame

问题 7 是比较好解决的，其问题的本质就是将 lambda 函数这个函数的形式给创建出来了。

所以在上一个问题的最后项目文档中写了，可以将该函数的形式输出出来，但是并不能真正的调用该函数。因为通过前面所有问题的铺垫，可以知道一个执行的过程必须要有执行的对象和执行的环境，该问题 8 其实就是在创建一个执行过程的执行 `Frame` 执行环境 `env` 。

lambda 表达式相当于创建了一个新的作用域，该作用域其实是作为调用该 lambda 表达式的子节点。

个人感觉这个函数其实是一个静态函数，在 C++ 中应该用 `static` 关键词修饰一下，首先需要创建一个环境给新的作用域，这个作用域的父亲节点是当前的作用域，然后需要把对应的形式参数和实际参数给绑定起来，最后这个新的作用域才是真正的作用域。

```python
def make_child_frame(self, formals, vals):
    if len(formals) != len(vals):
        raise SchemeError('Incorrect number of arguments to function call')
    # BEGIN PROBLEM 8
    "*** YOUR CODE HERE ***"
    new_frame = Frame(self)
    while formals is not nil:
        new_frame.define(formals.first, vals.first)
        formals = formals.rest
        vals = vals.rest
    return new_frame
    # END PROBLEM 8
```

### 问题 9: lambda

问题 7 和问题 8 都把前面的铺垫做好了，现在需要的就是执行过程并返回结果了。

该部分最好就是跟着项目文档中所说来做，创建一个新的 `Frame` ，这个 `Frame` 的父亲环境是 `procedure` 外面的运行环境，然后在这个环境下调用问题 8 写的绑定。~~感觉这里是不是多了一层，虽然并不影响结果，中间那一层是空的因为有 lookup~~

然后在执行，这段部分的逻辑可以自己理一下。

```python
elif isinstance(procedure, LambdaProcedure):
    new_frame = Frame(procedure.env)
    new_frame = new_frame.make_child_frame(procedure.formals, args)
    # print('DEBUG: new_frame =', new_frame)
    # print('DEBUG: env =', env)
    return eval_all(procedure.body, new_frame)
```

后面的问题 11 也有相关提示，其实就是修改一下作用域，代码如文档中所说非常相似。