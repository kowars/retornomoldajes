from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

# Load equipment data from CSV

equipos = []
with open('equipos.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    # Skip header line
    next(reader, None)
    for row in reader:
        # Each row has blank first and last columns
        if len(row) >= 4:
            familia = row[1].strip()
            codigo = row[2].strip()
            equipo = row[3].strip()
            equipos.append({'familia': familia, 'codigo': codigo, 'equipo': equipo})

# In-memory storage for return entries
retornos = []

@app.route('/')
def index():
    return render_template('index.html', equipos=equipos, retornos=retornos)

@app.route('/add', methods=['POST'])
def add_return():
    codigo = request.form['codigo']
    cantidad = request.form['cantidad']
    cliente = request.form['cliente']
    obra = request.form.get('obra', '')
    observaciones = request.form.get('observaciones', '')
    equipo = next((e['equipo'] for e in equipos if e['codigo'] == codigo), '')
    retornos.append({'cliente': cliente, 'obra': obra, 'codigo': codigo, 'equipo': equipo,
                    'cantidad': cantidad, 'observaciones': observaciones})
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
