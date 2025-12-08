from flask import Flask, render_template
from controller import cardapio_controller
from controller import api_controller

app = Flask(__name__)

# Página inicial
@app.route("/")
def home():
    return render_template("index.html")

# Cardápios
@app.route("/salgadas")
def salgadas():
    return cardapio_controller.mostrar_salgadas()

@app.route("/doces")
def doces():
    return cardapio_controller.mostrar_doces()

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


app.add_url_rule("/whatsapp", "whatsapp", cardapio_controller.ir_whatsapp)
app.add_url_rule("/instagram", "instagram", cardapio_controller.ir_instagram)
app.add_url_rule("/tiktok", "tiktok", cardapio_controller.ir_tiktok)
app.add_url_rule("/facebook", "facebook", cardapio_controller.ir_facebook)


if __name__ == "__main__":
    app.run(debug=True)
