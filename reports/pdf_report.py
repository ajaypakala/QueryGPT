"""
=========================================================
QueryGPT v2.0
Professional PDF Report Generator
=========================================================
"""

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle
)

from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet


def generate_pdf(
        filename,
        question,
        sql,
        dataframe,
        insights
):

    styles = getSampleStyleSheet()

    doc = SimpleDocTemplate(filename)

    story = []

    # -----------------------------------------------------
    # Title
    # -----------------------------------------------------

    story.append(

        Paragraph(

            "<b>QueryGPT AI Analysis Report</b>",

            styles["Title"]

        )

    )

    story.append(Spacer(1, 20))

    # -----------------------------------------------------
    # Question
    # -----------------------------------------------------

    story.append(

        Paragraph(

            "<b>Business Question</b>",

            styles["Heading2"]

        )

    )

    story.append(

        Paragraph(

            question,

            styles["BodyText"]

        )

    )

    story.append(Spacer(1, 12))

    # -----------------------------------------------------
    # SQL
    # -----------------------------------------------------

    story.append(

        Paragraph(

            "<b>Generated SQL</b>",

            styles["Heading2"]

        )

    )

    story.append(

        Paragraph(

            f"<font face='Courier'>{sql}</font>",

            styles["Code"]

        )

    )

    story.append(Spacer(1, 12))

    # -----------------------------------------------------
    # Result Table
    # -----------------------------------------------------

    story.append(

        Paragraph(

            "<b>Query Result</b>",

            styles["Heading2"]

        )

    )

    data = [

        dataframe.columns.tolist()

    ]

    data.extend(

        dataframe.astype(str).values.tolist()

    )

    table = Table(data)

    table.setStyle(

        TableStyle(

            [

                ("BACKGROUND", (0,0), (-1,0), colors.darkblue),

                ("TEXTCOLOR", (0,0), (-1,0), colors.white),

                ("GRID", (0,0), (-1,-1), 0.5, colors.black),

                ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),

                ("BOTTOMPADDING", (0,0), (-1,0), 8),

                ("BACKGROUND", (0,1), (-1,-1), colors.beige),

            ]

        )

    )

    story.append(table)

    story.append(Spacer(1,20))

    # -----------------------------------------------------
    # AI Insights
    # -----------------------------------------------------

    story.append(

        Paragraph(

            "<b>AI Business Insights</b>",

            styles["Heading2"]

        )

    )

    story.append(

        Paragraph(

            insights.replace("\n","<br/>"),

            styles["BodyText"]

        )

    )

    doc.build(story)