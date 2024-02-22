from bidict import bidict
while True:
    stolici = bidict({'Москва': "Россия", 'Лондон': "Англия"})
    a = input('Введите столицу или страну: ')
    if a in stolici:
        print(stolici[a])
    else:
        print(stolici.inverse[a])