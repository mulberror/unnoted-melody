---
title: "{{ replace .TranslationBaseName "-" " " | title }}"
subtitle: ""
description: ""
date: {{ .Date }}
lastmod: {{ .Date }}
draft: true

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