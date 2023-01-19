
for i in range(2,15):
    if i % 2 == 0:
        for j in range(2, 15):
            print('/ \_', end='')
    else:
        for j in range(2, 15):
            print('\_/', end='')
    print('')