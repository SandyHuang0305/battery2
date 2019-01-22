phone = input('手機型號？')
battery = int(input('目前電量多少？'))
if phone == 'samsung note 7' and battery < 10:
	print('注意安全')
elif phone != 'samsung note 7' and battery <10:
	print('不是note7就好,記得充電喔')
elif not phone == 'samsung note 7' or battery > 90:
	print('可以繼續使用')
else:
	print('我也不知道發生甚麼事')			