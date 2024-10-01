# texto = "Programação em Python" 
# contador_vogais = 0
# for caractere in texto:
#    if caractere.lower() in "aeiou":
#        contador_vogais += 1
# print(f"Número de vogais: {contador_vogais}")

# nota1 = float(input("Digite a primeira nota: "))
# nota2 = float(input("Digite a segunda nota: "))
# nota3 = float(input("Digite a terceira nota: "))
# nota4 = float(input("Digite a quarta nota: "))
# nota5 = float(input("Digite a quinta nota: "))
# notas = [nota1, nota2, nota3, nota4, nota5]
# soma = 0
# for nota in notas:
#    soma += nota
#
# media = soma / len(notas)

# if media >= 6:
#    print("Aprovado")
# else:
#    print("Reprovado")

soma_notas = 0

for i in range(5):
    nota = float(input(f"Digite a nota {i+1}: "))
    soma_notas += nota

    media = soma_notas / 5

print(f"A média das notas é: {media: .2f}")
if media >= 6:
    print("Aprovado")
else:
    print("Reprovado")

