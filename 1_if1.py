age = int(input())
def employment(age):
    if 3 <= age <= 6:
        return ('Учится в детском саду')
    elif 7 <= age <= 18:
        return ('Учится в школе')
    elif 19 <= age <= 22:
        return ('Учится в ВУЗе')
    elif 23 <= age:
        return ('Работает')
print(employment(age))