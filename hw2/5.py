"""
5. Дозвольте користувачу вводити цілі числа по черзі. Якщо введене число менше 10, пропустіть 
його і нічого не робіть. Якщо воно більше 100, зупиніть введення чисел і програму.
 В інших випадках виводьте число на екран. 
 Підказка: використовуйте if/elif/else/break/continue
"""

"""
1) Vvod chisla
2) Sravnitm chislo s 10
3) Esli menshe 10 to propustit i nichego
4) Esli bolshe 100 no ostanovit programmu
5) Drugie sluchai
6) Pechat chisla
"""
while True:
    try:
        n = int(input("Enter the whole number motherfucker: "))
    except ValueError:
        print("Stupido, enter the WHOLE number, you're id..t! ")
        continue

    if n < 10:
        continue
    elif n > 100:
        break
    else:
        print(f"{n=}")
