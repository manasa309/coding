num : int = int(input('enter the number: '))
n = num

if n >= 20: print ('Not Weird')
elif n % 2 == 0 & n in range (2,5): print('Not Weird')
elif n % 2 == 0 & n in range(6,20): print('Weird')
elif n % 2 != 0: print('Weird')

else: print ('ERROR: please input within the conditions')