# Python como calculadora

print(2+2)
 

## Operadores básicos
### Um operador é um símbolo da linguagem de programação, capaz de operar com os valores.
### Por exemplo, assim como na aritmética, o sinal de + (mais) é o operador que é capaz de adicionar dois números, dando o resultado da adição.
# +
# -
# *
# /
# //
# %
# **


#### Exponenciação
print(2 ** 3)
print(2 ** 3.)
print(2. ** 3)
print(2. ** 3.)


#### Multiplicação
print(2 * 3)
print(2 * 3.)
print(2. * 3)
print(2. * 3.)


#### Divisão
print(6 / 3)
print(6 / 3.)
print(6. / 3)
print(6. / 3.)


#### Divisão de número inteiro (divisão arredondada)
print(6 // 3)
print(6 // 3.)
print(6. // 3)
print(6. // 3.)


#### Restante (módulo)
print(14 % 4) # --> % (percentual)
# 14 // 4 dá 3 → este é o quociente inteiro;
# 3 * 4 dá 12 → como resultado da multiplicação de quociente e divisor;
# 14 - 12 dá 2 → este é o restante.

print(12 % 4.5)
# 3.0 – não 3 mas 3.0. A regra ainda funciona:
# 12 // 4.5 dá 2.0,
# 2.0 * 4.5 dá 9.0,
# 12 - 9.0 dá 3.0.


#### Adição
print(-4 + 4)
print(-4. + 8)


#### O operador de subtração, os operadores unários e binários
print(-4 - 4)
print(4. - 8)
print(-1.1)
print(+2)


#### Operadores e suas prioridades
print(2 + 3 * 5)


#### Operadores e suas ligações
print(9 % 6 % 2)
print(6 % 2 % 9)

# --> Agr com exponenciação
print(2 ** 2 ** 3)

print(-3 ** 2)
print(-2 ** 3)
print(-(3 ** 2))

#Exemplo de operador e suas prioridades
print(2 * 3 % 5)
 
#### Operadores e parênteses
print((5 * ((25 % 13) + 100) / (2 * 13)) // 2)


#### Pontos principais
# 1. Uma expressão é uma combinação de valores (ou variáveis, operadores, chamadas para funções - você aprenderá sobre eles em breve) que resulta em um determinado valor, por exemplo, 1 + 2.

# 2. Operadores são símbolos especiais ou palavras-chave que são capazes de operar nos valores e realizar operações (matemáticas), por exemplo, o operador * multiplica dois valores: x * y.

# 3. Operadores aritméticos em Python: + (adição), - (subtração), * (multiplicação), / (divisão clássica ‒ sempre retorna um ponto flutuante), % (módulo ‒ divide o operando esquerdo pelo operando direito e retorna o restante da operação, por exemplo , 5 % 2 = 1), ** (exponenciação ‒ operando esquerdo elevado à potência do operando direito, por exemplo, 2 ** 3 = 2 * 2 * 2 = 8), // (floor/divisão inteira ‒ retorna um número resultante da divisão, mas arredondado para o número inteiro mais próximo, por exemplo, 3 // 2.0 = 1.0)

# 4. Um operador unário é um operador com apenas um operando, por exemplo, -1 ou +3.

# 5. Um operador binário é um operador com dois operandos, por exemplo, 4 + 5 ou 12 % 5.

# 6. Alguns operadores agem antes de outros - a hierarquia de prioridades:
# o operador ** (exponenciação) tem a prioridade mais alta;
# então o unário + e - (Nota: um operador unário à direita do operador de exponenciação se liga mais fortemente, por exemplo, 4 ** -1 é igual a 0.25)
# então: *, /, e %,
# e, por fim, a prioridade mais baixa: binário + e -.

# 7. Subexpressões entre parênteses são sempre calculadas primeiro, por exemplo, 15 - 1 * (5 * (1 + 2)) = 0.

# 8. O operador de exponenciação usa a associação do lado direito, por exemplo, 2 ** 2 ** 3 = 256.