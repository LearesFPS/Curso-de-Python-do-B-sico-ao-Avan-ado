print('------------------')
print('ESCOLA BABY SAFADA')
print('------------------')
n1 = input(float('DIGÍTE A PRIMEIRA NOTA: '))
n2 = input(float('DIGÍTE A SEGUNDA NOTA: '))
m = (n1 + n2)/2
if m >= 7:
  print('ALUNO APROVADO!')
else:
  if (m >= 5) and (m < 6):
    print('ALUNO EM RECUPERAÇÃO!')
  else:
    print('ALUNO REPROVADO!')