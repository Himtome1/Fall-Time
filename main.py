import tkinter as tk
import math as m
import time as t


w = 600
h = 400
x = w//2
y = w//2

# Window size
window = tk.Tk()
window.resizable(width=False, height=False)
window.title("Fall Time")

entry1 = tk.Frame(master=window)
canvas = tk.Canvas(master=window, height=h, width=w, bg="#EAF5F5",)


def calc():
    speed = float(speed_entry.get())
    theta = float(angle_entry.get())
    height = float(height_entry.get())  # parameters from entry fields in GUI

    vx = (speed * m.cos(m.radians(theta)))
    vy = (speed * m.sin(m.radians(theta)))  # velocity components

    time_1 = vy / 9.8  # time until max height

    max_height = (vy * time_1) + (0.5 * (-9.8 * time_1 * time_1))

    time_2 = m.sqrt((2 * (max_height+height)) / 9.8)  # time from max height to ground

    time_total = time_1 + time_2
    dx = vx * time_total  # distance travelled in x direction

    result_label["text"] = f"Time: {round(time_total, 2)} s \n Distance: {round(dx, 2)} m "  # updates result label
    return vx, vy, height, time_total, max_height, time_1


def y_position(time, vy, height):  # y-position as a function of time, vy and height are constants from by GUI field

    y = height+(vy * time) - 4.905*time*time

    return y


def graphic_motion():
    data = calc()  # calls calc() and stores returned list as data
    vx = data[0]
    vy = data[1]
    height = data[2]
    time = data[3]
    color = 'B6D7A8'
    color_end = 'D7A8A8'
    positions = []  # initializing position list

    n = -1  # index loop counter

    canvas.itemconfig(my_circle, fill=f"#{color}")
    canvas.moveto(my_circle, 25, y-height*25+93)
    canvas.update()
    t.sleep(1)
    start_time = t.time()
    ypos = 1
    while ypos >= 0:
        n = n + 1
        current_time = t.time() - start_time
        ypos = y_position(current_time, vy, height)
        positions.append(y_position(current_time, vy, height), )
        # positions.append(round(y_position(i, vy, height), ))
        # print(positions[n])

        circle_coords = canvas.coords(my_circle)
        x_coord = circle_coords[0]
        y_coord = circle_coords[1]

        print(current_time)

        canvas.update()

        if x_coord >= 600:
            width_increased = w
            width_increased = width_increased*2
            canvas.config(width=width_increased)

            if x_coord >= 1200:
                width_increased = width_increased * 2
                canvas.config(width=width_increased)
        else:
            canvas.config(width=w)

        if y_coord > 0:
            canvas.moveto(my_circle, 25 + vx * current_time * 25, y - positions[n] * 25 + 93)

        if y_coord <= 0:
            canvas.moveto(my_circle, 25 + vx * current_time * 25, y - positions[n] * 25 + 400)

        t.sleep(0.01)

    circle_coords = canvas.coords(my_circle)
    canvas.moveto(my_circle, circle_coords[0], y+93)
    canvas.itemconfig(my_circle, fill=f"#{color_end}")

    return circle_coords


def action():
    graphic_motion()






my_circle = canvas.create_oval(x, y, x+10, y+10, fill="#B6D7A8")


height_label = tk.Label(master=entry1, text="Enter height in metres:")
height_entry = tk.Entry(master=entry1, width=10)

speed_label = tk.Label(text="Enter speed: ", master=entry1)
speed_entry = tk.Entry(master=entry1, width=10)

angle_label = tk.Label(master=entry1, text="Enter angle:")
angle_entry = tk.Entry(master=entry1, width=10)

height_label.grid(row=0, column=0, sticky="w")
height_entry.grid(row=0, column=1)

speed_label.grid(row=1, column=0, sticky="w")
speed_entry.grid(row=1, column=1)

angle_label.grid(row=2, column=0, sticky="w")
angle_entry.grid(row=2, column=1)

entry1.grid(row=0, column=0, sticky="w")
# entry2.grid(row=1, column=0)

result_label = tk.Label(master=entry1, text="result")

result_button = tk.Button(
    master=entry1,
    text="GO!",
    height=2,
    width=5,
    command=action,
)

result_button.grid(row=0, column=2, sticky="w", padx=100, pady=5)
result_label.grid(row=0, column=3, sticky="w")
canvas.grid(row=1, column=0)




tk.mainloop()
