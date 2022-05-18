# 1. Приймає радіус кола, повертає довжину кола. Обробити випадки коли в радіус приходить не числом.
from math import pi
def circle_perimetr(r):
    try:
        return 2 * pi * r
    except:
        return
radius = 5
result = circle_perimetr(radius)
if result is None:
    print("Not number")
else:
    print(result)

# 2. Приймає радіус кола, повертає площу кола. Обробити випадки коли в радіус приходить не числом.
from math import pi
def circle_area(r):
    try:
        return pi * r ** 2
    except:
        return
radius = 2
result = circle_area(radius)
if result is None:
    print("Not number")
else:
    print(result)

# 3. Приймає число, повертає чи є число паліндромом. Тобто з права наліво і зліва на право читається однаково.
#    12321 - це паліндром, 1234 - не паліндром.
def is_palindrome(x: int):
    x_lst = list(str(x))
    for i in range(len(x_lst)//2):
        if x_lst[i] != x_lst[len(x_lst)-i-1]:
            return False
    return True
def is_palindrome1(x:int):
    x_str = str(x)
    x_rev = x_str[::-1]
    if x_str == x_rev:
        return True
    else:
        return False
def is_palindrome2(x: int):
    copy_x = x
    rev_x = 0
    while x != 0:
        rev_x = rev_x * 10 + x % 10
        x = x // 10
    if copy_x == rev_x:
        return True
    else:
        return False
print(is_palindrome(1562651))
print(is_palindrome1(152651))
print(is_palindrome2(156265))
#
# # 4. Функція приймає число n яке більше ніж 0. За допомогою рекурсії виводить всі числа що менші n, але більші ніж 0.
def my_recur(n: int):
    n = n - 1
    print(n)
    if n < 2:
        return
    return(my_recur(n))
my_recur(1)

# 5. Написати функцію lambda що приймає x i y, а повертає x^2 + y^2
sum_sqr = lambda x, y: x**2 + y**2
print(sum_sqr(5, 3))

# # 6. Написати функцію lambda що приймає слово і повертає його довжину.
my_len = lambda x: len(x)
print(my_len("asdasdasd"))

# # 7. Написати map що перетворює всі числа в списку на строку.
my_lst = [1, 4, 3, 6, 8]
my_str = ""
my_str = my_str.join(map(str, my_lst))
print(my_str)

# # 8. Написати filter що залишає в списку тільки числа > 10
import random
my_lst = [random.randint(0, 20) for i in range(20)]
print(my_lst)
my_lst = list(filter(lambda max_int: max_int > 10, my_lst))
print(my_lst)

# 9. Є список слів, за допомогою map видалити з кожного слова всі букви "а" (abcd -> bcd )
#    (2 способи з lambda і без) (підказка: використати метод replace)
def my_repl(def_str):
    def_str = def_str.replace("a", "")
    return def_str
my_str_lst = ["wa", "add","waas", "assas", "daadadd", "qqaaqaqqa", "wawwaawa"]
my_str_def = list((map(my_repl, my_str_lst)))
print(my_str_def)
my_str_lmd = list((map(lambda x: x.replace("a", ""), my_str_lst)))
print(my_str_lmd)

# 10. Є список слів, за допомогою filter залишити тільки ті слова в яких к-ть букв більша ніж 4.
#    (2 способи з lambda і без)
def my_del(def_str):
    if len(def_str) > 4:
        return True
    else:
        return False
my_str_lst = ["wa", "add","waas", "assas", "daadadd", "qqaaqaqqa", "wawwaawa"]
my_str_def = list(filter(my_del, my_str_lst))
print(my_str_def)
my_str_lmd = list(filter(lambda x: len(x) > 4, my_str_lst))
print(my_str_lmd)
