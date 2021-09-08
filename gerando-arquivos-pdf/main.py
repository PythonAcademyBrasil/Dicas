import pdfkit

# Converte o HTML em PDF utilizando o pdfkit
pdfkit.from_file(
    input='assets/pagina.html',
    output_path='saida.pdf',
    css='assets/estilos.css',
    options={
        'page-size': 'A4',
        'margin-top': '0.5in',
        'margin-right': '0.5in',
        'margin-bottom': '0.5in',
        'margin-left': '0.5in',
        'encoding': 'UTF-8'
    }
)
