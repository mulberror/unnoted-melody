---
title: "Vercel Live 模式下遇到的一个加载问题"
subtitle: ""
description: ""
date: 2024-10-27T09:36:11+08:00
lastmod: 2024-10-27T09:36:11+08:00
draft: true

featuredImage: "feature-img.webp"
featuredImagePreview: "feature-img.webp"

# 标签
tags: ["Vercel", "博客"]
# 分类
categories: ["建站"]
# 系列(如果下面这一行注释掉，就不会显示系列为空了)
series: ["小站重生记"]
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
书接上文，在大致完成了博客的重建后，我将博客通过 Vercel 进行了部署。

Vercel 是支持通过 Vercel Live 的模式帮助网站持有者来实时进行一些修改的，并且通过 Vercel 进入到的自己的网站，都默认会进入到该模式中。

## 2 遇见问题

{{<figure src="/img/posts/little-problem-in-vercellive-mode/missing-of-js.webp" title="部分 js 文件未能加载成功" width="100%">}}

如上图所示，左侧加载博客标题的动画和右侧搜索栏的打开都需要加载 js 文件，但是这两个部分都没有进行加载。

这里需要特别感谢我的好室友 [MLAcookie](https://mlacookie.top/)，帮助我一起找到解决方法。

一开始我们觉得这个是 cdn 缓存的问题，但是在 [MLAcookie](https://mlacookie.top/) 和另外一个室友的电脑上用相同的环境进行访问后，发现他们都加载成功了。后来查看了请求到的文件，发现浏览器已经请求到了对应的 js 文件。

{{<figure src="/img/posts/little-problem-in-vercellive-mode/js-loaded-in-local.webp" title="本地已请求到打印动画的 js 文件" width="100%">}}

所以就基本排除是 cdn 缓存的问题，我们将下一个目标锁定在本地加载的过程中出现异常。

## 3 本地调试
