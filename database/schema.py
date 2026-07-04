"""
=========================================================
Database Schema
=========================================================
"""

import pandas as pd

from database.connection import get_connection


def get_tables():

    conn = get_connection()

    query = """
    SELECT name
    FROM sqlite_master
    WHERE type='table'
    ORDER BY name;
    """

    tables = pd.read_sql(
        query,
        conn
    )

    conn.close()

    return tables["name"].tolist()


def get_table_data(table):

    conn = get_connection()

    df = pd.read_sql(
        f"SELECT * FROM {table}",
        conn
    )

    conn.close()

    return df


def get_columns(table):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        f"PRAGMA table_info({table})"
    )

    rows = cursor.fetchall()

    conn.close()

    return rows


def get_database_schema():

    conn = get_connection()

    cursor = conn.cursor()

    schema = ""

    tables = cursor.execute(

        """
        SELECT name
        FROM sqlite_master
        WHERE type='table'
        """

    ).fetchall()

    for table in tables:

        table_name = table[0]

        schema += f"\nTABLE : {table_name}\n"

        cols = cursor.execute(

            f"PRAGMA table_info({table_name})"

        ).fetchall()

        for col in cols:

            schema += f"{col[1]} ({col[2]})\n"

    conn.close()

    return schema