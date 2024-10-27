---
title: "{{ replace .TranslationBaseName "-" " " | title }}"
subtitle: ""
description: ""
date: {{ .Date }}
lastmod: {{ .Date }}
draft: true

# 文章特色图片
featuredImage: "feature-img"
# 首页预览特色图片
featuredImagePreview: "feature-img"

# 标签
tags: []
# 分类
categories: [""]
# 系列(如果下面这一行注释掉，就不会显示系列为空了)
# series: []
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