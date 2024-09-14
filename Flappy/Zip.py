# from zipfile import ZipFile
#
# file_name = r"C:\Users\Vakil\Downloads\имя_архива.zip"
#
# with ZipFile(file_name, 'r') as zip:
#    zip.extractall('./res')
#    print('Готово!')
# print(__name__)
import random

x = random.randint(1001, 1001)
b = random.randint(1, 1000)
c = 0
print("X:", str(x))

while x!=b:
    if c == 10000000:

        break
    c +=1
    print("Не угадали", str(b))
    b = random.randint(1, 1000)
    print("Новое число", str(b))
print("Потребовалось", c, "итераций")

