from flask import Flask, render_template, request
import random
import json

app = Flask(__name__)


# Load quotes from JSON file
def load_quotes():
    with open("data/quotes.json", "r") as file:
        return json.load(file)


@app.route("/")
def index():
    quotes = load_quotes()
    quote = random.choice(quotes)
    return render_template("index.html", quote=quote)


@app.route("/add", methods=["GET", "POST"])
def add_quote():
    if request.method == "POST":
        new_quote = request.form.get("quote")
        if new_quote:
            quotes = load_quotes()
            quotes.append(new_quote)
            with open("data/quotes.json", "w") as file:
                json.dump(quotes, file, indent=4)
            return render_template("add.html", message="Quote added successfully!")
    return render_template("add.html", message=None)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=2222)
