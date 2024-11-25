---
title: "Stanford CS106L 课程笔记"
subtitle: ""
description: ""
slug: 406d2a
date: 2024-11-21T14:36:42+08:00
lastmod: 2024-11-21T14:36:42+08:00
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

## 前言

本篇文章主要记录我在学习 Stanford CS106L: Standard C++ Programming 课程时的过程和作业。

该课程的内容貌似每一年都有一定程度的变动，且课程作业在 2024 年左右进行一次大改动，所以同时记录了 2022 年版本和 2024 年版本中的内容。

<!--more-->

## 环境配置

- 操作系统: macOS
- 编辑器: Clion（不过使用 Clion 出现了一些补全、缩进的问题）

首先需要进行 `pkg-config` 的安装，不然 `vcpkg` 会报错。

![alt text](/img/image.png)

```bash
brew install pkg-config
```

然后从课程的 github 仓库中下载代码即可，并运行内部的 `setup.sh` 脚本即可。

详细资料可以见 csdiy 的 [cs106l 课程](https://csdiy.wiki/%E7%BC%96%E7%A8%8B%E5%85%A5%E9%97%A8/cpp/CS106L/#_2)

## 2022 版

### 作业 1
