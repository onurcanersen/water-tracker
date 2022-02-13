from flask import render_template, current_app, redirect, url_for, request

def home_page():
    db = current_app.config["db"]
    if "add-glass" in request.form:
        db.create_log("200")
        return redirect(url_for("home_page"))
    elif "add-bottle" in request.form:
        db.create_log("500")
        return redirect(url_for("home_page"))
    elif "add-custom" in request.form:
        amount = request.form["amount"]
        db.create_log(amount)
        return redirect(url_for("home_page"))
    elif "save" in request.form:
        id = request.form["id"]
        new_amount = request.form["new-amount"]
        db.update_log(id, new_amount)
        return redirect(url_for("home_page"))
    elif "delete" in request.form:
        id = request.form["id"]
        db.delete_log(id)
        return redirect(url_for("home_page"))
    else:
        total = db.get_todays_total()
        logs = db.get_todays_logs()
        target = db.get_target()
        return render_template("home.html", total=total, logs=logs, target=target)

def statistics_page():
    db = current_app.config["db"]
    if "delete" in request.form:
        id = request.form["id"]
        db.delete_log(id)
        return redirect(url_for("statistics_page"))
    else:
        dates, amounts = db.get_dates_amounts()
        logs = db.get_logs()
        return render_template("statistics.html", dates=dates, amounts=amounts, logs=logs)
    
def settings_page():
    db = current_app.config["db"]
    if "save" in request.form:
        target = request.form["target"]
        db.update_target(target)
        return redirect(url_for("settings_page"))
    else:
        target = db.get_target()
        return render_template("settings.html", target=target)