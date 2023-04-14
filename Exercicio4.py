x = 3
y = 4
z = 0.6

print (x+x*x**(y*x)/z);
print (((not(x + z < y)) or (x + x * z >= y)) and True);

#print(x + x * x ** (y * x) / z);
#Nesta linha, o Python seguiria a ordem de precedência dos operadores, resolvendo primeiro a potência, depois a multiplicação e, por último, a divisão e a adição. Portanto, a expressão seria resolvida da seguinte forma:

#x ** (y * x) = 3 ** (4 * 3) = 3 ** 12 = 531441
#x * 531441 = 3 * 531441 = 1594323
#1594323 / z = 1594323 / 0.6 = 2657205.0
#x + 2657205.0 = 3 + 2657205.0 = 2657208.0
#Portanto, a saída seria: 2657208.0

#print(((not(x + z < y)) or (x + x + z >= y)) and True);
#Nesta linha, o Python avaliaria primeiro a expressão dentro dos parênteses e, em seguida, a expressão completa. A expressão dentro dos parênteses seria avaliada da seguinte forma:

#x + z = 3 + 0.6 = 3.6
#x + z < y = 3.6 < 4 = True
#not(True) = False
#Em seguida, a expressão completa seria avaliada da seguinte forma:

#x + x + z = 3 + 3 + 0.6 = 6.6
#6.6 >= y = 6.6 >= 4 = True
#False or True = True
#True and True = True
#Portanto, a saída seria:

