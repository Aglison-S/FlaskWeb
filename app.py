from flask import Flask, render_template, request

app = Flask(__name__)

nomes = []
registros = []

@app.route('/', methods=["GET","POST"])
def principal():
	# frutas = ['melão', 'melancia']
	nome = request.form.get('nome')
	if request.method == 'POST':
		nomes.append(nome)
	return render_template("index.html", nomes=nomes)

@app.route('/sobre', methods=["GET","POST"])
def sobre():
	# diario = {"João":6.0,
	# 		  "Paulo":5.0,
	# 		  "José":4.0
	# 		 }

	aluno = request.form.get('aluno')
	nota = request.form.get('nota')

	if request.method == 'POST':
		registros.append({"aluno":aluno, "nota":nota})
	return render_template("sobre.html", registros=registros)

app.run(debug=True)