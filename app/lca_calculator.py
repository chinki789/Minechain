from flask import Blueprint, render_template, request

lca_bp = Blueprint("lca", __name__)

@lca_bp.route("/lca", methods=["GET", "POST"])
def lca_calculator():
    result = None
    if request.method == "POST":
        diesel = float(request.form["diesel"])
        electricity = float(request.form["electricity"])
        emissions = (diesel * 2.68) + (electricity * 0.82)
        result = round(emissions, 2)
    return render_template("lca_calculator.html", result=result)
