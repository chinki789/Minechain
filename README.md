⚡ MineChain – Blockchain-Inspired Supply Chain & LCA Dashboard
📌 Problem Statement

Mining supply chains face challenges like poor traceability, manual record-keeping, lack of transparency, and difficulty generating standardized sustainability reports.
Companies need a digital system that tracks mine batches, suppliers, carbon emissions, and generates professional LCA reports automatically.

💡 Solution

MineChain is a lightweight blockchain-inspired dashboard that tracks mines, suppliers, product batches, and their life-cycle emissions.
It includes automatic PDF report generation, making sustainability reporting fast, accurate, and visually professional.

✨ Key Features

✅ Dashboard overview of mines, batches, and suppliers
✅ LCA (Life Cycle Assessment) emission calculations
✅ Real-time supply chain status tracking
✅ Professional PDF report generation
— Tables
— Charts
— Alternating row colors
— Auto-formatted headers
✅ Simple and clean Streamlit UI

🛠️ Tech Stack

Frontend / UI: Streamlit
Backend: Python
PDF Generation: ReportLab
Data Handling: Pandas
Deployment: Render

🚧 Challenges

🔹 Designing a clean PDF layout with tables and charts
🔹 Ensuring LCA calculations remain accurate across multiple batches
🔹 Managing state inside Streamlit
🔹 Render deployment configuration with Procfile & environment variables

🚀 Future Scope

🔹 Add blockchain hashing for tamper-proof batch verification
🔹 Integrate QR-based batch tracking
🔹 Add supplier scoring using ML
🔹 Multi-user login system with roles (Admin, Auditor, Supplier)

⚡ How to Run Locally
git clone https://github.com/chinki789/Minechain.git
cd Minechain
pip install -r requirements.txt
streamlit run main.py

