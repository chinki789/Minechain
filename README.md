⛏️ MINECHAIN – Blockchain-Inspired Supply Chain Tracking + LCA Dashboard
📌 Problem Statement

Traditional mining supply chains lack transparency, traceability, and environmental accountability.
Companies struggle to track batches, monitor suppliers, calculate carbon footprint, and generate professional sustainability reports.

There’s a need for a simple, smart, and automated system that brings clarity and trust into mining operations.

💡 Solution

MineChain is a lightweight, blockchain-inspired dashboard that lets users:

Track mines, suppliers, and mineral batches

Calculate Life Cycle Assessment (LCA) metrics

View supply-chain progress in real-time

Export clean, professional PDF reports

MineChain combines data analytics + clean UI to create a transparent and eco-focused mining ecosystem.

✨ Key Features

✅ Dashboard Overview — Mines, batches, suppliers, activities
✅ LCA Calculator — CO₂ emissions, energy use, transport impact
✅ Blockchain-Style Batch Tracking — Immutable-like record history
✅ PDF Report Generator — Tables, charts & alternating row colors
✅ Supply Chain Status Timeline — Extraction → Transport → Processing
✅ Clean UI — Easy to use, beginner-friendly, mobile responsive

🛠️ Tech Stack

Frontend: HTML, CSS, Jinja Templates
Backend: Python (Flask)
Database: SQLite
Reporting: ReportLab, Matplotlib
Deployment: Render
Version Control: GitHub

🚧 Challenges

Designing accurate LCA formulas for mining workflows

Creating clean PDF layouts using ReportLab

Managing file generation on cloud platforms like Render

Handling batch relationships in a simple but traceable manner

🚀 Future Scope

🔹 Add real blockchain ledger (Hyperledger / Ethereum)
🔹 Add AI-based LCA prediction
🔹 Real-time GPS tracking of trucks & suppliers
🔹 Multi-user roles (Admin / Supplier / Auditor)
🔹 Cloud database integration (PostgreSQL, Firebase)

⚡ How to Run
git clone https://github.com/chinki789/Minechain.git
cd Minechain
pip install -r requirements.txt
python main.py


For deployment on Render:

gunicorn main:app
