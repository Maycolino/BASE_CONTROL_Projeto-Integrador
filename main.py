import json
from flask import Flask, render_template, request, jsonify, redirect

app = Flask(__name__, static_url_path='/static')

### dados ficticios somente para teste:

listaDeServicos = [
    {
        'matricula': '20250',
        'colaborador': 'João Silva',
        'placa': 'DLC2581',
        'retirada': '30/09/2023',
        'hora_retirada': '10:00',
        'devolucao': '01/10/2023',
        'hora_devolucao': '11:00',
        'kms_rodados': '100',
        'despesa_combustivel': '50.00',
        'despesa_pane': '10.00',
        'despesa_pedagio': '5.00',
        'multa': '0.00',
        'observacoes': 'Nenhuma observação'
    },
    {
        'matricula': '20251',
        'colaborador': 'Maria Santos',
        'placa': 'RTY4127',
        'retirada': '28/09/2023',
        'hora_retirada': '12:00',
        'devolucao': '29/09/2023',
        'hora_devolucao': '14:00',
        'kms_rodados': '150',
        'despesa_combustivel': '70.00',
        'despesa_pane': '5.00',
        'despesa_pedagio': '8.00',
        'multa': '20.00',
        'observacoes': 'Arranhão na lateral esquerda'
    },{
        'matricula': '20252',
        'colaborador': 'Pedro Alves',
        'placa': 'AWE5337',
        'retirada': '25/09/2023',
        'hora_retirada': '09:30',
        'devolucao': '26/09/2023',
        'hora_devolucao': '10:45',
        'kms_rodados': '120',
        'despesa_combustivel': '60.00',
        'despesa_pane': '15.00',
        'despesa_pedagio': '10.00',
        'multa': '5.00',
        'observacoes': 'Cheiro de queimado no motor'
    },
    {
        'matricula': '20253',
        'colaborador': 'Ana Oliveira',
        'placa': 'GHI0915',
        'retirada': '23/09/2023',
        'hora_retirada': '08:00',
        'devolucao': '30/09/2023',
        'hora_devolucao': '09:30',
        'kms_rodados': '80',
        'despesa_combustivel': '40.00',
        'despesa_pane': '8.00',
        'despesa_pedagio': '7.00',
        'multa': '0.00',
        'observacoes': 'Risco no para-choque traseiro'
    }
    # Adicione mais 8 entradas com dados fictícios aqui...
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'GET':
        return render_template("registro.html")
    if request.method == 'POST':
        registro_data = {
            'matricula': request.form['matricula'],
            'colaborador': request.form['colaborador'],
            'placa': request.form['placa'],
            'retirada': request.form['retirada'],
            'hora_retirada': request.form['hora_retirada'],
            'devolucao': request.form['devolucao'],
            'hora_devolucao': request.form['hora_devolucao'],
            'kms_rodados': request.form['kms_rodados'],
            'despesa_combustivel': request.form['despesa_combustivel'],
            'despesa_pane': request.form['despesa_pane'],
            'despesa_pedagio': request.form['despesa_pedagio'],
            'multa': request.form['multa'],
            'observacoes': request.form['observacoes']
        }

        listaDeServicos.append(registro_data)

        return redirect("/", code=302)


@app.route('/acompanhar', methods=['GET'])
def acompanhar():
    return render_template("acompanhar.html", dados=listaDeServicos)

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000)

