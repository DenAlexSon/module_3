# 1.Функция с параметрами по умолчанию:
def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(a=2, b='столбец', c=False)
print_params(b=25)
print_params([1, 2, 3])
print_params(5, 8)

values_list = [1, 2, 3]
values_dict = {'a': 3, 'b': 2, 'c': 1}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)
