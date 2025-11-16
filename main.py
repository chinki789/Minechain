from flask import Flask, render_template, request, send_file
from app import dashboard, lca_calculator, supply_chain, batch_registration, generate_report
import os

app = Flask(__name__)

# -------------------------------
# Routes for Dashboard & Pages
# -------------------------------

@app.route('/')
def home():
    return render_template('dashboard.html')

@app.route('/dashboard')
def show_dashboard():
    return render_template('dashboard.html')

@app.route('/lca_calculator', methods=['GET', 'POST'])
def show_lca_calculator():
    result = None
    if request.method == 'POST':
        # Get form data and calculate LCA
        input_data = request.form.to_dict()
        try:
            result = lca_calculator.calculate_lca(input_data)
        except Exception as e:
            result = f"Error: {e}"
    return render_template('lca_calculator.html', result=result)

@app.route('/supply_chain', methods=['GET', 'POST'])
def show_supply_chain():
    supply_data = None
    if request.method == 'POST':
        input_data = request.form.to_dict()
        try:
            supply_data = supply_chain.process_supply_chain(input_data)
        except Exception as e:
            supply_data = {"error": str(e)}
    return render_template('supply_chain.html', supply_data=supply_data)

@app.route('/batch_registration', methods=['GET', 'POST'])
def show_batch_registration():
    message = None
    if request.method == 'POST':
        input_data = request.form.to_dict()
        try:
            message = batch_registration.register_batch(input_data)
        except Exception as e:
            message = f"Error: {e}"
    return render_template('batch_registration.html', message=message)

@app.route('/generate_report', methods=['GET'])
def generate_report_pdf():
    # Example sample data (replace with real data from your app logic)
    sample_data = {
        "Dashboard": ["Item 1", "Item 2", "Item 3"],
        "Supply Chain": {"Supplier A": "100 units", "Supplier B": "200 units"},
        "LCA Calculator": {"CO2": "50 kg", "Water": "120 L"}
    }

    try:
        pdf_path = generate_report.generate_pdf_report(sample_data)
        return send_file(pdf_path, as_attachment=True)
    except Exception as e:
        return f"Error generating PDF: {e}"

# -------------------------------
# Run Flask App
# -------------------------------

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)

