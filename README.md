# AlipayAR

# How to Use

#### 1、restore one picture
🌰  python alipayar.py input/IMG_1838.PNG   
🌰  python alipayar.py png
#### 2、restore a lot of pictures
🌰  python alipayar.py input/ output/

# Requirement
Python Imaging Library(PIL)

# Attention

maybe you should to add some paramether to suit your screenshot

🌰 📱iPhone6
```
[system]
phone=iphone6
```

🌰 📱honor6
```
[system]
phone=honor6
```

```
[honor6]
# 不同机型对应不同的width*height
left=220
top=618
width=280
height=280
# 高度偏移值
margin=7,4
# 黑线宽度
blanLineHeight=6
# 黑线数量 固定值一般不需要改动
blanLineSize=27

[iphone6]
# 不同机型对应不同的width*height
left=205
top=638
width=340
height=340
# 高度偏移值
margin=10,5
# 黑线宽度
blanLineHeight=7
# 黑线数量 固定值一般不需要改动
blanLineSize=27
```

![](https://ww4.sinaimg.cn/large/006tNc79jw1fb1zhrbookj30ja0y2dke.jpg)

# More 

[玩玩支付宝AR红包](https://blog.fangjie.info/2016/12/23/%E7%8E%A9%E7%8E%A9%E6%94%AF%E4%BB%98%E5%AE%9DAR%E7%BA%A2%E5%8C%85/)

