# viewer.py

from flask import Flask, send_from_directory, render_template_string
import os

app = Flask(__name__)
# É uma boa prática definir o caminho da pasta de forma absoluta
# para evitar problemas de diretório de trabalho.
SCREENSHOT_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'screenshots')

# Cria a pasta se ela não existir (bom para o primeiro deploy)
if not os.path.exists(SCREENSHOT_FOLDER):
    os.makedirs(SCREENSHOT_FOLDER)

@app.route('/')
def index():
    # Adicionado um tratamento para caso a pasta esteja vazia
    if not os.path.exists(SCREENSHOT_FOLDER) or not os.listdir(SCREENSHOT_FOLDER):
        return "<h1>Nenhuma imagem encontrada na pasta 'screenshots'.</h1>"
        
    arquivos = sorted(os.listdir(SCREENSHOT_FOLDER), reverse=True)
    imagens_html = ''.join([f'<img src="/img/{nome}" width="500"><br>' for nome in arquivos])
    return render_template_string(f"""
    <html><body>
    <h1>Prints de Tela</h1>
    {imagens_html}
    </body></html>
    """)

@app.route('/img/<path:nome>')
def serve_img(nome):
    return send_from_directory(SCREENSHOT_FOLDER, nome)

# A parte 'if __name__ == "__main__":' foi removida.