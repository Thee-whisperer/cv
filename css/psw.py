 if(passcheck!=passw):
	for i in range(3):
		 print('retry!!\n')
		 i=i-1
		 passcheck=input(print('enter password\t'))
	     if(passcheck==passw):
			break
		 else:
			continue
else:
	print('welcome')