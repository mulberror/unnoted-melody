---
title: "小站重生记 | 用 hugo + vercel + cloudflare 重建博客"
subtitle: ""
description: ""
date: 2024-10-24T00:51:43+08:00
lastmod: 2024-10-24T00:51:43+08:00
draft: false

resources:
- name: "featured-image"
  src: "featured-image.webp"

# 标签
tags: []
# 分类
categories: [""]
# 系列
series: []
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

comment:
  utterances:
    enable: true
  waline:
    enable: false
  disqus:
    enable: false
---
## 1 前言
我之前也是用 hugo 框架搭建的博客，使用的主题是 PaperMod。

不过因为大部分存货都丢失了，再加上碰巧见看到了 [ryan4yin](https://thiscute.world/) 大佬的博客，从而了解到了 [HEIGE-PCloud](https://pcloud.dev/) 大佬制作的 [DoIt](https://github.com/HEIGE-PCloud/DoIt) 主题。

DoIt 主题非常符合我一开始预想的博客样式，所以就直接花了一段时间进行了个人博客的重建，并且在这个期间还花了一点时间从零学了点前端知识，简单地写了一个简陋的个人主页 [My Little World](https://www.mulbx.top/)。

## 2 hugo + gitpage 阶段