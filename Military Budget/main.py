from sjvisualizer import Canvas
from sjvisualizer import DataHandler
from sjvisualizer import BarRace
from sjvisualizer import PieRace
from sjvisualizer import Date
from sjvisualizer import StaticText
from sjvisualizer import StaticImage
import time
import json

def main(duration = 1.0, fps = 60, font_color=(255,255,255), background=(0,0,0)):
    number_of_frames = duration * fps * 60
    df = DataHandler.DataHandler(excel_file="data/military budget.xlsx", number_of_frames=number_of_frames).df

    canvas = Canvas.canvas(bg=background)

    # load colors
    with open('colors/colors.json') as f:
        colors = json.load(f)

    # static_img = StaticImage.static_image(canvas=canvas.canvas, x_pos=0, y_pos=0, height=1350,
    #                              width=1350, file="assets/background.png")
    # canvas.add_sub_plot(static_img)

    square = canvas.canvas.create_rectangle(-1, -1, 1051, 1351)

    # add bar chart
    bar_chart = BarRace.bar_race(canvas=canvas.canvas, df=df, number_of_bars=12, x_pos=200, y_pos=250, height=1000,
                                 width=750, colors=colors, shift=150, unit="$M", font_color=font_color)
    canvas.add_sub_plot(bar_chart)

    # add pie chart
    pie = PieRace.pie_plot(canvas=canvas.canvas, df=df, x_pos=725, y_pos=750, height=350,
                                 width=350, colors=colors, shift=150, unit="$M", display_percentages=False, display_label=False, back_ground_color=(0,0,0))
    canvas.add_sub_plot(pie)

    date = Date.date(canvas=canvas.canvas, df=df, time_indicator="year", width=0, height=100, x_pos=900, y_pos=1100,
                     font_color=font_color)
    canvas.add_sub_plot(date)

    title = StaticText.static_text(canvas=canvas.canvas, text="Military Budget", width=0, height=100, anchor="c",
                                   x_pos=1050 / 2, y_pos=50, font_color=font_color)
    canvas.add_sub_plot(title)

    title = StaticText.static_text(canvas=canvas.canvas, text="Data Source: World Bank", width=0, height=25, anchor="w",
                                   x_pos=50, y_pos=1300, font_color=font_color)
    canvas.add_sub_plot(title)

    title = StaticText.static_text(canvas=canvas.canvas, text="Made with: sjvisualizer", width=0, height=25, anchor="e",
                                   x_pos=1000, y_pos=1300, font_color=font_color)
    canvas.add_sub_plot(title)

    canvas.play(fps=fps)

main()