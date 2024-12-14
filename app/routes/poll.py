from flask import Flask, render_template, request
from app.routes import app
from .poll_data import poll_data


filename = "data.txt"


@app.get("/poll/")
def poll_page():
    return render_template("poll.html", data=poll_data)


@app.post("/poll/")
def poll():
    vote = request.form.get("field")
    if vote:
        with open(filename, "a", encoding='utf-8') as out:
            out.write(vote + "\n")
    return render_template("poll.html", data=poll_data)


@app.get("/results/")
def get_results():
    with open(filename, "r", encoding='utf-8') as file:
        total_votes = {}
        data = file.read().split()

    for vote in data:
        total_votes[vote] = data.count(vote)
    
    formatted_votes = {}
    for vote, count in total_votes.items():
        formatted_name = vote.replace("_", " ")
        formatted_votes[formatted_name] = count

    return render_template("results.html", total_count=formatted_votes)
