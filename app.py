from flask import Flask, render_template, request

app = Flask(__name__)

frutas =[]

@app.route('/', methods=["GET","POST"])
def principal():
	# frutas = ['melão', 'melancia']
	fruta = request.form.get('fruta')
	if request.method == 'POST':
		frutas.append(fruta)
	return render_template("index.html", frutas=frutas)

@app.route('/sobre')
def sobre():
	diario = {"fulano":6.0,
			  "sicrano":5.0,
			  "beltrano":4.0
			 }
	return render_template("sobre.html", diario=diario)

app.run(debug=True)