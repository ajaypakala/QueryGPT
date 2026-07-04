"""
=========================================================
Helper Functions
=========================================================
"""

from datetime import datetime


def dataframe_to_csv(df):

    return df.to_csv(
        index=False
    ).encode("utf-8")


def report_filename():

    timestamp = datetime.now().strftime(

        "%Y%m%d_%H%M%S"

    )

    return f"QueryGPT_{timestamp}.pdf"


def csv_filename():

    timestamp = datetime.now().strftime(

        "%Y%m%d_%H%M%S"

    )

    return f"QueryGPT_{timestamp}.csv"