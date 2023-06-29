print("Введите слово маленькими латинскими буквами")
slovo=input()
kol_sog=0
kol_a=0
kol_e=0
kol_i=0
kol_o=0
kol_u=0
# ==================================
for element in slovo:
    if element=="a":
        kol_a+=1
    elif element=="e":
        kol_e+=1
    elif element=="i":
        kol_i+=1
    elif element=="o":
        kol_o+=1
    elif element=="u":
        kol_u+=1
    else:
        kol_sog+=1

print("Слово содержит:")
print(kol_sog,"согласных")
print((kol_a+kol_e+kol_i+kol_o+kol_u),"гласных, в том числе:")
# ==================================
if kol_a==0:
    print("Букв 'a':",False)
else:
    print("Букв 'a':",kol_a)

if kol_e==0:
    print("Букв 'e':",False)
else:
    print("Букв 'e':",kol_e)
    
if kol_i==0:
    print("Букв 'i':",False)
else:
    print("Букв 'i':",kol_i)

if kol_o==0:
    print("Букв 'o':",False)
else:
    print("Букв 'o':",kol_o)
    
if kol_u==0:
    print("Букв 'u':",False)
else:
    print("Букв 'u':",kol_u)



# Не смог победить с помощью команды map(),пришлось погуглить
# и забежать чуть вперёд )
