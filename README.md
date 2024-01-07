# 二維Linked List作品說明

作者： 412410025 資工一 楊博勛

## 功能

### NodeList 相關
| 指令 | 參數1 | 參數2 | 說明 | 圖片 |
| --- | --- | --- | --- | ---|
| appendList | name(string) |  | 新增一個名為 name 的 Nodelist 於 NodeList 的最尾端 | 
| deleteList | name(string) |  | 將名為 name 的 Nodelist刪除 |
| nameList | name(string) | newname(string) | 把名為 name 的 Nodelist重新命名為 newname |
| sort | name(string) |  | 將名為 name 的 Nodelist 做排序(由小到大) |
| merge | targetName(string) | dataName(string) | 將 dataName 的資料放到 targetName 後面 |
| reverse | name(string) |  | 將 name  裡面所有的點反轉 |

### 相關照片
appendList

![image](https://cdn.discordapp.com/attachments/1193489674233184256/1193489897844121660/image.png?ex=65ace715&is=659a7215&hm=775ab0e938f209d01885e15a50a9d222851046241dc3b4503e837af7793ececb&)

deleteList

![image](https://cdn.discordapp.com/attachments/1193489674233184256/1193491346317652009/image.png?ex=65ace86e&is=659a736e&hm=4832036ef8cdffd824a351bfb966468592dee143d9d4828a9d0a79419da94a54&)

nameList

![image](https://cdn.discordapp.com/attachments/1193489674233184256/1193493718448226374/image.png?ex=65aceaa4&is=659a75a4&hm=ffd5c82c46ecb42bfbc5a3eaf794aa25705b1576fe4c81a261f3f705e86a571b&)

sort

![image](https://cdn.discordapp.com/attachments/1193489674233184256/1193493718448226374/image.png?ex=65aceaa4&is=659a75a4&hm=ffd5c82c46ecb42bfbc5a3eaf794aa25705b1576fe4c81a261f3f705e86a571b&)

merge

![image](https://cdn.discordapp.com/attachments/1193489674233184256/1193494812687601835/image.png?ex=65aceba9&is=659a76a9&hm=cfd1dbe5a3c307197d054bb0bbf85885b49782485f71c8ba6ac99a53f5a698f1&)

reverse

![image](https://cdn.discordapp.com/attachments/1193489674233184256/1193496429566623784/image.png?ex=65aced2a&is=659a782a&hm=4642ff478cdd2309570545ded3b47f2f986d0e79b7d94576d8bbf67acff05f2e&)

### Node 相關
| 指令 | 參數1 | 參數2 | 參數3 | 說明 |
| --- | --- | --- | --- | --- |
| print | name(string) |  |  | 輸出 name 的全部資料 |
| append | name(string) | data(int) |  | 將 data 加入到 name 的最後面 |
| update | name(string) | target(int) | data(int) | 將 name 中的 target 換成 data |
| insert | name(string) | target(int) | data(int) | 在 name 中的 target 前插入 data |
| delete | name(string) | target(int) |  | 將 name 中的 target 刪除 |

### 相關照片

print

![image](https://cdn.discordapp.com/attachments/1193489674233184256/1193496876067074088/image.png?ex=65aced95&is=659a7895&hm=0f1ae6d10024935763b49f656a7ec4b27b5c9befcba85a1387602ef55bdcec92&)

append

![image](https://cdn.discordapp.com/attachments/1193489674233184256/1193497551048036402/image.png?ex=65acee36&is=659a7936&hm=41807e36760e7a55383de8cb44395f5e2faffffd7468d049eac2c8ab34631068&)

update

![image](https://cdn.discordapp.com/attachments/1193489674233184256/1193545717340459090/image.png?ex=65ad1b12&is=659aa612&hm=60753b1a93050075b79b604d3ea1bc53482a6c47e6b30690c6ef808fd36e8bd6&)

insert

![image](https://cdn.discordapp.com/attachments/1193489674233184256/1193545995007570012/image.png?ex=65ad1b54&is=659aa654&hm=e72b5d3aee68a9990977093f9da7b2e501f59db0672e996bd9473c8384179dfc&)

delete

![image](https://cdn.discordapp.com/attachments/1193489674233184256/1193546223785873488/image.png?ex=65ad1b8a&is=659aa68a&hm=4671884b05bb5062564256115254f86000010734a0929cc1a402764875ac8b82&)

### 額外實作
| 指令 | 參數1 | 參數2 | 說明 | 實作方法 |
| --- | --- | --- |  --- | --- |
| printAll |  |  | 列出整串NodeList 跟所有Node內容 | 從LinkedList的head開始印出，接著找head的next，印出NodeList'name 和 NodeList'head 接下去的整串Node的data 
| search | name(string) | target(int) | 尋找 target 是否存在在 name 當中，並輸出該 target 位於 name 中的第幾個 Node | 找到NodeList(name)後，往其連結Node後搜尋target，找到之後印出該target在該Node的第幾位，ex. Target 3 is located at No. 1 in NodeList name |

### 相關照片

printAll

![image](https://cdn.discordapp.com/attachments/1193489674233184256/1193546531274506290/image.png?ex=65ad1bd4&is=659aa6d4&hm=65563c00dd73d9805d569121ac3584cb9a2b0b334508f53d7f564518e5d45e40&)

search

![image](https://cdn.discordapp.com/attachments/1193489674233184256/1193546735465803786/image.png?ex=65ad1c04&is=659aa704&hm=049997e277ea9405a1bc1f2832a00c568ec6c316967c18be6c8ed71ca8a4cd53&)