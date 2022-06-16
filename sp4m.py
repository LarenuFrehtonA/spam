import pyautogui
import time

message = input("message? : ")
str = input("How many times ?: ")

print("sp4m")

count = 5
while(count != 0):
	print(count)
	time.sleep(1)
	count -= 1

print("sending..!")

for i in range(0,int(str)):
	pyautogui.typewrite(message + '\n')
