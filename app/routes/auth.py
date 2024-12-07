from flask import render_template, request
from flask import Flask, render_template, request, redirect, url_for
from app.routes import app
from app.models import (
    Session,
)
from sqlalchemy import select
from datetime import datetime
from .pizza import get_all_pizzas


@app.post("/login/")
def login():
    username = request.form.get("username")
    if username == "admin":
        return redirect(url_for("admin_page"))
    return redirect(url_for("home_page"))


@app.get("/admin/")
def admin_page():
    pizzas = get_all_pizzas()
    context = {
        "back_button": "Повернутися на головну сторінку",
        "pizzas": pizzas
    }
    return render_template("admin.html", **context)
