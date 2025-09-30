#CONCATINATION
first_name = 'Manasa'
last_name = 'Naik'
full_name = first_name +" "+ last_name

print(full_name)

#REPETATION
greetings = 'helloooo\n' *3  

print (greetings)      #prints hello 3 times
print (greetings*2)    #prints hello 6 times (3x2)

# STRING METHODS: method/ funtion don't return the same string but a new string with changed attributes

string = 'Dayananda Sagar Academy Of Management And Technology'

print (string.lower())        #small
print (string.upper())        #caps
print (string.swapcase())     #swaps all Mono = mONO
print (string.title())        #all the words first letter is cap-ed
print (string.capitalize())   #only first letter of the string is cap-ed

str_1 = 'illay'
str_2 = 'ILLAY'

print (str_1 == str_2)                               #F
print (f'{str_1.casefold() == str_2.casefold()}')    #T    #caseless string mathching\

print(f'{str_1}'.isalpha)


print ( first_name.center(10, '*'))            #PADDING     #manasa=6    10-6= 4, sooo **Manasa**


str_3 = 'hello i am manasa and i am learning python'
print (str_3.count('python'))                 # counts how many times a sustring as been seen     str_3.count('substring", strart=0, end= len(str_3))
print (str_3.count('a' ,0 , len(str_3)))

str_4 = 'Manasa_s_naik'
print (str_4.encode())                 #text -> bytes
print (str_4.encode().decode())        #bytes -> text

print(string.endswith('logy', 0, len(string)))
print(string.endswith(('logy','Academy','Technology')))     #returns True if any one of the option fits
print(string.casefold().endswith("technology"))             #case in-sensitive

str_5 = 'hello\tthere\ti\tam\tmanasa'        # \t -> tab character    (increases space basically)
print(str_5.expandtabs())


#css-ing    SLAYYYYYYYYY
from colorama import Fore, Style

data = "name\tdept\tcourse\nmanasa\tcse\tdbms\nsara\tiot\tdbms"
lines = data.split("\n")                                           #splits data str into a list[]

# Print header in green
print(Fore.YELLOW + lines[0].expandtabs() + Style.RESET_ALL)
# Print remaining rows
for row in lines[1::]:
    print(row.expandtabs())

#the above makes the colume name yellow thats alllllllllll


print(string.find('Academy', 0, len(string)))            #returns the index number of the searched substring. No match: -1
print(string.index('Sagar', 0, len(string))) 
#print (string.index('manasa',0,len(string)))            #same func as find() --only diff is it returns a ValueError if substring is not found

age = 20
sentence = 'my name is {} and my age is {}'.format(full_name,age)      #formating how a text will be printed on console
print(sentence)


sentence2 = "I like {1} more than {0}".format("coffee", "tea")
print(sentence2)

print("helooooo".isalpha())

username = input("enter username:")         #can be used to check for validity
if username.isalpha():
    print(f'wellllcome {username}')
else:
    print('please eneter valid username')