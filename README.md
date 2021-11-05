# Secure-Code-Creator
一个基于安全文件MD5值的强密码生成器

Copyright (c) 2020 Steve D. J..All rights reserved.

使用方法：下载Release版本压缩包，解压后运行SecureCodeCreator.exe，按照程序内文字指引操作即可。

设计思想：
使用强密码且不将密码直接存储于本地或云端，降低密码被窃取的风险。

基本流程：
  1.生成一个随机内容的txt文件作为安全文件；
  2.计算该文件的MD5值；
  3.用户使用此文件作为账号密码；
  4.登陆时只需将安全文件拖入程序窗口即可获得密码。
  
