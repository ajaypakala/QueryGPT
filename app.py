"""
=========================================================
QueryGPT v2.0
Universal AI Database Analyst
=========================================================
"""

# =====================================================
# IMPORTS
# =====================================================

import streamlit as st
import pandas as pd
from reports.pdf_report import generate_pdf

from utils.helpers import report_filename

from database.uploader import save_database

from database.connection import (
    set_database,
    get_connection
)

from database.schema import (
    get_tables,
    get_table_data,
    get_columns,
    get_database_schema
)

from database.query_executor import (
    execute_query
)

from ai.ai_service import (
    generate_sql,
    explain_results
)

from visualization.charts import (
    auto_chart
)

from utils.helpers import (
    dataframe_to_csv
)

# =====================================================
# PAGE CONFIGURATION
# =====================================================

st.set_page_config(

    page_title="QueryGPT",

    page_icon="🗄️",

    layout="wide"

)

# =====================================================
# SESSION STATE
# =====================================================

if "database_loaded" not in st.session_state:

    st.session_state.database_loaded = False

if "generated_sql" not in st.session_state:

    st.session_state.generated_sql = ""

if "query_result" not in st.session_state:

    st.session_state.query_result = None

if "database_schema" not in st.session_state:

    st.session_state.database_schema = ""

if "uploaded_database" not in st.session_state:

    st.session_state.uploaded_database = ""

# =====================================================
# TITLE
# =====================================================

st.title("🗄️ QueryGPT")

st.caption(
    "Universal AI Database Analyst"
)

# =====================================================
# DATABASE UPLOAD
# =====================================================

st.divider()

st.header("📂 Upload SQLite Database")

uploaded_db = st.file_uploader(

    "Choose SQLite Database",

    type=[

        "db",

        "sqlite",

        "sqlite3"

    ]

)

if uploaded_db is not None:

    filepath = save_database(

        uploaded_db

    )

    set_database(

        filepath

    )

    st.session_state.database_loaded = True

    st.session_state.uploaded_database = uploaded_db.name

    st.success(

        f"Loaded : {uploaded_db.name}"

    )

else:

    st.info(

        "Upload any SQLite database to continue."

    )

    st.stop()

# =====================================================
# LOAD DATABASE SCHEMA
# =====================================================

if st.session_state.database_schema == "":

    st.session_state.database_schema = (

        get_database_schema()

    )

# =====================================================
# SIDEBAR
# =====================================================

st.sidebar.title("Database Explorer")

st.sidebar.success(

    st.session_state.uploaded_database

)

tables = get_tables()

selected_table = st.sidebar.selectbox(

    "Select Table",

    tables

)

# =====================================================
# TABLE INFORMATION
# =====================================================

df = get_table_data(

    selected_table

)

columns = get_columns(

    selected_table

)

st.header(

    f"📋 {selected_table}"

)

col1, col2 = st.columns(2)

with col1:

    st.metric(

        "Rows",

        len(df)

    )

with col2:

    st.metric(

        "Columns",

        len(df.columns)

    )

# =====================================================
# COLUMN INFORMATION
# =====================================================

st.subheader(

    "Column Information"

)

for column in columns:

    st.write(

        f"**{column[1]}** ({column[2]})"

    )

# =====================================================
# DATA PREVIEW
# =====================================================

st.subheader(

    "Preview"

)

st.dataframe(

    df,

    use_container_width=True

)

st.divider()


# =====================================================
# AI SQL GENERATOR
# =====================================================

st.header("🤖 AI SQL Generator")

question = st.text_input(

    "Ask anything about your database",

    placeholder="Example: Show top 10 customers"

)

col1, col2 = st.columns([1,4])

with col1:

    generate = st.button(

        "Generate SQL",

        use_container_width=True

    )

with col2:

    clear = st.button(

        "Clear",

        use_container_width=True

    )

if clear:

    st.session_state.generated_sql = ""

    st.session_state.query_result = None

# =====================================================
# GENERATE SQL
# =====================================================

if generate:

    if question.strip() == "":

        st.warning(

            "Please enter a question."

        )

    else:

        with st.spinner(

            "Generating SQL..."

        ):

            sql = generate_sql(

                schema=st.session_state.database_schema,

                question=question

            )

        st.session_state.generated_sql = sql

# =====================================================
# GENERATED SQL
# =====================================================

if st.session_state.generated_sql != "":

    st.subheader(

        "Generated SQL"

    )

    st.code(

        st.session_state.generated_sql,

        language="sql"

    )

# =====================================================
# EXECUTE SQL
# =====================================================

