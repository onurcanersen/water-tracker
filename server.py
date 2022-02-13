from flask import Flask
import views
import os

from database import Database

def create_app():
    app = Flask(__name__)
    app.config.from_object("settings")

    home_path = os.path.expanduser("~")
    db = Database(os.path.join(home_path, "log.db"))
    app.config["db"] = db

    app.add_url_rule("/", view_func=views.home_page, methods=["GET", "POST"])
    app.add_url_rule("/statistics", view_func=views.statistics_page, methods=["GET", "POST"])
    app.add_url_rule("/settings", view_func=views.settings_page, methods=["GET", "POST"])

    return app

if __name__ == "__main__":
    app = create_app()
    port = app.config.get("PORT", 5000)
    app.run(host="0.0.0.0", port=port)