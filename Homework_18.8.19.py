bilet = int(input("Введите количество билетов, которые хотите приобрести: ")) #Получаем от пользователя количество билетов

sum = 0 #Задаем переменную, в которой будет прибавляться стоимость каждого билета

for i in range(1, bilet + 1): #Начинаем цикл
    print("Введите возраст посетителя", i, ":")
    vozrast = int(input()) #Получаем от пользователя возраст каждого посетителя
    if 18 <= vozrast <= 25: #В зависимости от введенного возраста проверяем условия и прибавляем соответствующую стоимость к сумме в переменную sum
        sum += 990
    elif vozrast > 25:
        sum += 1390

if bilet > 3: #Проверяем сколько билетов хочет приобрести пользователь и применяем скидку к общей сумме, если билетов больше трех
    sum = sum - sum * 10 / 100

print("Сумма к оплате:", sum) #Выводим пользователю сумму к оплате
        