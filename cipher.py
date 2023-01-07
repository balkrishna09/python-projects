
# Git commit to branch C
def Branch_c():
    print('I am in branch-C')





# Git commit to branch A
def Branch_A():
    print('I am in branch-A')




def encryption(text_to_encrypt, shift_no):
    cipher=''
    for letter in text_to_encrypt:
        position=alphabet.index(letter)
        new_position=position+shift_no
        cipher+=alphabet[new_position]
    print(cipher)


def decryption(text_to_encrypt, shift_no):
    cipher=''
    for letter in text_to_encrypt:
        position=alphabet.index(letter)
        new_position=position-shift_no
        cipher+=alphabet[new_position]
    print(cipher)
a=0
while a==0:
    option = input('enter yes to start and no to end- ')
    if option =='yes':
        text=input('enter text- ')
        shift=int(input('enter no of shift you want- '))
        alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a']
        choose=input('what you want encrypt or decrypt -')
        if choose=='encrypt':
            encryption(text_to_encrypt=text,shift_no=shift)
        elif choose=='decrypt' :
            decryption(text_to_encrypt=text,shift_no=shift)
        else:
            print('choose right option')
    else:
        a+=1
