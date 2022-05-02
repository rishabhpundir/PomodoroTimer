from tkinter import *
import math
from urllib import response
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    window.after_cancel(timer)
    timer_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    tick_label.config(text="")
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60 
    
    if reps % 2 == 0 and reps != 8:
        timer_label.config(text="Break!", fg=PINK, bg=YELLOW, font=(FONT_NAME, 32, "bold"))
        countdown(short_break_sec)
    elif reps % 8 == 0:
        timer_label.config(text="Break!", fg=RED, bg=YELLOW, font=(FONT_NAME, 32, "bold"))
        countdown(long_break_sec)
    else:
        timer_label.config(text="Work!", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 32, "bold"))
        countdown(work_sec)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    global timer
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_str = '0' + str(count_sec) # OR use an f string to cut off 'else' usage
    else:
        count_str = str(count_sec)
        
    count_sec = count_str
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1, countdown, count-1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps/2)
        for tick in range(work_sessions):
            mark += "✔️"
            tick_label.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=75, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 132, text="00:00", fill="white", font=(FONT_NAME, 26, "bold"))
canvas.grid(row=1, column=1)

#Timer label
timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 32, "bold"))
timer_label.grid(row=0, column=1)

#Start Button
start_button = Button(text="Start", command=start_timer)
start_button.grid(row=2, column=0)

#Reset Button
reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(row=2, column=2)

#Tick label
tick_label = Label(fg=GREEN, bg=YELLOW)
tick_label.grid(row=4, column=1)

window.mainloop()