morse_code_d= { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}
option=int(input("Enter 1 to convert morse to letter and 2 to convert letter to morse: " ))
message=str(input("message: "))

def morsetoletter(message):
    answer=''
    message=message.split(' ')
    morse_code_l_keys=list(morse_code_d.keys())
    morse_code_l_values=list(morse_code_d.values())
    
    #print(message)
    for i in message:
        index=morse_code_l_values.index(i)
        answer+=morse_code_l_keys[index]+' '
    
    print(answer)
    
#morsetoletter(message)

def lettertomorse(message):
    message=message.upper()
    answer=''
    for letter in message:
        #print(letter)
        if letter != ' ':
            answer+=morse_code_d[letter]+' '
            #print(answer,end="")
        else:
            answer+=' '
            
    print(answer)
#lettertomorse(message)

if option==1:
    print('Answer is')
    morsetoletter(message)
elif option==2:
    print('Answer is')
    lettertomorse(message)