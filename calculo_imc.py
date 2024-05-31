def calcular_imc(peso,altura):
    return peso / (altura ** 2)

def obter_dados_usuario():
    nome = input("qual o seu nome:?")
    idade = int(input("quantos anos voçe tem:?"))
    altura = float(input("qual a sua altura em metros:?"))
    peso = float(input("qual o seu peso em kilogramas?:"))
    return nome, idade, altura, peso

def main():
    
    nome, idade, altura, peso = obter_dados_usuario()
    imc = calcular_imc(peso, altura)
    print(f"seu nome é: {nome}")
    print(f"sua idade é: {idade} anos")
    print(f"sua altura é: {altura} metros")
    print(f"seu peso é: {peso} kg")
    print(f"e seu imc é: {imc: .2f}")
    
if __name__ == "__main__":
    main()
    