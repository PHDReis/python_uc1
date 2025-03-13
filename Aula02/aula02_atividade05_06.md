# Exercícios feitos em aula utilizando a IDLE do Python

Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

numero_inteiro=15
numero_real=15,15
texto=("cinco")
type(numero_inteiro)
<class 'int'>
type(numero_real)
<class 'tuple'>
type(texto)
<class 'str'>
numero_real=15.15
type(numero_real)
<class 'float'>
numero_inteiro+numero_real
30.15
numero_inteiro+texto
texto*numero_inteiro
'cincocincocincocincocincocincocincocincocincocincocincocincocincocincocinco'
texto2=texto+""
texto2*numero_inteiro
'cincocincocincocincocincocincocincocincocincocincocincocincocincocincocinco'
texto2=texto+" "
texto*numero_inteiro
'cincocincocincocincocincocincocincocincocincocincocincocincocincocincocinco'
>>> texto2*numero_inteiro
'cinco cinco cinco cinco cinco cinco cinco cinco cinco cinco cinco cinco cinco cinco cinco '
>>> 
>>> 
>>> 

>>> 
>>> 
>>> 
>>> idade=input("Digite a sua idade ")
Digite a sua idade 30
>>> type(idade)
<class 'str'>
>>> help(input)
Help on built-in function input in module builtins:

input(prompt='', /)
    Read a string from standard input.  The trailing newline is stripped.

    The prompt string, if given, is printed to standard output without a
    trailing newline before reading input.

    If the user hits EOF (*nix: Ctrl-D, Windows: Ctrl-Z+Return), raise EOFError.
    On *nix systems, readline is used if available.

>>> idade_numero=int(idade)
>>> type(idade_numero)
<class 'int'>
>>> idade_numero_2=int(input("Qual a sua idade ? "))
Qual a sua idade ? 30
>>> type(idade_numero_2)
<class 'int'>
>>> 
>>> 
>>> ANO_ATUAL=2025
>>> idade_numero_2=int(input("Qual a sua idade ? "))
Qual a sua idade ? 30
>>> ano_nascimento=ANO_ATUAL-idade_numero_2
>>> print(ano_nascimento)
1995
