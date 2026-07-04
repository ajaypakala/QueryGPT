"""
=========================================================
Query Executor
=========================================================
"""

import pandas as pd

from database.connection import get_connection


def execute_query(query):

    conn = get_connection()

    try:

        df = pd.read_sql(
            query,
            conn
        )

        conn.close()

        return True, df

    except Exception as e:

        conn.close()

        return False, str(e)