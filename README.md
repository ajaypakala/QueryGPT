# 🗄️ BridgeSQL – Natural Language Database Assistant

BridgeSQL is an AI-powered SQL analytics application that allows users to upload any SQLite database and interact with it using natural language. The application automatically discovers the database schema, generates SQL queries using Google's Gemini AI, executes them, visualizes the results, and provides AI-generated business insights.

---

## 🚀 Features

- 📂 Upload any SQLite database (`.db`, `.sqlite`, `.sqlite3`)
- 🔍 Automatic database schema detection
- 🤖 Natural Language → SQL generation using Gemini AI
- ⚡ Automatic SQL execution
- 📊 Interactive data visualization using Plotly
- 🧠 AI-generated business insights
- 📈 Database explorer
- 📋 Query result preview
- 📥 Export query results to CSV
- 📄 Generate professional PDF reports
- 🌙 Modern Streamlit interface

---

# Application Workflow

```
Upload SQLite Database
          │
          ▼
Automatic Schema Detection
          │
          ▼
Ask Questions in English
          │
          ▼
Gemini AI Generates SQL
          │
          ▼
Execute SQL Query
          │
          ▼
Display Results
          │
          ▼
Automatic Charts
          │
          ▼
Business Insights
          │
          ▼
Download CSV / PDF
```

---

# Project Structure

```
QueryGPT/

│── app.py
│── config.py
│── requirements.txt
│── README.md
│── .gitignore
│── .env.example

├── ai/
│   └── ai_service.py

├── database/
│   ├── uploader.py
│   ├── connection.py
│   ├── schema.py
│   ├── database_info.py
│   └── query_executor.py

├── visualization/
│   └── charts.py

├── reports/
│   └── pdf_report.py

├── utils/
│   └── helpers.py

├── uploads/

```

---

# Technologies Used

### Programming Language

- Python 3.11

### Framework

- Streamlit

### Database

- SQLite

### AI

- Google Gemini 2.5 Flash

### Data Processing

- Pandas

### Visualization

- Plotly

### Report Generation

- ReportLab

---

# Installation

Clone the repository

```bash
git clone https://github.com/ajaypakala/QueryGPT.git

cd QueryGPT
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the environment

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# Configure Gemini API

Create a `.env` file

```
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

or use Streamlit Secrets when deploying.

---

# Run the Application

```bash
streamlit run app.py
```

---

# Supported Database Formats

- SQLite (.db)
- SQLite (.sqlite)
- SQLite (.sqlite3)

---

# Example Questions

```
Show top 10 customers.

List employees with salary above 50000.

Show total sales by country.

Which products generated the highest revenue?

Display monthly sales trend.

Find customers from Hyderabad.

Show average salary by department.

List orders placed last month.

Who are the top 5 suppliers?

Find products with low inventory.
```

---


# Future Enhancements

- PostgreSQL Support
- MySQL Support
- SQL Server Support
- Database Relationship Visualization
- AI Dashboard Generation
- Query History
- Saved Queries
- Authentication
- Multi-user Support
- Cloud Deployment

---

# Highlights

This project demonstrates experience in:

- Artificial Intelligence
- Natural Language Processing
- Prompt Engineering
- SQL Query Generation
- Database Management
- Data Visualization
- Business Intelligence
- Python Development
- Streamlit Application Development
- Report Automation

---

# Author

**Ajaybabu Pakala**

GitHub

https://github.com/ajaypakala

LinkedIn

www.linkedin.com/in/pakala-ajaybabu

---

# License

This project is released under the MIT License.

---


# App link

https://querygpt-ajaypakala.streamlit.app/
