import pdfkit
import base64
import string


def converte_imagem_base64(caminho_imagem: str) -> str:
    """
    Converte imagem para Base64
    :param caminho_imagem: Diretório da imagem
    :return: imagem convertida para Base64
    """
    with open(caminho_imagem, 'rb') as imagem:
        imagem_convertida = base64.b64encode(imagem.read()).decode()

    return imagem_convertida


def substitui_variaveis_html(caminho_html: str) -> str:
    """
    Substitui as variáveis no template HTML
    :param caminho_html: Caminho do arquivo HTML
    :return: HTML com variáveis substituídas
    """
    with open(caminho_html, 'r') as arquivo_html:
        template = string.Template(arquivo_html.read())
        imagem_base64 = converte_imagem_base64('assets/logo.png')
        grafico_base64 = converte_imagem_base64('assets/grafico.png')

        return template.substitute(
            logo_base64=imagem_base64,
            grafico_base64=grafico_base64
        )


if __name__ == '__main__':
    #
    html = substitui_variaveis_html('assets/pagina.html')

    pdfkit.from_string(
        input=html,
        output_path='saida.pdf',
        css='assets/estilos.css',
        options={
            'page-size': 'A4',
            'margin-top': '0.75in',
            'margin-right': '0.75in',
            'margin-bottom': '0.75in',
            'margin-left': '0.75in',
            'encoding': "UTF-8"
        }
    )
