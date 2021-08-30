import matplotlib.pyplot as plt

# Trata o arquivo CSV de entrada
with open('dados/Falsificacao_Dados_Abertos.csv', 'r') as arquivo:
    linhas = arquivo.readlines()

    # Utiliza List Comprehensions pra iterar sobre todas as linhas
    # removendo os '\n' e dividindo a string no ponto e vírgula
    conteudo = [linha.replace('\n', '').split(';') for linha in linhas]

    # Dicionário de resultados no formato:
    # resultado = {
    #    "{ano com 2 dígitos}": {quantidade de cédulas totais},
    #    "{ano com 2 dígitos}": {quantidade de cédulas totais},
    #    ...
    # }
    resultado = {}

    # Trata o resultado, adicionando valores ao dict "resultado"
    for linha in conteudo:
        ano = linha[0][2:]
        quantidade = float(linha[4].replace('.', '').replace(',', '.'))

        try:
            resultado[ano] = resultado[ano] + quantidade
        except KeyError:
            resultado[ano] = 0
            resultado[ano] = resultado[ano] + quantidade


# Cria o Eixo X com os "ANOS"
eixo_x = list(resultado.keys())

# Cria o Eixo Y com os a Quantidade de Cédulas
eixo_y = list(resultado.values())

# Cria um Figure e um Axes (classes do Matplotlib)
figura, eixos = plt.subplots()

# Plota os pontos e adicina rótulo ao conjunto de dados
eixos.plot(eixo_x, eixo_y, label='Número total de cédulas falsificadas')

# Mostra a "grid" (linhas horizontais e verticais)
eixos.grid(True)

# Adiciona rótulos nos Eixos X e Y
eixos.set_xlabel('Ano')
eixos.set_ylabel('Quantidade de Cédulas Falsificadas')

# Adiciona rótulo superior
eixos.set_title("Cédulas Falsificadas no Brasil")

# Adiciona legenda
eixos.legend()

# Por fim, mostra o resultado em tela =D
plt.show()
