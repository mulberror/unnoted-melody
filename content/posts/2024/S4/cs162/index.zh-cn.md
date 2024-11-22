---
title: "Cs162"
subtitle: ""
description: ""
slug: 57518e
date: 2024-11-22T09:55:43+08:00
lastmod: 2024-11-22T09:55:43+08:00
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

## 环境搭建

m1 芯片上出现的 Unimplemeted syscall number 282 问题

进入到 Docker 的设置界面，取消勾选 "Use Rosetta for x86/amd64 emulation on Apple Silicon"，然后重启 Docker。
