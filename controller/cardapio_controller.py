from flask import render_template
from model.bd import cardapio_salgado, cardapio_doce

def mostrar_salgadas():
    lista = [f"{item.id} - {item.descricao} - {item.preco}" for item in cardapio_salgado]
    return render_template("salgadas.html", cardapio=cardapio_salgado)

def mostrar_doces():
    lista = [f"{item.id} - {item.descricao} - {item.preco}" for item in cardapio_doce]
    return render_template("doces.html", cardapio=cardapio_doce)

def mostrar_todos_ordenados_mais_barato():
    todos = cardapio_salgado + cardapio_doce
    ordenados = sorted(todos, key=lambda x: x.preco)  
    return render_template("todos.html", cardapio=ordenados)

def mostrar_todos_ordenados_mais_caro():
    todos = cardapio_salgado + cardapio_doce
    ordenados = sorted(todos, key=lambda x: x.preco, reverse=True)  
    return render_template("todos.html", cardapio=ordenados)

def editar_item(cardapio, item_id, nova_descricao, novo_preco):
    for item in cardapio:
        if item.id == item_id:
            item.descricao = nova_descricao
            item.preco = novo_preco
            return True
    return False

def deletar_item(cardapio, item_id):
    for i, item in enumerate(cardapio):
        if item.id == item_id:
            del cardapio[i]
            return True
    return False

def adicionar_item(cardapio, id, descricao, preco):
    novo_item = type(cardapio[0])(id, descricao, preco)  # Cria um novo item do mesmo tipo que os existentes
    cardapio.append(novo_item)

def buscar_item_por_id(cardapio, item_id):
    for item in cardapio:
        if item.id == item_id:
            return item
    return None


