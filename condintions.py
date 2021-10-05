temp = 0

while temp != 999:
    temp = int(input('please enter the current temperature: '))

    if temp == 999:
        print('program end.')
    elif temp > 90:
        print('wear shorts.')
    elif temp > 70:
        print ('short sleeves are fine. ')
    elif temp > 50:
        print('wear a jacket. ')
    elif temp > 32:
        print('wear a heavy coat. ')
    else:
        print('stay inside.')

    print(' ')
    

