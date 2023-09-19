# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.

def newset(num):
    new_set = set()
    for i in range(num):
        new_set.add(int(input("Введите число для множества: ")))
    return new_set

n = int(input("Введите кол-во элементов первого множества: "))
n_set = newset(n)

m = int(input("Введите кол-во элементов второго множества: "))
m_set = newset(m)

print(*n_set)
print(*m_set)

s_set = sorted(n_set.intersection(m_set))
print(*s_set)