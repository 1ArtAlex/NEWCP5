print ("введите площадь зала")
try: 
	S=int(input())
except ValueError:
	print ("введены некоректные данные")
	exit()
else:
	print ("введите радиус сцены")
try: 
	R=int(input())
except ValueError:
	print ("введены некоректные данные")
	exit()
else:
	print ("введите расстояние от стены зала до сцены")
try: 
	K=int(input())
except ValueError:
	print ("введены некоректные данные")
	exit()
else:
	if S>=(2*K+2*R)**2:
		print ("сцену вписать можно")
	else:
		print ("сцену вписать нельзя")
