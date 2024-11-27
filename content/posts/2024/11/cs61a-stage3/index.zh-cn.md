---
title: "UCB CS61A 课程学习阶段性小结（三）"
subtitle: ""
description: ""
slug: 5a1140
date: 2024-11-24T14:56:29+08:00
lastmod: 2024-11-24T14:56:29+08:00
draft: true

resources:
# 文章特色图片
- name: featured-image
  src: featured-img.webp
# 首页预览特色图片
- name: featured-image-preview
  src: featured-img.webp

# 标签
tags: ['Python', '编程基础', '数据抽象', '搜索']
# 分类
categories: ["学习"]
# 合集(如果下面这一行注释掉，就不会显示系列为空了)
collections: ["CS61A 学习记录"]
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

本篇文章的范围是从 `lab04` 到 `proj 3 ant` 的内容，该部分的内容需要更加对面向对象编程的概念有一定了解。

还有就是关于指针的概念，比如说 `lab05` 和 `hw05` 的内容就是关于指针的。

该部分的项目 `proj 3 ant` 的拓展问题稍微有点问题，我的代码可以通过测试，但是在实际使用的时候会出现卡死的情况。

## 实验 4: 树递归，数据抽象

本次实验内容首先是 Python 中的字典，也就是 C++ 中的 `map`。

Python 中的字典内部是一种数据的映射，将键映射到值，如果是第一次接触到这种数据结构的话，可以看成一个下标类型比较自由的列表。

该实验的第二个问题就是把字典看成列表，使用列表推导的方式生成一个字典。

### 实验 4. 问题 3: 购买水果

本道题目是将字典和递归搜索进行结果，题意需要找到所有购买水果的方案，通过题目需要输出所有的方案就可以看出需要使用搜索。

每一个水果都至少需要买一个，所以假如说当前搜索到了第 i 个水果，就枚举该水果购买多少，然后递归搜索下一个水果。

```python
def buy(fruits_to_buy, prices, total_amount):
    def add(fruits, amount, cart):
        if fruits == [] and amount == 0:
            print(cart)
        elif fruits and amount > 0:
            fruit = fruits[0]
            price = prices[fruit]
            # print('DEBUG', fruit, price)
            for k in range(1, amount // price + 1):
                # Hint: The display function will help you add fruit to the cart.
                add(fruits[1:], amount - k * price, cart + display(fruit, k))
    add(fruits_to_buy, total_amount, '')
```

### 实验 4. 数据抽象

该部分对应教科书中的 [数据抽象](https://composingprograms.netlify.app/2/2) 部分的内容。

教科书上写的有点复杂，根据个人的看法，其实就是把复合数据更加的模块化，每一个部分都被一个独立的程序所控制。

感觉有点像类和调用类中元素的接口的感觉。

比如说 `lab04` 中用一个列表作为一个复合数据表示一个城市的信息，然后每一个城市的信息都需要进行合法性的判断，调用的时候也需要调用一个函数来进行取出。

在其他的编程语言中，例如 C++ 中，这种数据抽象的方式就像类的概念。（Python 非常强调数据抽象，也就是模块化的概念）

## 作业 4: 序列、数据抽象、树

### 作业 4. 问题 2: Deep Map

本道题目需要实现一个函数，该函数可以对一个嵌套的列表进行操作，对于列表中的每一个元素都进行操作。

这里就牵扯到一个关于对于列表的修改，其实在上文也提到过，函数的参数中的列表其实就是原本列表，也是一个指针，在函数内部对列表进行的修改会影响到原本的列表。

如果需要在迭代的过程中**删除**一个元素，`for i in list(s):` 或者 `for i in s[:]` 这样的写法复制了一个列表，在删除元素时不会导致指针错误，这样是比较好的写法。

回到正题，本道题目首先需要对当前列表中的元素进行判断，如果元素依旧为列表，那么就递归处理，否则就对元素进行修改。

```python
def deep_map(f, s):
    for i in range(len(s)):
        if type(s[i]) == list:
            deep_map(f, s[i])
        else:
            s[i] = f(s[i])
```

### 作业 4. 问题 4: 平衡

本题目是练习数据抽象相关的内容，平衡就是要求每一个中点的两端的**力矩**相等。

所以对于每一个中间的支点首先需要判断是否为叶子，如果不是就要判断两端返回的**重量和距离的乘积**是否相同。

```python
def balanced(m):
    if is_planet(m):
        return True
    else:
        return balanced(end(left(m))) and 
               balanced(end(right(m))) and 
               total_mass(end(left(m))) * length(left(m)) == total_mass(end(right(m))) * length(right(m))
```

## 实验 8: Mutable Trees

实验 8 的内容比较简单，目的就是熟悉一下树的结构。

### 实验 8. 问题 5: Maximum Path Sum

这个问题是求树中从根节点到叶子节点的最大路径和。

函数返回子树中的最大路径和。

假设要求解以 $r$ 为根的最大路径，该路径就是 $r$ 子树中最大的路径再加上 $r$ 上标签上的值。

```python
def max_path_sum(t):
    """Return the maximum path sum of the tree.

    >>> t = Tree(1, [Tree(5, [Tree(1), Tree(3)]), Tree(10)])
    >>> max_path_sum(t)
    11
    """
    "*** YOUR CODE HERE ***"
    if t.is_leaf():
        return t.label
    else:
        max_path = 0
        for b in t.branches:
            max_path = max(max_path, max_path_sum(b))
        return t.label + max_path
```