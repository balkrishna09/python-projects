import random 
big_letter=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
small_letter=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z' ]
num=[]
for n in range(0,10):
    num.append(n)
num=str(num)
symbols = ['~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`', '}', '.', '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/']

user_s_letter=int(input('how many small alphabet you wanna use - '))
user_l_letter=int(input('how many big alphabet you wanna use - '))
user_symbol=int(input('how many small alphabet you wanna use - '))
user_no=int(input('how many small alphabet you wanna use - '))

final_s_letter=''
for s in range(1,user_s_letter+1):
    random_letter=random.choice(small_letter)
    final_s_letter+=random_letter
#print(final_letter)

final_l_letter=''
for b in range(1,user_l_letter+1):
    random_letter=random.choice(big_letter)
    final_l_letter+=random_letter

final_n_letter=''
for n in range(1,user_no+1):
    random_letter=random.choice(num)
    final_n_letter+=random_letter
    
final_sy_letter=''
for sy in range(1,user_symbol+1):
    random_letter=random.choice(symbols)
    final_sy_letter+=random_letter
    
final_letter=final_sy_letter+final_l_letter+final_n_letter+final_s_letter
print(final_letter)
    




