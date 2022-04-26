import pandas
import plotly.express as px
from datetime import datetime

if __name__ == '__main__':
    df = pandas.read_csv("BGE_8681551752_HDF_26_04_2022.csv", parse_dates=['Date and Time'])
    df.info()

    df['Date and Time'] = pandas.to_datetime(df['Date and Time'], utc=True)
    # df.info()

    today = df[df['Date and Time'].dt.date == datetime(2022, 4, 1).date()]
    print(today)
    # april_df = df[df["Date and Time"]]
    fig = px.bar(today, x="Date and Time", y="Interval Value", title='Usage', color='Date and Time'
                 , color_discrete_map={
            "2022-04-01 00:00:00+00:00": "red",
            "2022-04-01 00:30:00+00:00": "red",
            "2022-04-01 01:00:00+00:00": "red"})
    fig.show()
