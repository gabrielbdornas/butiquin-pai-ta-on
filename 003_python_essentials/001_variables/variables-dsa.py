# Variáveis e operadores
# https://github.com/Andrelamor/PythonFundamentos/blob/master/Cap02/Notebooks/DSA-Python-Cap02-02-Variaveis.ipynb

#variáveis e operadores
var_teste = 1
var_teste
print(var_teste)
var_teste = 2
print(var_teste)
print(type(var_teste))
var_teste = 9.5
print(type(var_teste))
x = 1
print(x)

#declaração múltipla
p1, p2, p3 = "Francisco", "Gabriel", "André"
print(p2)
print(p3 + ' trabalha com ' + p1 + ' e com ' + p2 + ' e eles estão dispostos a estudar python')
fruta1 = fruta2 = fruta3 = 'caqui'
print(fruta1)
print(fruta2)
print(fruta3)

#variáveis atribuídas a outras variáveis e ordem dos operadores
largura = 2
altura = 4
area = largura * altura
perimetro = 2 * largura + 2 * altura
print(area)
print(perimetro)

#operações com variáveis
idade1 = 25
idade2 = 35
print(idade1 - idade2)
print(idade1 / idade2)
print(idade2 % idade1)

#concatenação de variáveis
tipo = "pacote"
nome = 'dpckan'
full_name = tipo + ' ' + nome
print(full_name)
