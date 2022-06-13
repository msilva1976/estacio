"""def multiplicador(numero):
    global a # todas as referencias a variavel a são para a global
    a = 2 #a global se alterado
    print('Dentro da função, variavel vale: {}'.format(a))
    return a *numero

a = 3 #esta variavel tem escopo global
b = multiplicador(5)
print('A variavel b {}'.format(b))
print('Fora da função, a variavel a vele {} '.format(a))"""


'''def function1():
    a = 10
    print('function1 ')
    print(a)

a = 30
print('no corpo principal')
print(a)

print(a)'''
from numpy import array
notas_real = array([2, 5, 10, 20, 50, 100],dtype=int)