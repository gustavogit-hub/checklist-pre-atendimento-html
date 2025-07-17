from flask import Flask, request, render_template

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

    # Enviando o nome do cliente para a página de sucesso
    return render_template("sucesso.html", cliente=cliente)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

