#Faça um Programa que peça as 4 notas bimestrais e mostre a média.
print('-'*70)
print('Programa que calcula a média de 4 notas')
print('-'*70)

#numero de notas a serem inseridas
n = 4
#inicializando a variavel media e soma
media = 0  
soma = 0

#solicitando as notas ao usuario, com a conversão para inteiro
primeira_nota = int(input("Informe a nota do primeiro bimestre"))
segunda_nota = int(input("Informe a nota do segundo bimestre"))
terceira_nota = int(input("Informe a nota do terceiro bimestre"))
quarta_nota = int(input("Informe a nota do quarto bimestre"))

#calculando a media
soma = primeira_nota + segunda_nota + terceira_nota + quarta_nota
media = soma/n

#mostrando a media na tela
print('-'*70)
print f('A media das notas é {}')
print('-'*70)

