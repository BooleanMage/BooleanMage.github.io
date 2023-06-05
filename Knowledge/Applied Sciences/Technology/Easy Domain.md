---
layout: default
---

# Easy Domain
我就爛架站法

## 目標
* 讓其他人可以看 www.aaaaa.com 
* 可以用 mail@aaaaa.com 可以發信 收信

## 前言(可跳過的廢話)
* 為什麼要用我就爛架站法?
  * 我覺得有個人網址好酷 ex: www.aaaaa.com
  * 我覺得別人的信箱好酷 ex: mail@aaaaa.com
  * 買NAS很貴 一直開著耗電很貴 固定IP很貴 租服務很貴
  * 部落格文章是散亂的，單純照時間先後出現
  * 我想要像wiki或像書本那樣有多層次目錄
* 啊我就不會架站 請別人架要錢
* 啊我就想省錢
* 啊我就不會寫網頁

## 需要的準備工作
1. 註冊gmail信箱，名稱隨意，等等會蓋掉
2. 註冊github帳號，名稱隨意，等等會蓋掉
3. 到Cloudflare註冊一個帳號
4. 在cloudflare買一個網域，名稱重要，等等是用這個
  * 不熱門的域名大概USD$9/year，買一個你開心的網域**<your_domain>**
  * 另一個方式去Godaddy買之後由cloudflare代管，我個人認為太麻煩了

## mail
* 需要讓gmail偽裝自己的mail address
* 需要讓收信送進自己的gamil
* 使用[強者我學長的教學](https://github.com/FlandreDaisuki/gh-as-blog/issues/7)
* 完成之後你的 mail@**<your_domain>** 可以收信和寄信

## 架站，使用github.io
* 註冊一個github帳號**<your_name>**
* 開一個專案名為**<your_name>**.github.io

#### 寫你的第一個頁面
* github.io一律使用README.md
* 參考專案 
  * [posetmage.github.io](https://github.com/posetmage/posetmage.github.io)
  * [QuantumNecro.github.io](https://github.com/QuantumNecro/QuantumNecro.github.io)
* 完成之後，就可以看 https://**<your_name>**.github.io/

#### 改網址
1. GitHub上設定偽裝網址
2. Cloudflare DNS設定CNAME

完成之後你的**<your_domain>** 就可以連到你的**<your_name>**.github.io的頁面

## 結論
Q: 這個網站好醜，為什麼不要請工程師寫好看的頁面?  
A:![](https://i.imgur.com/afA0fr9.png =x300)


---
tags:
  - [[Github]]
  
---