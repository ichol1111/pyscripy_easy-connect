#!/usr/bin/python

import os
import time
import win32gui
import win32api
import win32con
from pymouse import *
from pykeyboard import PyKeyboard
from ctypes import *

#打开应用程序
os.system('start "" /d "D:\Sangfor\SSL\SangforCSClient" "SangforCSClient.exe"')

time.sleep(3)

a = win32gui.FindWindow(None, "EasyConnect")
loginid = win32gui.GetWindowPlacement(a)

# 定义一个键盘对象
k = PyKeyboard()

# 输入用户名
k.type_string("123")
# # 按下回车
win32api.keybd_event(13, 0, 0, 0)
win32api.keybd_event(13, 0, win32con.KEYEVENTF_KEYUP, 0)
time.sleep(3)

#输入用户名
k.type_string("123")
# # 按下tab，切换到输入密码的地方
k.tap_key(k.tab_key)
# 输入密码
k.type_string("123")

# # 按下回车
win32api.keybd_event(13, 0, 0, 0)
win32api.keybd_event(13, 0, win32con.KEYEVENTF_KEYUP, 0)

