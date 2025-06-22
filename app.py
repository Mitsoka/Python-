from flask import Flask, render_template, request, url_for, redirect
from db import db
from models import Tarefas

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///banco.db'
db.init_app(app)

@app.route("/")
def home():
    trf = Tarefas.query.all()
    return render_template("hoe.html", tarefas=trf)

@app.route("/registrar", methods=["GET", "POST"])
def registrar():
    if request.method == "POST":
        tarefa = request.form.get("tarefa")
        nv_trf = Tarefas(tarefa=tarefa)
        db.session.add(nv_trf)
        db.session.commit()
    return render_template("registrar.html")

@app.route("/editar/<int:id>", methods=["GET", "POST"])
def editar(id):
    trf = Tarefas.query.filter_by(id=id).first()
    if request.method == "POST":
        tarefa = request.form.get('tarefa')
        trf.tarefa = tarefa
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("editar.html", tarefa=trf)

@app.route("/deletar/<int:id>")
def deletar(id):
    trf = Tarefas.query.filter_by(id=id).first()
    db.session.delete(trf)
    db.session.commit()
    return redirect(url_for('home'))
    
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)