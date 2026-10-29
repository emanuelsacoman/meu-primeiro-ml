
# Dados de treinamento: (solo_seco, dia_quente), resposta
dados = [
    ((0, 0), 0),
    ((0, 1), 0),
    ((1, 0), 0),
    ((1, 1), 1),
]

# O neurônio começa sem conhecimento
peso_seco = 0.0
peso_quente = 0.0
vies = 0.0

taxa_aprendizado = 0.2

# Repetimos os exemplos por várias épocas
for epoca in range(1, 21):
    erros = 0

    for (seco, quente), correto in dados:

        # 1. Faz a previsão
        pontuacao = (
            seco * peso_seco
            + quente * peso_quente
            + vies
        )

        previsao = 1 if pontuacao >= 0 else 0

        # 2. Calcula o erro
        erro = correto - previsao
        erros += abs(erro)

        # 3. Aprende com o erro
        peso_seco += taxa_aprendizado * erro * seco
        peso_quente += taxa_aprendizado * erro * quente
        vies += taxa_aprendizado * erro

    print(f"Época {epoca}: {erros} erros")

    # Quando percorre tudo sem errar, encerra
    if erros == 0:
        break

print("\nModelo treinado!")
print("Peso seco:", round(peso_seco, 2))
print("Peso quente:", round(peso_quente, 2))
print("Viés:", round(vies, 2))

print("\nTestando o modelo:")
for (seco, quente), correto in dados:
    pontuacao = seco*peso_seco + quente*peso_quente + vies
    previsao = 1 if pontuacao >= 0 else 0
    print((seco, quente), "->", previsao)
