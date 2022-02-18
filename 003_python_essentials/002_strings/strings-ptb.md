# Strings (PTB)

Neste tutorial, você aprenderá mais sobre strings no Python. Então, defini a variável seguinte:
````python
course = 'Python for Beginners'
````
Anteriormente, eu disse que você poderia usar aspas simples ou duplas para definir uma string, mas há momentos em que você precisa usar uma dessas opções, caso contrário terá problemas.

Aqui está um exemplo: imagine que você queira mudar essa string para _Python's course for Beginners_. Então, queremos adicionar um apóstrofo, como este:

````python
course = 'Python's course for Beginners'
````
Você pode dizer que isso está ficando estranho, porque nossa string começa em 'P' e termina em 'n'. 
Todos esses caracteres que temos aqui após o segundo apóstrofo (_s course for Beginners_), o interpretador Python não sabe o que são. 

Então, para resolver esse problema, precisamos usar aspas duplas para definir nossa string, para que possamos ter uma aspa simples no meio da string. 
Então, vamos mudar as aspas do início e final da string para duplas, para podermos ter o apóstrofo em _Python's_ corretamente interpretado:
````python
course = "Python's course for Beginners"
print(course)
````
Agora vamos dizer que não queremos este apóstrofo aqui, então temos "Python for Begginers", mas queremos colocar Beginners entre aspas duplas. 
Mais uma vez, se você adicionar uma aspa dupla aqui, o interpretador Python fica confuso porque assume que a segunda aspa dupla indica o final da string, então ele não sabe quais são esses caracteres:
````python
course = "Python for "Beginners"
print(course) 
````
Então, para resolver isso, precisamos mudar nossas aspas duplas para aspas simples, e então podemos manter aspas duplas na palavra _Beginners_:

````python
course = 'Python for "Beginners"'
print(course) 
````
Portanto, existem os casos de uso de aspas simples ou duplas. 
Agora, em todos os exemplos, mostrei que lidamos apenas com strings curtas, mas e se você quisesse definir uma string com várias frases? 
Por exemplo, e se você quisesse definir uma string para a mensagem que enviamos em um e-mail. Nesse caso, precisamos usar aspas triplas. 
Portanto, temos 3 aspas para iniciar nossa string e 3 aspas para finalizá-la. 
Novamente, essas aspas podem ser aspas simples ou duplas. Agora, com isso, podemos definir uma string que abrange várias linhas. 
Por exemplo:
````python
course = '''
Hi Teresa, 

Here is our first email to you. 

Thank you, 

Patrick
'''
print(course) 
````
Então, obtemos essa bela string de várias linhas. 
Agora, vamos mudar isso de volta para algo simples, para que possamos ver outras características de strings em Python. 
Vou usar aspas simples e definir o nome da variável _course_ como _Python for Beginners_. Agora aqui vamos usar colchetes para obter um caractere e um determinado índice nesta string. Então, para obter o primeiro caractere, usamos colchetes e digitamos 0:
````python
course = 'Python for Beginners'
print(course[0])
````

Portanto, o índice do primeiro caractere nesta string é 0. Em outras palavras, é assim que as strings Python são indexadas: 0, 1, 2, 3, etc. 
Então, o índice do primeiro caractere é 0, o índice do segundo é 1 e assim sucessivamente. Então, se executarmos este programa, obtemos _P_. 
Também podemos usar um índice negativo aqui. E esse é um dos recursos que não temos em outras linguagens de programação. 
Com índice negativo, podemos começar a buscar os caracteres do final. Então, se eu passar negativo 1 aqui, assumindo que 0 é o primeiro caractere, negativo 1 é o último caractere. 
Então, quando executamos este programa, devemos ver _s_:

````python
course = 'Python for Beginners'
print(course[-1])
````
Se passarmos menos 2, isso retornará o segundo caractere do final (_r_). OK? Portanto, preste muita atenção a esta sintaxe de colchetes, porque muitas vezes é o tópico para testes online de Python ou exames universitários. 
Também podemos usar uma sintaxe semelhante para extrair alguns caracteres em vez de um caractere. Por exemplo, se digitarmos:
````python
course = 'Python for Beginners'
print(course[0:3])
````
O interpretador Python retornará todos os caracteres começando com _0_ até _3_, mas não retornará o caractere no índice 3. 
Agora, aqui também temos valores padrão para o índice inicial e final. Portanto, se não fornecermos o índice final, o Python retornará todos os caracteres até o final da string:
````python
course = 'Python for Beginners'
print(course[0:])
````
Mas se você alterar o índice inicial para 1, isso excluirá o primeiro caractere:
````python
course = 'Python for Beginners'
print(course[1:])
````
Da mesma forma, temos um valor padrão para o índice inicial. Portanto, se não o fornecermos e adicionarmos e terminarmos o índice como 5, o Python assumirá 0 como o índice inicial:
````python
course = 'Python for Beginners'
print(course[:5])
````
Agora, e se deixarmos o índice inicial e o índice final? Neste caso, 0 será assumido como o índice inicial e o comprimento da string será assumido como o índice final. Então, com esta sintaxe, você pode basicamente copiar ou clonar uma string:
````python
course = 'Python for Beginners'
print(course[:])
````
Em outras palavras, se eu definir outra variável aqui, vamos chamá-la de _another_ e configurá-la assim:
````python
course = 'Python for Beginners'
another = course [:]
print(another)
````
A segunda variável será a cópia da primeira. 
Agora aqui está um pequeno exercício para você: Defina uma variável, chamada _name_, e defina-a como _Jane_. Quando printamos:
````python
course = 'Jane'
print(course[1:-1])
````
O que você acha que vai aparecer no terminal?

