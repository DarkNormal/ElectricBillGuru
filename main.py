import pandas
import plotly.express as px


if __name__ == '__main__':
    df = pandas.read_csv("BGE_8681551752_HDF_13_04_2022.csv")
    fig = px.line(df, x="Date and Time", y="Interval Value", title='Usage')
    fig.show()
