import tkinter
from components import get_path, apply_patch, credits

tk = tkinter.Tk()

tk.title("Wuthering Waves")
tk.minsize(600,640)
tk.maxsize(1920,1080)

tk.configure(bg="#1f1f1f")

TITLE = tkinter.Label(
    tk,
    text="WUWA POTATO SETTINGS PATCH",
    bg="#1f1f1f",
    fg="white",
    font=("Arial", 16, "bold")
)
TITLE.pack(pady=30)

PATH_WIDGET = tkinter.StringVar() #initial value

PATH_FRAME = tkinter.Frame(tk, bg="#1f1f1f")
PATH_FRAME.pack(fill="x", padx=20, pady=20)

PATH_ENTRY = tkinter.Entry(
    PATH_FRAME,
    textvariable=PATH_WIDGET,
    state="readonly",
    readonlybackground="#2b2b2b",
    fg="white",
    relief="flat"
)
PATH_ENTRY.pack(side="left", fill="x", expand=True, ipady=6)

def update_gui_path(PATH):
    if PATH:
        PATH_WIDGET.set(PATH)
        BUILD_BUTTON1.config(state="normal")
        BUILD_BUTTON2.config(state="normal")
        BUILD_BUTTON3.config(state="normal")
        BUILD_BUTTON4.config(state="normal")

BUTTON1 = tkinter.Button(
    PATH_FRAME,
    text="Update",
    command=lambda: update_gui_path(get_path.update_path())
)
BUTTON1.pack(side="right", padx=(8, 0))

BUILD_FRAME = tkinter.Frame(tk, bg="#1f1f1f")
BUILD_FRAME.pack(expand=True)

BUILD_BUTTON1 = tkinter.Button(
    BUILD_FRAME,
    text="Potato",
    width=25,
    state="disabled",
    command=lambda: apply_patch.APPLY_POTATO(THE_PATH)
)
BUILD_BUTTON1.pack(pady=10)

BUILD_BUTTON2 = tkinter.Button(
    BUILD_FRAME,
    text="Low",
    width=25,
    state="disabled",
    command=lambda: apply_patch.APPLY_LOW(THE_PATH)
)
BUILD_BUTTON2.pack(pady=10)

BUILD_BUTTON3 = tkinter.Button(
    BUILD_FRAME,
    text="Medium",
    width=25,
    state="disabled",
    command=lambda: apply_patch.APPLY_MEDIUM(THE_PATH)
)
BUILD_BUTTON3.pack(pady=10)

BUILD_BUTTON4 = tkinter.Button(
    BUILD_FRAME,
    text="Restore Default",
    width=25,
    state="disabled",
    command=lambda: apply_patch.APPLY_DEFAULT(THE_PATH)
)
BUILD_BUTTON4.pack(pady=10)

CREDITS_BUTTON = tkinter.Button(
    tk,
    text="Credits",
    command=credits.show_credits
)
CREDITS_BUTTON.place(relx=1.0, rely=1.0, x=-10, y=-10, anchor="se")


def rungui(SETTINGS_PATH):
    global THE_PATH
    THE_PATH = SETTINGS_PATH
    update_gui_path(SETTINGS_PATH)
    tk.mainloop()
