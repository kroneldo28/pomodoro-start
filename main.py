from tkinter import *
import math


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 2
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 20
reps = 0


# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    if reps % 2 == 0:
        countdown(WORK_MIN * 60)
        reps += 1
        start_timer()
    elif reps % 2 == 1 and reps < 7:
        countdown(SHORT_BREAK_MIN * 60)
        reps += 1
        start_timer()
    elif reps == 7:
        countdown(LONG_BREAK_MIN * 60)
        reps += 1
        start_timer()
    else:
        pass


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000, countdown, count - 1)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
# We create the canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=False)
# We create a PhotoImage file that reads our image file
tomato_img = PhotoImage(file="tomato.png")
# We draw the image on the canvas
canvas.create_image(100, 112, image=tomato_img)
# We draw  a text on the canvas
timer_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 35, "bold"))
# We pack the canvas
canvas.grid(column=1, row=1)

# Timer Label
timer_label = Label(text="Timer", font=(FONT_NAME, 60), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

# Start and Reset Buttons
start_button = Button(text="Start", highlightbackground=YELLOW, command=start_timer)
start_button.grid(column=0, row=2)
reset_button = Button(text="Reset", highlightbackground=YELLOW)
reset_button.grid(column=2, row=2)

# The check Label
check_label = Label(text="✓", fg=GREEN, bg=YELLOW)
check_label.grid(column=1, row=3)

window.mainloop()
