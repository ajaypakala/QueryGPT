"""
=========================================================
Database Upload Module
=========================================================
"""

import os
import shutil

UPLOAD_FOLDER = "uploads"

os.makedirs(
    UPLOAD_FOLDER,
    exist_ok=True
)


def save_database(uploaded_file):

    destination = os.path.join(
        UPLOAD_FOLDER,
        uploaded_file.name
    )

    with open(destination, "wb") as f:

        shutil.copyfileobj(
            uploaded_file,
            f
        )

    return destination


def remove_old_databases():

    for file in os.listdir(UPLOAD_FOLDER):

        path = os.path.join(
            UPLOAD_FOLDER,
            file
        )

        try:

            os.remove(path)

        except Exception:

            pass