# viewer.py

from flask import Flask, send_from_directory, render_template_string
import os

app = Flask(__name__)
SCREENSHOT_FOLDER = 'screenshots'

@app.route('/')
def index():
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

if __name__ == '__main__':
    app.run(debug=True, port=5000)
