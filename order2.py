ar = []
while True:
    a = input('Numbers: ')
    try:
         a = float(a)
    except:
        x = 0
    if a == 'done':
        break
    ar.append(a)

ar.sort()
print(ar)

    
