from sjvisualizer import Canvas
from sjvisualizer import DataHandler
from sjvisualizer import BarRace
from sjvisualizer import Date
from sjvisualizer import StaticText
import time
import json

def main(duration = 1.0, fps = 60):
    number_of_frames = duration * fps * 60
    df = DataHandler.DataHandler(excel_file="data/GDP PPP Data.xlsx", number_of_frames=number_of_frames).df

    canvas = Canvas.canvas()

    square = canvas.canvas.create_rectangle(-1, -1, 1441, 1441)

    # load colors
    with open('colors/colors.json') as f:
        colors = json.load(f)

    # add bar chart
    bar_chart = BarRace.bar_race(canvas=canvas.canvas, df=df, number_of_bars=20, x_pos=50, y_pos=200, height=1200, width=1350, colors=colors)
    canvas.add_sub_plot(bar_chart)

    date = Date.date(canvas=canvas.canvas, df=df, time_indicator="year", width=0, height=150, x_pos=1200, y_pos=1200, font_color=(100,100,100))
    canvas.add_sub_plot(date)

    title = StaticText.static_text(canvas=canvas.canvas, text="GDP per Capita (PPP)", width=0, height=100, anchor="c", x_pos=1440/2, y_pos=50)
    canvas.add_sub_plot(title)

    canvas.play(fps=fps)


if __name__ == "__main__":
    main()