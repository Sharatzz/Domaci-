#Zadatak 1:

def desifrovanje_koda():

    s= 0
    p = 1

    tb = input('Unesite trocifreni broj')

    

    for _ in tb:

        s = s + int(_)
        p = p * int(_)

    print(p - s)


desifrovanje_koda()

print('Viktor')