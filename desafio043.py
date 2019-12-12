altura = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))
imc = peso / altura ** 2
if imc < 17:
    print(f'Seu IMC é: {imc:.2f}, considerado desnutrição. ')
elif imc < 18.5:
    print(f'Seu IMC é: {imc:.2f}, considerado abaixo do peso. ')
elif imc < 25:
    print(f'Seu IMC é: {imc:.2f}, considerado normal. ')
elif imc < 30:
    print(f'Seu IMC é: {imc:.2f}, considerado acima do peso. ')
elif imc < 35:
    print(f'Seu IMC é: {imc:.2f}, considerado obesidade I. ')
elif imc < 40:
    print(f'Seu IMC é: {imc:.2f}, considerado obesidade II. ')
else:
    print(f'Seu IMC é: {imc:.2f}, considerado obesidade mórbida. ')
