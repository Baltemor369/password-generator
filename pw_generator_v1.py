import random

letter_min="azertyuiopmlkjhgfdsqwxcvbn"
letter_maj="AZERTYUIOPQSDFGHJKLMWXCVBN"
nb="12345678901234567890"
spe_char="&#{[|\"\@]}=+-*/§?<>'(-_)$£*%!.;:,'"
same_settings=False
while 1:
    
    if not same_settings:
        while 1:
            len_pw=int(input("Enter the length for your password (>1) : "))
            if len_pw and len_pw >1:
                break

        check_letter_min=input("Do you want lowercase letter Y/N? ").upper()=="Y"
        check_letter_maj=input("Do you want capital letter Y/N? ").upper()=="Y"
        check_number=input("Do you want number Y/N? ").upper()=="Y"
        check_spe_char=input("Do you want special char Y/N? ").upper()=="Y"

        tmp=check_letter_min+check_letter_maj+check_number+check_spe_char
    
    pw=""
    i=0
    while i<len_pw:
        loto=random.randrange(0,4)
        if check_letter_min and loto==0:
            pw+=letter_min[random.randrange(0,len(letter_min))]
        elif check_letter_maj and loto==1:
            pw+=letter_maj[random.randrange(0,len(letter_maj))]
        elif check_number and loto==2:
            pw+=nb[random.randrange(0,len(nb))]
        elif check_spe_char and loto==3:
            pw+=spe_char[random.randrange(0,len(spe_char))]
        i=len(pw)
        

    print(pw)
    if input("generate another one Y/N ? ").upper()!="Y":
        break
    same_settings=input("Keep the same settings Y/N ?").upper()=="Y"