---
title: "Leetcode 1977: 划分数字的方案数"
subtitle: ""
description: ""
slug: 2c5482
date: 2025-02-24T18:57:27+08:00
lastmod: 2025-02-24T18:57:27+08:00
draft: false

resources:
# 文章特色图片
- name: featured-image
  src: featured-img.webp
# 首页预览特色图片
- name: featured-image-preview
  src: featured-img.webp

# 标签
tags: ['动态规划', 'Leetcode', '字符串', '算法', '复试']
# 分类
categories: ["算法"]
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

这是 2024 年科软机试的最后一题，虽然前 3 题比较简单，但是个人感觉对于 1h 的上机考试来说这就是一道防 AK 题，在复试机试考场上可能只有那些有算法竞赛基础的同学才能做出来。

题目考查的主要就是动态规划，不失为一道动态规划从入门到进阶的好题。

<!--more-->

题目描述比较简短，这里就不赘述题意了。

题目链接：[Leetcode](https://leetcode.cn/problems/number-of-ways-to-separate-numbers/description/)

## 解题思路

### 设计状态

对于这个计数类问题一般来说都是采用 DP 的方式进行求解的，而且很常见的一种设计状态的方式就是令其中一维 $i$ 表示当前选择数字的最后一位是字符串的第 $i$ 个字符。

该题目中还有一个限制条件就是需要对数字的大小进行比较，令分割出来的结果**不递减**，那么显然一维的状态无法表示所有的信息，可以考虑设置第二维 $j$ 表示最后一个字符串的长度为 $j$。

这样状态就设计成 $f[i][j]$ 表示最后一个数字的末尾为字符串第 $i$ 位，并且长度为 $j$ 的总方案数，这样设计状态的方式就隐含了另外一个信息就是前一个数字的最后一位为字符串的第 $i-j$ 位。

### 考虑非递减的约束条件

考虑状态转移方程，也就是如何递推求解 $f[i][j]$，考虑到题目中的约束条件为分割出来的序列不递减，所以我们就需要保证**当前最后一个数字（以 $i$ 结尾的数字）**要大于等于**前一个数字（以 $i-j$ 结尾的数字）**。

在大数字的比较（高精度数字比较）中，数字之间的大小首先比较位数（长度），所以如果前一个数字的位数 $k$ 满足 $k<j$，则前一个数字**一定小于**当前数字，对应所有的 $f[i-j][k]$ 对 $f[i][j]$ 都有贡献。

$$
f[i][j]=\sum_{k<j}f[i-j][k]
$$

对于这个求和，由于数据范围 $n\leq 3500$，所以并不能直接枚举 $k$，但是可以使用前缀和优化成 $O(1)$ 的复杂度。

同理在长度 $k>j$ 的情况下，一定不满足条件，对 $f[i][j]$ 不产生贡献。

### 解决长度相同的比较问题

剩余的情况就是 $k=j$ 的情况，也可以联想到大数的比较中的过程，需要找到两个数字**从开头第一个不相同的数字**，然后比较该数字的大小。

和上面求和中不能直接枚举 $k$ 的理由相同，这边**不能直接使用 `std::string` 中的函数或者循环比较的方式来判断数字的大小**，需要直接定位到该**第一个不同数字的位置**。

让我们重新审视一下该问题，现在的问题就是在一个字符串当中我们需要比较两个长度相同（长度为 $j=k$）的子串对应的数字大小（区间分别为 $[i-j*2+1, i-j]$ 和 $[i-j+1, i]$），该问题被转换成了找到这两个区间从头开始比较，**第一个不相同的数字**的位置在哪里。

对于该问题也可以转换成**计算两个区间的相同前缀的最大长度**，定义状态 $h[i][j]$ 表示两个区间开头分别为 $i$ 和 $j$（$i<j$），转移就是考虑第 $i$ 个字符和第 $j$ 个字符是否相同，将这两个字符去掉后对应的两个区间的开头为 $i+1,j+1$，如果相同就可以拼上来，否则就长度为 $0$。（可以用最长公共子串的 DP 思路进行类比理解）

$$
h[i][j]=h[i+1][j+1]+1 \ (\[s[i]=s[j]\])
$$

```cpp
std::vector h(n + 1, std::vector<int>(n + 1, 0));
for (int i = n - 1; i >= 0; i--) {
  for (int j = n - 1; j > i; j--) {
    if (num[i] == num[j]) {
      h[i][j] = h[i + 1][j + 1] + 1;
    }
  }
}
```

该预处理的时间复杂度为 $O(n^2)$，预处理好就可用于找到两个区间的第一个不相同的字符了。

1. 两个区间（以 $i-j*2+1$ 开头以及以 $i-j+1$）对应的最长长度如果大于等于 $j$（也就是两段区间完全相同），那么 $f[i-j][j]$ 对 $f[i][j]$ 就有贡献（因为两段对应的数字完全相同。
2. 否则我们就比较从两个区间开头的第 $h[i-j*2+1][i-j+1]+1$ 这个字符大小，如果后面的区间对应的字符大于等于前一个区间的字符，那就有贡献。


## 代码

仅供参考

```cpp
class Solution {
  constexpr static int P = 1e9 + 7;
public:
  int numberOfCombinations(std::string num) {
    int n = num.size();
    std::vector h(n + 1, std::vector<int>(n + 1, 0));
    for (int i = n - 1; i >= 0; i--) {
      for (int j = n - 1; j > i; j--) {
        if (num[i] == num[j]) {
          h[i][j] = h[i + 1][j + 1] + 1;
        }
      }
    }
    std::vector f(n + 1, std::vector<int>(n + 1, 0));
    std::vector g(n + 1, std::vector<int>(n + 1, 0));
    if (num[0] == '0') {
      return 0;
    }
    for (int i = 0; i < n; i++) {
      f[i][i + 1] = 1;
      for (int j = 1; j <= i; j++) {
        if (num[i - j + 1] == '0') {
          continue;
        }
        f[i][j] = (f[i][j] + g[i - j][j - 1]) % P;
        if (i - j * 2 + 1 >= 0) {
          auto check = [&](int i, int j, int k) -> bool {
            if (h[i][j] >= k) {
              return true;
            }
            return num[i + h[i][j]] <= num[j + h[i][j]];
          };
          if (check(i - j * 2 + 1, i - j + 1, j)) {
            f[i][j] = (f[i][j] + f[i - j][j]) % P;
          }
        }
      }
      for (int j = 1; j <= n; j++) {
        g[i][j] = (g[i][j - 1] + f[i][j]) % P;
      }
    }
    return g[n - 1][n];
  }
};
```