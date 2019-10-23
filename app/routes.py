from flask import Flask, render_template


def load(app: Flask) -> Flask:
    @app.route("/")
    def home():
        return render_template("home.html")

    return app
