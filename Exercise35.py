HumanYears=float(input('Enter human years:'))
DogYears=float
if 0<HumanYears<=2:
    DogYears=HumanYears*21
    print(HumanYears, 'human years is equivalent to', DogYears, 'dog years')
elif HumanYears>=2:
    DogYears=21+(HumanYears-2)*4
    print(HumanYears, 'human years is equivalent to', DogYears, 'dog years')
else:
    print('ERROR.')
