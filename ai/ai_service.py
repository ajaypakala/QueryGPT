"""
=========================================================
QueryGPT v2.0
Universal AI Service
=========================================================
"""

import os
import streamlit as st
from dotenv import load_dotenv
from google import genai

# ==========================================================
# LOAD API KEY
# ==========================================================

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    try:
        API_KEY = st.secrets["GEMINI_API_KEY"]
    except Exception:
        API_KEY = None

if not API_KEY:
    raise ValueError(
        "GEMINI_API_KEY not found."
    )

client = genai.Client(api_key=API_KEY)

MODEL = "gemini-2.5-flash"

# ==========================================================
# INTERNAL GEMINI FUNCTION
# ==========================================================

def ask_gemini(prompt):

    try:

        response = client.models.generate_content(

            model=MODEL,

            contents=prompt

        )

        return response.text.strip()

    except Exception as e:

        return f"Gemini Error:\n\n{e}"


# ==========================================================
# GENERATE SQL
# ==========================================================

def generate_sql(schema, question):

    prompt = f"""
You are a Senior SQL Developer.

Your task is to generate SQL for ANY SQLite database.

DATABASE SCHEMA

{schema}

USER QUESTION

{question}

RULES

1. Return ONLY SQL.

2. Do NOT explain.

3. Do NOT use markdown.

4. Do NOT use ```sql.

5. Use ONLY tables from the schema.

6. Use valid SQLite syntax.

Return SQL only.
"""

    sql = ask_gemini(prompt)

    sql = (
        sql.replace("```sql", "")
        .replace("```", "")
        .strip()
    )

    return sql


# ==========================================================
# AI BUSINESS INSIGHTS
# ==========================================================

def explain_results(question, dataframe):

    data = dataframe.to_string(index=False)

    prompt = f"""
You are a Senior Business Analyst.

Business Question

{question}

Query Result

{data}

Generate

1. Executive Summary

2. Key Insights

3. Business Impact

4. Recommendations

Maximum 250 words.

Use Markdown.
"""

    return ask_gemini(prompt)


# ==========================================================
# EXECUTIVE SUMMARY
# ==========================================================

def executive_summary(dataframe):

    data = dataframe.to_string(index=False)

    prompt = f"""
Generate an Executive Summary.

Dataset

{data}

Maximum 200 words.

Include

• Overview

• Findings

• Risks

• Recommendations
"""

    return ask_gemini(prompt)


# ==========================================================
# EXPLAIN SQL
# ==========================================================

def explain_sql(sql):

    prompt = f"""
Explain this SQL query.

SQL

{sql}

Explain

• Tables

• Conditions

• Joins

• Output

Keep it simple.
"""

    return ask_gemini(prompt)


# ==========================================================
# SUGGEST CHART
# ==========================================================

def suggest_chart(dataframe):

    data = dataframe.head(20).to_string(index=False)

    prompt = f"""
Dataset

{data}

Suggest the BEST visualization.

Choose ONLY ONE.

Bar Chart

Line Chart

Pie Chart

Scatter Plot

Histogram

Return ONLY chart name.
"""

    chart = ask_gemini(prompt)

    return chart.strip()


# ==========================================================
# DATA SUMMARY
# ==========================================================

def summarize_database(schema):

    prompt = f"""
Database Schema

{schema}

Summarize

• Database Purpose

• Tables

• Relationships

• Business Domain

Maximum 150 words.
"""

    return ask_gemini(prompt)