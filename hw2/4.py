"""
4. Напишіть програму "fizzbuzz". Логіка програми-гри наступна: 
1) Користувач вводить ціле число. 
2) Якщо воно ділиться націло на 3, програма має вивести "fizz". 
3) Якщо воно ділиться націло на 5, програма має вивести "buzz". 
4) Якщо воно ділиться націло і на 3, і на 5, програма має вивести "fizzbuzz".
5) В інших випадках виведіть якесь повідомлення за замовчуванням. 
Підказка: використовуйте if/elif/else
"""

while True:
    try:
        n = int(input("Enter int number: "))
    except ValueError:
        print(f"{ValueError}. Please try again.")
        continue

    if n % 3 == 0 and n % 5 == 0:
        print("fizzbuzz")
    elif n % 3 == 0:
        print("fizz")
    elif n % 5 == 0 :
        print("buzz")
    else:
        print("Za zamovchennyam")
    
    break

