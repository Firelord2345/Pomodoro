from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
ticks = ""

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps, ticks
    reps = 0
    ticks = ""
    canvas.itemconfig(timer_text, text="00:00")
    label.config(text="TIMER", fg=GREEN)
    tick.config(text="")
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_down():
    global reps
    reps+=1
    work=WORK_MIN
    short=SHORT_BREAK_MIN
    long=LONG_BREAK_MIN
    if reps%8==0:
        label.config(text="LONG BREAK",font=FONT_NAME,fg=PINK)
        count_down(long*60)
    if reps%2==0:
        label.config(text="SHORT BREAK",font=FONT_NAME,fg=PINK)
        count_down(short*60)
    else:
        label.config(text="WORK",font=FONT_NAME,fg=PINK)
        count_down(work*60)
   
    
    
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    
    min=math.floor(count/60)
    sec=count%60
    canvas.itemconfig(timer_text,text=f"{min}:{sec}")
    if sec<10:
          canvas.itemconfig(timer_text,text=f"{min}:0{sec}")  
    if count>0:
     window.after(1000,count_down,count-1)
    else:
        update_ticks()
        start_down()
# ---------------------------- UPDATE TICKS ------------------------------- #
def update_ticks():
    global ticks
    if reps % 2 != 0:  # After each work session
        ticks += "✓"
        tick.config(text=ticks)

# ---------------------------- UI SETUP ------------------------------- #
# Create the main window
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50,bg="white")

# Create text timer
label=Label(text="TIMER",font=FONT_NAME,bg="white",fg=GREEN)
label.grid(column=1,row=0)



# Load the image
tomato_img = PhotoImage(file="tomato.png")  

# Create a canvas widget
canvas = Canvas(width=200, height=224, bg="white", highlightthickness=0)
canvas.create_image(100, 112, image=tomato_img)  
timer_text=canvas.create_text(100,130,text="00:00",fill="white",font=FONT_NAME)
canvas.grid(column=1,row=1)

# Create a button for start
start=Button(text="Start",command=start_down)
start.grid(column=0,row=2)

# Create a button for reset
reset=Button(text="Reset",command=reset_timer)
reset.grid(column=2,row=2)

# tickmark

tick=Label(fg=GREEN,bg="white",font=FONT_NAME)
tick.grid(column=1,row=2)

window.mainloop()