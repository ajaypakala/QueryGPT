"""
=========================================================
Database Information
=========================================================
"""

import os

from database.connection import (
    get_connection,
    get_database
)


def get_database_info():

    conn = get_connection()

    cursor = conn.cursor()

    tables = cursor.execute(

        """
        SELECT name
        FROM sqlite_master
        WHERE type='table'
        """

    ).fetchall()

    total_rows = 0

    for table in tables:

        count = cursor.execute(

            f"SELECT COUNT(*) FROM {table[0]}"

        ).fetchone()[0]

        total_rows += count

    conn.close()

    path = get_database()

    size = round(

        os.path.getsize(path) / 1024,

        2

    )

    return {

        "tables": len(tables),

        "rows": total_rows,

        "size": f"{size} KB"

    }