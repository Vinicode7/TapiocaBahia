from flask import Flask, render_template
from controller import cardapio_controller
from controller import api_controller
from model.bd import cardapio_salgado, cardapio_doce, cardapio_bahia, cardapio_bebidas


app = Flask(__name__,template_folder='view')

# Página inicial
@app.route("/")
def home():
    return render_template("principal.html")

# Cardápios
@app.route("/salgadas" )
def salgadas():
    return render_template(
        "salgadas.html",
        cardapio=cardapio_salgado
    )

@app.route("/doces")
def doces():
    return render_template(
        "doces.html",
        cardapio=cardapio_doce
    )


@app.route("/bebidas")
def bebidas():
    return render_template(
        "bebidas.html",
        cardapio=cardapio_bebidas
    )

@app.route("/bahia")
def bahia():
    return render_template(
        "bahia.html",
        cardapio=cardapio_bahia
    )

@app.route("/sobrenos")
def sobrenos():
    return render_template("sobrenos.html")


@app.route("/todos/mais_barato")
def todos_mais_barato():
    return cardapio_controller.mostrar_todos_ordenados_mais_barato()

@app.route("/todos/mais_caro")
def todos_mais_caro():
    return cardapio_controller.mostrar_todos_ordenados_mais_caro()

# Redes sociais e WhatsApp
@app.route("/whatsapp")
def whatsapp():
    return cardapio_controller.ir_whatsapp()

@app.route("/instagram")
def instagram():
    return cardapio_controller.ir_instagram()

@app.route("/tiktok")
def tiktok():
    return cardapio_controller.ir_tiktok()

@app.route("/facebook")
def facebook():
    return cardapio_controller.ir_facebook()


if __name__ == "__main__":
    app.run(debug=True)
