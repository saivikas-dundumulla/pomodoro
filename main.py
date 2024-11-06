from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
TICK = "✔"
reps = 0
timer = ""
# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(canvas_text, text="00:00")
    timer_label.config(fg=GREEN, text="Timer")
    check_mark.config(text="")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    long_break_session = LONG_BREAK_MIN * 60
    short_break_session = SHORT_BREAK_MIN * 60
    work_session = WORK_MIN * 60

    if reps % 8 == 0:
        timer_label.config(fg=RED, text="Break")
        count_down(long_break_session)
    elif reps % 2 == 0:
        timer_label.config(fg=PINK, text="Break")
        count_down(short_break_session)
    else:
        timer_label.config(fg=GREEN, text="Timer")
        count_down(work_session)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(counter):
    min_hand = counter // 60
    second_hand = counter % 60
    if second_hand < 10:
        second_hand = f"0{second_hand}"
    canvas.itemconfig(canvas_text, text=f"{min_hand}:{second_hand}")
    if counter > 0:
        global timer
        timer = window.after(100, count_down, counter - 1)
    else:
        start_timer()
        total_sessions = reps // 2
        checks = ""
        for _ in range(total_sessions):
            checks += TICK
        check_mark.config(text=checks)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label(text="Timer", font=(FONT_NAME, 36, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
canvas_text = canvas.create_text(102, 130, text="00:00", font=(FONT_NAME, 32, "bold"), fill="white")
canvas.grid(row=1, column=1)

start_button = Button(text="START", command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text= "RESET", command=reset_timer)
reset_button.grid(row=2, column=2)

check_mark = Label(fg=GREEN, bg=YELLOW)
check_mark.grid(row=3, column=1)


window.mainloop()
