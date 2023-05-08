"""
6. нехай користувач введе два числа - a i b, при цьому a має бути менше b. Виведіть середнє арифметичне чисел
 з відрізку [a;b], але тільки тих, що діляться націло на 3. 
Підказка: зверніть увагу, що відрізок [a;b] включає в себе і a, i b. 
Щоб знайти середнє арифметичне чисел, Ви маєте їхню суму поділити на їхню кількість.
"""
"""
1) input 2 digits
2) proverka, chto a<b. trebovat vvod zanovo esli a>b
3) naity vse chisla ot a do b , kotorye delyatsya na 3
4) poschitat kolicestvo etih chisel
5) naity sr. arif.
"""
while True:
    a = int(input('vvedi menshee chislo: '))
    b = int(input('vvedi bolshee chislo: '))
    if a > b:
        print('a dolzhno byt menshe, dubina!')
        continue
    else:
        chislitel = 0
        delitel = 0
        while a <= b:
            if a % 3 == 0:
                chislitel += a
                delitel += 1
                a += 1
            else:
                a += 1
        print(f"sr.arif: {chislitel/delitel}")
        break
