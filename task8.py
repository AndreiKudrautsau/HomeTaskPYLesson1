# Задача 8: Требуется определить, 
# можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками 
# (то есть разломить шоколадку на два прямоугольника).
# *Пример:*
# 3 2 4 -> yes
# 3 2 1 -> no

n = int (input ("Введите количество долек шоколадки по горизонтале> "))
m = int (input ("Введите количество долек шоколадки по вертикале> "))
r = int (input ("Введите желаемое количество долек, получаемое за один разлом > "))

if r % n == 0 or r % m == 0 and r >= n and r >= m:
    print ('по горизонтале -', n, 'по вертикале -', m, 'количество долек -', r, '- > YES')
else:
    print ('по горизонтале -', n, 'по вертикале -', m, 'количество долек -', r, '- > NO')
