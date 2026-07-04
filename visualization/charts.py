"""
=========================================================
QueryGPT v2.0
Automatic Chart Generator
=========================================================
"""

import pandas as pd
import plotly.express as px


def auto_chart(df):

    """
    Automatically chooses the best chart.
    """

    if df is None:

        return None

    if len(df.columns) < 2:

        return None

    numeric = df.select_dtypes(include="number").columns.tolist()

    categorical = df.select_dtypes(
        exclude="number"
    ).columns.tolist()

    datetime_cols = []

    for col in df.columns:

        try:

            pd.to_datetime(df[col])

            datetime_cols.append(col)

        except Exception:

            pass

    # ---------------------------------------------
    # Date + Numeric
    # ---------------------------------------------

    if len(datetime_cols) and len(numeric):

        return px.line(

            df,

            x=datetime_cols[0],

            y=numeric[0],

            markers=True,

            title=f"{numeric[0]} Over Time"

        )

    # ---------------------------------------------
    # Category + Numeric
    # ---------------------------------------------

    if len(categorical) and len(numeric):

        return px.bar(

            df,

            x=categorical[0],

            y=numeric[0],

            text=numeric[0],

            title=f"{numeric[0]} by {categorical[0]}"

        )

    # ---------------------------------------------
    # Two Numeric Columns
    # ---------------------------------------------

    if len(numeric) >= 2:

        return px.scatter(

            df,

            x=numeric[0],

            y=numeric[1],

            title="Scatter Plot"

        )

    # ---------------------------------------------
    # One Numeric Column
    # ---------------------------------------------

    if len(numeric) == 1:

        return px.histogram(

            df,

            x=numeric[0],

            title=f"{numeric[0]} Distribution"

        )

    return None