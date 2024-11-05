import re
#1
def check_license_plate(plate):

    personal_pattern = r'[АВЕИКМНОРСТУХ]\d{3}[АВЕИКМНОРСТУХ]{2}\d{2,3}'
    taxi_pattern = r'[АВЕИКМНОРСТУХ]{2}\d{3}\d{2,3}'
    plate = plate.upper()
    if re.match(personal_pattern, plate):
        return "Частный легковой автомобиль"
    elif re.match(taxi_pattern, plate):
        return "Такси"
    else:
        return "Некорректный номер"
plates = ['А333АА78', 'A333AA77',"ТТ22278",'Д256Д22']
for i in plates:
    result = check_license_plate(i)
    print(f"{i}: {result}")
#2
file = open('2.txt', 'r', encoding='utf-8')
text = file.read()
a = sum(1 for word in text.split() if all(c.isalpha() or c == '-' for c in word))
print(text)
print(a)
#3
from functools import reduce
from functools import reduce
s='Уважаемые! Если вы к 09:00 не вернёте чемодан, то уже в 09:00:01 я за себя не отвечаю.'
s=s.split()
x=list(filter(lambda x: re.search(r'\b(0[0-9]|1[0-9]|2[0-4])[:](0[0-9]|[0-9]{2})\b',x) ,s))
s= reduce(lambda x,y:  x+' '+y, s)
for i in x:
    s=s.replace(i,'(TBD)',1)
print(s)
#4
s='Владимир устроился на работу в одно очень важное место. И в первом же документе он ничего не понял, там были сплошные ФГУП НИЦ ГИДГЕО, ФГОУ ЧШУ АПК и т.п. '
x=re.findall(r'\b[А-ЯЁ][А-ЯЁ ]*[А-ЯЁ]\b',s)
print(x)