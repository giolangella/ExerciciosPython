#EXERCÍCIO 04 - FAÇA UM PROGRAMA QUE LEIA ALGO PELO TECLADO E MOSTRE NA TELA O SEU TIPO PRIMITIVO E TODAS AS INFORMAÇÕES POSSÍVEIS SOBRE ELE
x = input ('Digite algo: ')
print (x, 'É do tipo primitivo', type(x))
print (x, 'É numérico? ', x.isnumeric(), '!')
print (x, 'É alfabético? ',  x.isalpha(), '!')
print (x, 'É alfanumérico? ', x.isal)
print (x, 'Possuia apenas letras maiúsculas?', x.isupper())
print (x, 'Possui apenas letras minúsculas?', x.islower())
print (x, 'Está capitalziada? ', x.istitle())

