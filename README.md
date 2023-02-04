# 原神登龙斩助手

为迪卢克定制。

## 环境
1. Windows PC(推荐)
2. Python 3.8
```
pynput==1.7.6
PySide6==6.4.2
```

## 使用
1. 管理员身份启动
2. F键对应普攻登龙
3. R键对应一段登龙
4. T键对应二段登龙
5. V键对应三段登龙
6. Alt键可在游戏中屏蔽(启用)登龙功能
   
## 配置
### 移速buff
```
[General]
A=352
E1=431
E2=471
E3=658
SH=24
IS_DENGING=0
IS_BLOCK=0
```
### 无移速buff
暂无,对帧数要求太高了。成功率很低。

### Nuitka 打包
```
python -m nuitka --onefile --windows-disable-console --enable-plugin=pyside6 --windows-icon-from-ico=favicon.ico --windows-uac-admin -o DengLong/DengLong.exe --output-dir=DengLong --remove-output main.py
```

### 其它
[logo](https://www.logosc.cn/logo/favicon?s=%E7%99%BB%E9%BE%99)




