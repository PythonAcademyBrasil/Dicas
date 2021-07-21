import easyocr

# Define Português como idioma
reader = easyocr.Reader(['pt'])

# Lê a imagem
resultados = reader.readtext('placas.jpg', paragraph=False)

# Itera sobre o resultado
for resultado in resultados:
    print(f'Texto encontrado:\n'
          f'\tPosição: {resultado[0]}\n'
          f'\tTexto: {resultado[1]}\n')
