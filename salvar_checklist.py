from flask import Flask, request, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("checklist.html")

@app.route('/salvar', methods=['POST'])
def salvar():
    cliente = request.form.get('cliente')
    problema = request.form.get('problema')

    with open("checklist_registros.txt", "a", encoding="utf-8") as f:
        f.write(f"Cliente: {cliente}\nProblema: {problema}\n{'-'*40}\n")

    return render_template("sucesso.html", cliente=cliente)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
