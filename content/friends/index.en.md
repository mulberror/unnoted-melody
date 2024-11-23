---
title: "Friend Links"
date: 2024-10-28T00:24:31+08:00
draft: false
hiddenfromsearch: true

comment:
  utterances:
    enable: true
  waline:
    enable: false
---

<div class="linkpage"><ul id="friendsList"></ul></div>

<script type="text/javascript">
var myFriends = [
    ["https://www.cnpatrickstar.com/", "https://www.cnpatrickstar.com/images/avatar.jpg", "Patrick Star - 学长", "派大星的石头屋"], 
    ["https://www.f1nley.xyz/", "https://avatars.githubusercontent.com/u/32237950?v=4", "Finley Ge - 学长", "Keep learning, coding, thinking."], 
    ["https://gggaaalleeee.top/", "https://gggaaalleeee.top/image/avatar.jpg", "gggaaallleee - 学长", "阳和启蛰，天雨流芳。"], 
    ["https://www.lonesome.cn/", "https://www.lonesome.cn/assets/avatar.png", "Ximo - 同学", "惜寞的无人小间"], 
    ["https://blog.bluebird.icu/", "https://blog.bluebird.icu/config/head.jpg", "青鸟 - 同学", "青鸟のBlog"], 
    ["https://ljw030710.github.io/", "https://avatars.githubusercontent.com/u/115199222?v=4", "iolzyy - 同学", "人生如一片静水，唯有内心澄澈，方能映照出真正的天地。"],
    ["https://blog.liip.fun/", "https://blog.liip.fun/avatar.jpg", "离谱 - 学弟", "离谱的blog"],
];

// 以下为核心功能内容，修改前请确保理解您的行为内容与可能造成的结果
var  targetList = document.getElementById("friendsList");
while (myFriends.length > 0) {
    var rndNum = 0;
    var friendNode = document.createElement("li");
    var friend_link = document.createElement("a"), 
        friend_img = document.createElement("img"), 
        friend_name = document.createElement("h4"), 
        friend_about = document.createElement("p")
    ;
    friend_link.target = "_blank";
    friend_link.href = myFriends[rndNum][0];
    friend_img.src=myFriends[rndNum][1];
    friend_name.innerText = myFriends[rndNum][2];
    friend_about.innerText = myFriends[rndNum][3];
    friend_link.appendChild(friend_img);
    friend_link.appendChild(friend_name);
    friend_link.appendChild(friend_about);
    friendNode.appendChild(friend_link);
    targetList.appendChild(friendNode);
    myFriends.splice(rndNum, 1);
}
</script>

<style>

.linkpage ul {
    color: rgba(255,255,255,.15)
}

.linkpage ul:after {
    content: " ";
    clear: both;
    display: block
}

.linkpage li {
    float: left;
    width: 48%;
    position: relative;
    -webkit-transition: .3s ease-out;
    transition: .3s ease-out;
    border-radius: 5px;
    line-height: 1.3;
    height: 90px;
    display: block
}

[data-theme='dark'] .linkpage h4 {
    color: #dddddd;
}

.linkpage h3 {
    margin: 15px -25px;
    padding: 0 25px;
    border-left: 5px solid #51aded;
    background-color: #f7f7f7;
    font-size: 25px;
    line-height: 40px
}

.linkpage li:hover {
    background: rgba(230,244,250,.5);
    cursor: pointer
}

.linkpage li a {
    padding: 0 10px 0 90px
}

.linkpage li a img {
    width: 60px;
    height: 60px;
    border-radius: 50%;
    position: absolute;
    top: 15px;
    left: 15px;
    cursor: pointer;
    margin: auto;
    border: none
}

.linkpage li a h4 {
    color: #333;
    font-size: 18px;
    margin: 0 0 7px;
    padding-left: 90px
}

.linkpage li a h4:hover {
    color: #51aded
}

.linkpage li a h4, .linkpage li a p {
    cursor: pointer;
    white-space: nowrap;
    text-overflow: ellipsis;
    overflow: hidden;
    line-height: 1.4;
    margin: 0 !important;
}

.linkpage li a p {
    font-size: 12px;
    color: #999;
    padding-left: 90px
}

@media(max-width: 460px) {
    .linkpage li {
        width:97%
    }

    .linkpage ul {
        padding-left: 5px
    }
}

</style>