from sjvisualizer import DataHandler, Canvas, BarRace, StaticImage
import json

EXCEL_FILE = "data/Nuclear.xlsx"
FPS = 60
DURATION = 0.25
with open("colors.json") as f:
    colors = json.load(f)

# colors = {}

# load the data into a data frame
df = DataHandler.DataHandler(excel_file=EXCEL_FILE, number_of_frames=FPS*DURATION*60).df

# creating the canvas
canvas = Canvas.canvas()

# adding the racing bar chart
bar_chart = BarRace.bar_race(df=df, canvas=canvas.canvas, colors=colors)
canvas.add_sub_plot(bar_chart)

# adding a title
canvas.add_title("Nuclear Warheads by Country", color=(0,0,0))
canvas.add_sub_title("From 1950 - 2021", color=(150,150,150))

# adding a time
canvas.add_time(df=df, time_indicator="year")

# # adding a logo
canvas.add_logo(logo="logo.png")

# play the animation
canvas.play(fps=FPS)