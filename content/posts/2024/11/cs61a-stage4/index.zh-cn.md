---
title: "Cs61a Stage 4"
subtitle: ""
description: ""
slug: f5c5a0
date: 2024-11-27T15:55:10+08:00
lastmod: 2024-11-27T15:55:10+08:00
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
