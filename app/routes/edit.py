from flask import Flask, render_template, abort, request, url_for, flash, redirect
from app.routes import app
from connection import get_db_connection



@app.get("/<int:pizza_id>/edit/")
def get_edit(pizza_id):
    pizza = get_pizza_id(pizza_id)
    return render_template("edit.html", pizza=pizza)


@app.post("/<int:pizza_id>/edit/")
def post_edit(pizza_id):
    pizza = get_pizza_id(pizza_id)
    name = request.form["name"]
    ingredients = request.form["ingredients"]
    price = request.form["price"]
    if not name or len(name) < 4:
        flash("Name is not required!")
        return render_template("edit.html", pizza=pizza) 
    else:
        connection = get_db_connection()
        connection.execute("UPDATE pizza SET name = ?, ingredients = ?, price = ? WHERE id =?",  (name, ingredients, price, pizza_id))
        connection.commit()
        connection.close()
        return redirect(url_for("menu_page"))
    

@app.post("/<int:pizza_id>/delete/")
def pizza_delete(pizza_id):
    connection = get_db_connection()
    connection.execute("DELETE FROM pizza WHERE id =?", (pizza_id,))
    connection.commit()
    connection.close()
    return redirect(url_for("menu_page"))
    

def get_pizza_id(pizza_id):
    connection = get_db_connection()
    pizza = connection.execute("SELECT * FROM pizza WHERE id = ?", (pizza_id,)).fetchone()
    connection.close()
    return pizza
