from flask import Blueprint, render_template, request
import uuid

batch_bp = Blueprint("batch", __name__)
batches = []

@batch_bp.route("/batch-registration", methods=["GET", "POST"])
def batch_registration():
    qr_code = None
    if request.method == "POST":
        batch_id = str(uuid.uuid4())[:8]
        batches.append(batch_id)
        qr_code = f"https://minechain.com/batch/{batch_id}"
    return render_template("batch_registration.html", batches=batches, qr_code=qr_code)
