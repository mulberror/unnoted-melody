---
title: "服务器部署 Flask 项目"
subtitle: ""
description: ""
slug: ec18fe
date: 2024-12-25T17:38:05+08:00
lastmod: 2024-12-25T17:38:05+08:00
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
  jas
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

由于本学期的创新实践课程要求，我和同学合作开发了一个简易的基于 gemini 的电影 GPT 系统。

项目的后端是基于 Python Flask 框架开发的，前端是基于 Vue.js 开发的。

## 配置信息

- 服务器：华为云 ECS（CentOS），我合作的同学已经安装了宝塔面板。
- 项目：Flask 项目
- Python 版本：3.10
- 项目地址：[movie-gpt](https://github.com/mulberror/movie-gpt)

## Flask 项目部署

### 本地生成依赖文件

```bash
pip freeze > requirements.txt # 生成依赖文件
```

