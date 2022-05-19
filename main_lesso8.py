Задачі для теста(спробуйте зробити кожну задачу декількома способами)

1.Ви є продукт менеджером і зараз очолюєте команду з розробки нового продукту. Нажаль, остання версія вашого продукту
не проходить перевірку якості.Оскільки кожна версія розроблена на основі попередньої версії, всі версії після
поганої версії також погані.Припустимо, у вас є n версій[1, 2, ..., n], і ви хочете знайти першу погану, через
яку всі наступні будуть поганими. Вам надається функція isBadVersion(version) -.bool, який повертає, чи є версія
поганою.Реалізуйте функцію пошуку першої поганої версії.Вам слід мінімізувати кількість викликів до функції.
Example 1:
Input: n = 5, bad = 4
Output: 4
Explanation:
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then
4 is the first bad version.
Example 2:
Input: n = 1, bad = 1
Output: 1

2. Для списку цілих чисел nums, відсортованого в зростаючому порядку, поверніть масив квадратів кожного числа,
відсортованих у зростаючому порядку.
Example 1:
Input: nums = [-4, -1, 0, 3, 10]
Output: [0, 1, 9, 16, 100]
Explanation: After squaring, the array becomes[16, 1, 0, 9, 100].
After sorting, it becomes[0, 1, 9, 16, 100].
Example 2:
Input: nums = [-7, -3, 2, 3, 11]
Output: [4, 9, 9, 49, 121]

nums = [-7, -3, 2, 3, 11]
nums_sqr = []
for i in nums:
    nums_sqr.append(i**2)
    for n in range(len(nums_sqr)-1, 0, -1):
        if nums_sqr[n] < nums_sqr[n-1]:
             nums_sqr[n], nums_sqr[n-1] = nums_sqr[n-1], nums_sqr[n]
print(nums_sqr)

nums = [-7, -3, 2, 3, 11]
nums_sqr = []
for i in nums:
    nums_sqr.append(i**2)
nums_sqr = sorted(nums_sqr)
print(nums_sqr)

3. Для списку цілих чисел nums перемістіть усі 0 в кінець, зберігаючи відносний порядок ненульових елементів.
Зауважте, що ви повинні зробити це на місці, не створюючи копію масиву.
Example 1:
Input: nums = [0, 1, 0, 3, 12]
Output: [1, 3, 12, 0, 0]
Example 2:
Input: nums = [0]
Output: [0]

nums = [0, 1, 0, 3, 12]
search_start = 0
search_stop = len(nums)-1
while search_start < search_stop:
    if nums[search_start] == 0:
        for i in range(search_start, search_stop):
            nums[i], nums[i+1] = nums[i+1], nums[i]
        search_stop -= 1
    else:
        search_start += 1
print(nums)

nums = [0, 1, 0, 3, 12]
nums.sort(key=bool, reverse=True)
print(nums)

4. Дано два відсортованих списка list1 I list2 повернути один відсортований список що місить елементи list1 I list2.
Example 1:
Input: list1 = [1, 2, 4], list2 = [1, 3, 4]
Output: [1, 1, 2, 3, 4, 4]
Example 2:
Input: list1 = [], list2 = []
Output: []
Example 3:
Input: list1 = [], list2 = [0]
Output: [0]

list1 = [1, 2, 4]
list2 = [1, 3, 4]
i = 0
j = 0
list_res = []
while i < len(list1) and j < len(list2):
    if list1[i] < list2[j]:
        list_res.append(list1[i])
        i += 1
    else:
        list_res.append(list2[j])
        j += 1
list_res += list1[i:]
list_res += list2[j:]
print(list_res)

list_res2 = sorted(list1+list2)
print(list_res2)

5. Дано масив літер змінити його порядок на протилежний не виконуючи функцій revers та[::-1]
Example 1:
Input: s = ["h", "e", "l", "l", "o"]
Output: ["o", "l", "l", "e", "h"]
Example 2:
Input: s = ["H", "a", "n", "n", "a", "h"]
Output: ["h", "a", "n", "n", "a", "H"]

my_str = ["h", "e", "l", "l", "o"]
for i in range(len(my_str)//2):
    my_str[i], my_str[-i-1] = my_str[-i-1], my_str[i]
print(my_str)

6. Написати функцію, яка приймає число n. А повертає значення числа фібоначі з порядковим номером N
Example 1:
Input: n = 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
Example 2:
Input: n = 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
Example 3:
Input: n = 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.

def decor_check_int(func):
    def wrapper(n):
        if type(n) != int:
            return "Not number"
        if n < 0:
            return "Negative number"
        if n == 0:
            return 0
        return func(n)
    return wrapper

@decor_check_int
def fib1(n):
    fib_prev = 0
    fib_last = 1
    i = 0
    while i <= n-2:
        fib_sum = fib_prev + fib_last
        fib_prev = fib_last
        fib_last = fib_sum
        i = i + 1
    return fib_last

@decor_check_int
def fib2(n):
    if n in (1, 2):
        return 1
    return fib2(n - 1) + fib2(n - 2)

from functools import reduce
@decor_check_int
def fib3(n):
    fib_list = reduce(lambda x, _: x + [x[-2] + x[-1]], [0] * (n-2), [1, 1])
    return fib_list[n-1]

print(fib1(2))
print(fib2(3))
print(fib3(4))
