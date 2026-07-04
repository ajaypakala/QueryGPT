"""
=========================================================
Dynamic SQLite Connection
=========================================================
"""

import sqlite3

DATABASE_PATH = None


def set_database(path):

    global DATABASE_PATH

    DATABASE_PATH = path


def get_database():

    return DATABASE_PATH


def get_connection():

    if DATABASE_PATH is None:

        raise Exception(
            "No database selected."
        )

    conn = sqlite3.connect(
        DATABASE_PATH
    )

    conn.row_factory = sqlite3.Row

    return conn