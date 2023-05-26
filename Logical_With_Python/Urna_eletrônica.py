yoda = 0
darth = 0
branco = 0
nulo = 0
i = 0

resp = input('Deseja iniciar a votação <S/N> : ')

if resp == 'S' or resp == 's':
    while i != 99999:
        voto = input('Darth Vader: 99\n'
                     'Mestre Yoda: 55\n'
                     'Branco: 00\n'
                     'Nulo: 66\n'
                     'Digite seu voto ou presione "Fim" para sair: ')
        if voto == "Fim" or voto == 'fim':
            break
        if int(voto) == 00:
            branco = branco + 1
        if int(voto) == 99:
            darth = darth + 1
        if int(voto) == 55:
            yoda = yoda + 1
        if int(voto) == 66:
            nulo = nulo + 1
        i = i + 1

else:print('Sessão encerrada sem votos!\n')

print('*** TOTAL DE VOTOS ***')
print('Darth Vader:', darth)
print('Mestre Yoda:', yoda)
print('Votos brancos:', branco)
print('Votos nulos:', nulo)
print('TOTAL DE VOTOS APURADOS: ',i ,'\n')

if darth > yoda:
    print("Darth Vader é o novo presidente da galáxia!")
elif yoda > darth:
    print("Mestre Yoda é o novo presidente da galáxia!")
elif yoda == 0 and darth == 0:
    print('Aguardando nova votação.')
else:print('Empate! A disputa será numa luta de sabre de luz.')