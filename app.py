from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/carga_bdvectorial')
def carga_bdvectorial():
    return render_template('carga_bdvectorial.html')

@app.route('/carga_bdrelacional')
def carga_bdrelacional():
    return render_template('carga_bdrelacional.html')

@app.route('/chatbot', methods=['GET', 'POST'])
def chatbot():
    mensaje = ''
    if request.method == 'POST':
        mensaje = request.form['mensaje']
    return render_template('chatbot.html', mensaje=mensaje)

@app.route('/estadisticas')
def estadisticas():
    return render_template('estadisticas.html')

if __name__ == '__main__':
    app.run(debug=True)