if st.session_state.generated_sql != "":

    with st.spinner(

        "Executing Query..."

    ):

        success, result = execute_query(

            st.session_state.generated_sql

        )

    if success:

        st.session_state.query_result = result

    else:

        st.error(result)

# =====================================================
# DISPLAY RESULT
# =====================================================

if st.session_state.query_result is not None:

    st.subheader(

        "Query Result"

    )

    st.dataframe(

        st.session_state.query_result,

        use_container_width=True

    )

st.divider()


# =====================================================
# KPI DASHBOARD
# =====================================================

if st.session_state.query_result is not None:

    result = st.session_state.query_result

    st.header("📊 Query Dashboard")

    c1, c2, c3 = st.columns(3)

    with c1:

        st.metric(

            "Rows Returned",

            len(result)

        )

    with c2:

        st.metric(

            "Columns",

            len(result.columns)

        )

    with c3:

        numeric_cols = result.select_dtypes(include="number").columns

        if len(numeric_cols):

            st.metric(

                "Numeric Columns",

                len(numeric_cols)

            )

        else:

            st.metric(

                "Numeric Columns",

                0

            )

# =====================================================
# AUTO CHART
# =====================================================

if st.session_state.query_result is not None:

    result = st.session_state.query_result

    st.header("📈 Visualization")

    try:

        fig = auto_chart(result)

        if fig is not None:

            st.plotly_chart(

                fig,

                use_container_width=True

            )

        else:

            st.info(

                "No suitable visualization available."

            )

    except Exception as e:

        st.warning(

            f"Chart Error: {e}"

        )

# =====================================================
# AI BUSINESS INSIGHTS
# =====================================================

if st.session_state.query_result is not None:

    result = st.session_state.query_result

    st.header("🧠 AI Business Insights")

    with st.spinner(

        "Analyzing Result..."

    ):

        insights = explain_results(

            question,

            result

        )

    st.markdown(

        insights

    )

# =====================================================
# DOWNLOADS
# =====================================================

if st.session_state.query_result is not None:

    result = st.session_state.query_result

    st.header("⬇ Download")

    csv = dataframe_to_csv(result)

    st.download_button(

        label="Download CSV",

        data=csv,

        file_name="query_result.csv",

        mime="text/csv"

    )

if st.session_state.query_result is not None:

    result = st.session_state.query_result

    pdf_name = report_filename()

    generate_pdf(

        pdf_name,

        question,

        st.session_state.generated_sql,

        result,

        insights

    )

# =====================================================
# DATABASE SCHEMA
# =====================================================

with st.expander(

    "📚 Database Schema"

):

    st.code(

        st.session_state.database_schema

    )

st.divider()


# ==========================================================
# SIDEBAR DATABASE INFORMATION
# ==========================================================

st.sidebar.divider()

st.sidebar.subheader("📊 Database Information")

try:

    db_info = get_database_info()

    st.sidebar.metric(
        "Tables",
        db_info["tables"]
    )

    st.sidebar.metric(
        "Total Rows",
        db_info["rows"]
    )

    st.sidebar.metric(
        "Database Size",
        db_info["size"]
    )

except Exception:

    pass

# ==========================================================
# QUERY HISTORY
# ==========================================================

if "query_history" not in st.session_state:

    st.session_state.query_history = []

if (
    question
    and question not in st.session_state.query_history
):

    st.session_state.query_history.append(question)

st.sidebar.divider()

st.sidebar.subheader("🕒 Recent Questions")

for q in st.session_state.query_history[-10:]:

    st.sidebar.write("•", q)

# ==========================================================
# APP STATISTICS
# ==========================================================

st.sidebar.divider()

st.sidebar.subheader("📈 Session")

st.sidebar.write(
    f"Questions Asked : {len(st.session_state.query_history)}"
)

if st.session_state.query_result is not None:

    st.sidebar.write(
        f"Last Query Rows : {len(st.session_state.query_result)}"
    )

# ==========================================================
# ABOUT
# ==========================================================

st.sidebar.divider()

st.sidebar.info(
"""
### QueryGPT v2.0

Universal AI Database Analyst

Features

✅ Upload Any SQLite Database

✅ Automatic Schema Detection

✅ AI SQL Generator

✅ SQL Execution

✅ Charts

✅ AI Insights

✅ CSV Export
"""
)

# ==========================================================
# FOOTER
# ==========================================================

st.divider()

st.caption(
    "QueryGPT v2.0 | Universal AI Database Analyst | Powered by Gemini 2.5 Flash"
)