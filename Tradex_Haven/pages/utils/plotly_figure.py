import plotly.graph_objects as go
import dateutil
import datetime
import numpy as np
import pandas_ta as pta



def plotly_table(dataframe):
    headerColor = '#0078ff'    # Header background color
    rowEvenColor = '#f8fafd'   # Even row color
    rowOddColor = '#e1e1e1'    # Odd row color

    fig = go.Figure(data=[go.Table(
        # Header styling
        header=dict(
            values=["<b>{}</b>".format(i) for i in dataframe.columns],
            fill_color=headerColor,
            align='center',
            font=dict(color='white', size=14),
            height=35
        ),
        # Cell styling
        cells=dict(
            values=[dataframe.index.tolist(), dataframe.iloc[:, 0].tolist()],
            fill_color=[[rowOddColor, rowEvenColor] * (len(dataframe) // 2 + 1)],
            align='left',
            font=dict(color='black', size=14),
            height=30  # Cell height
        )
    )])

    # Dynamically adjust height based on the row count
    fig.update_layout(
        height=35 + (len(dataframe) * 30),  # Header height + dynamic row height
        margin=dict(l=0, r=0, t=0, b=0),    # Remove unnecessary margins
        paper_bgcolor='white'
    )
    return fig

def plotly_table_for_days(dataframe):
    headerColor = '#0078ff'    # Header background color
    rowEvenColor = '#f8fafd'   # Even row color
    rowOddColor = '#e1e1e1'    # Odd row color

    # Reset index to include the datetime as a column
    dataframe = dataframe.reset_index()  
    dataframe = dataframe.rename(columns={'index': 'Date'})  # Rename index column to 'Date'

    # Reorder columns: Date first, then Open, High, Low, Close, Adj Close, Volume
    ordered_columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']
    dataframe = dataframe[ordered_columns]

    # Prepare cell values for all columns
    cell_values = [dataframe[col].tolist() for col in dataframe.columns]

    fig = go.Figure(data=[go.Table(
        # Header styling
        header=dict(
            values=["<b>{}</b>".format(col) for col in dataframe.columns],  # Include 'Date' in headers
            fill_color=headerColor,
            align='center',
            font=dict(color='white', size=14),
            height=35
        ),
        # Cell styling
        cells=dict(
            values=cell_values,  
            fill_color=[[rowOddColor, rowEvenColor] * (len(dataframe) // 2 + 1)],
            align='left',
            font=dict(color='black', size=14),
            height=30  # Cell height
        )
    )])

    # Dynamically adjust height based on the row count
    fig.update_layout(
        height=35 + (len(dataframe) * 30),  # Header height + dynamic row height
        margin=dict(l=0, r=0, t=0, b=0),    # Remove unnecessary margins
        paper_bgcolor='white'
    )
    return fig

