import random
a = int(input('輸入範圍最小值:'))
b = int(input('輸入範圍最大值:'))
r = random.randint(a, b)
count = 0
while True:
	count += 1
	num = int(input('猜數字:\n'))
	if num == r:
		print('你猜對了')
		print('你猜了', count, '次')
		break
	else :
		if num > r:
			print('太大了')
		else :
			print('太小了')
	print('你猜了', count, '次')
		