from flask import Blueprint, render_template, request

supply_bp = Blueprint("supply", __name__)
ledger = []

@supply_bp.route("/supply-chain", methods=["GET", "POST"])
def supply_chain():
    if request.method == "POST":
        stage = request.form["stage"]
        details = request.form["details"]
        ledger.append({"stage": stage, "details": details})
    return render_template("supply_chain.html", ledger=ledger)