# Formatted Strings

Strings formatadas são particularmente úteis em situações em que você gera dinamicamente algum texto com suas variáveis. 
Digamos que temos duas variáveis:
````python
first_name = 'Jane'
last_name = 'Joplin'
````
Então, digamos que com essas duas variáveis, queremos gerar algum texto como este:
````python
first_name = 'Jane'
last_name = 'Joplin'
Jane [Joplin] was a singer
````
Como fazemos isso? Definimos outra variável como _message_, adicionamos o primeiro nome e o concatenamos com uma string que contém um espaço e um colchete. 
Em seguida, precisamos adicionar um sobrenome, então precisamos adicionar uma string que contenha os colchetes de fechamento seguidos de _was a singer_:
````python
first_name = 'Jane'
last_name = 'Joplin'
message = first_name + ' [' + last_name + '] was a singer'
print(message)
````
Embora essa abordagem funcione perfeitamente, não é ideal porque, à medida que nosso texto fica mais complicado, fica mais difícil visualizar o output. 
Então, alguém lendo este código teria que visualizar todas as concatenações de strings em sua cabeça. 
É aqui que usamos strings formatadas, elas facilitam a visualização do output.

Então, vamos definir outra variável chamada _msg_ e defini-la como uma string formatada.

Uma string formatada é aquela que é prefixada com _f_:
````python
msg = f'{first_name} [{last_name}] was a singer'
print(msg)
````
Com essas chaves, estamos definindo espaços reservados ou buracos em nossa string, e quando executamos nosso programa esses buracos serão preenchidos com o valor de nossas variáveis. 
Então aqui temos 2 marcadores de posição com as chaves '{ }'.

Com essa string formatada, podemos visualizar facilmente como é a saída.

Portanto, para definir strings formatadas, prefixe-o com um _f_ e adicione chaves para inserir valores dinamicamente em suas strings.

# String Methods

Para calcular o número de caracteres na string abaixo, podemos usar uma função interna chamada len:
````python
course = 'Python for Beginners'
print(len(course))
````
Então, como você pode ver, temos 20 caracteres nesta string. Isso é particularmente útil quando você recebe entrada do usuário (input). 
Por exemplo, você notou que, quando você preenche um formulário online, cada campo de entrada geralmente tem um limite? 
Por exemplo, você pode ter 50 caracteres para o seu nome. Portanto, usando esta função de _len_, podemos impor um limite no número de caracteres em um campo de entrada. Se o usuário digitar caracteres além do que permitimos, podemos exibir um erro.

Agora, essa função _len_ é outra função incorporada ao Python, é uma função de uso geral, portanto não está restrita somente em contar o número de caracteres em uma string. Podemos usar esta função para contar o número de itens em uma lista também, por exemplo.

Agora também temos funções específicas para strings. Referimo-nos a essas funções como métodos (estilo de programação orientada a objetos). Para acessar essas funções, usamos o operador '.':

* para converter todos esses caracteres em maiúsculas
````python
course = 'Python for Beginners'
print(course.upper())
````
* para converter todos esses caracteres em minúsculas
````python
course = 'Python for Beginners'
print(course.lower())
````
Observe que esses métodos não alteram as strings originais; na verdade, eles criam novos e mantêm o original como está. 
Então, se imprimirmos nossa variável _course_ logo após chamarmos o método _upper_, podemos ver que nossa variável de curso ainda tem sua forma original:
````python
course = 'Python for Beginners'
print(course.upper())
print(course)
````
Agora, se você deseja encontrar um caractere ou uma sequência de caracteres em uma string, pode usar o método _find_. 
Isso retornará o índice da primeira ocorrência do caractere 'o':
````python
course = 'Python for Beginners'
print(course.find('o'))
````
Observe que o método _find_ é sensível a caracteres minúsculos e maiúsculos. Por exemplo, se passarmos o caractere maiúsculo 'O', ele retornará '-1' porque não temos maiúsculas nesta string:
````python
course = 'Python for Beginners'
print(course.find('O'))
````
Nós também podemos procurar por uma sequência de caracteres:
````python
course = 'Python for Beginners'
print(course.find('Beginners'))
````
Obtemos '11', porque a palavra começa com o índice 11.

Também temos um método para substituir um caractere ou uma sequência de caracteres: _replace_.
````python
course = 'Python for Beginners'
print(course.replace('Beginners', 'Managers'))
````
O mesmo método pode ser usado para substituir um único caracter:
````python
course = 'Python for Beginners'
print(course.replace('B', 'T'))
````
Esse método, como o _find_, diferencia maiúsculas de minúsculas (_case sensitive_).

Há momentos em que você deseja verificar a existência de um caractere ou sequência de caracteres em sua string. 
Nessas situações, você usa o operador _in_. 
Então, digamos que você queira saber se essa string contém a palavra 'Python':
````python
print('Python' in course)
````
Esta é uma expressão booleana e obtém _true_ ou _false_ como _output_. 
Ou seja, trata-se de outro método _case sensitive_:
````python
print('python' in course)
````
