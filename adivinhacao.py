print('********************************');
print('Bem vindo ao jogo de adivinhação');
print('********************************');

numero_secreto = 43;

chute_str = input("Digite o seu número: ");

print("Você digitou ", chute_str);

chute = int(chute_str);

acertou = chute == numero_secreto;

maior = chute > numero_secreto;
menor = chute < numero_secreto;

if ( acertou ):
    print('acertou');
else:
    if(maior):
        print("Você errou!! O seu chute foi maior que o numero secreto")
    elif (menor):
        print("Você errou!! O seu chute foi menor que o numero secreto")

print('fim do Jogo')

def oi( hello: str ) -> str:
    print(hello)
    return 'oii'
oi(hello='1')

