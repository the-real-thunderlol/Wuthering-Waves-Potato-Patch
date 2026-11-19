import tkinter
import webbrowser

def show_credits():
    POPUP = tkinter.Toplevel()

    POPUP.title("Credits")
    POPUP.resizable(False, False)

    POPUP.configure(bg="#1f1f1f")

    MADE_BY_LABEL = tkinter.Label(
        POPUP,
        text="Made by Thunderlol",
        bg="#1f1f1f",
        fg="white",
        font=("Arial", 12, "bold")
    )
    MADE_BY_LABEL.pack(padx=30, pady=(30, 10))

    YOUTUBE_LABEL = tkinter.Label(
        POPUP,
        text="Youtube = @thunderlol",
        bg="#1f1f1f",
        fg="#4ea1ff",
        cursor="hand2",
        font=("Arial", 12, "underline")
    )
    YOUTUBE_LABEL.pack(padx=30, pady=5)
    YOUTUBE_LABEL.bind("<Button-1>", lambda event: webbrowser.open("https://www.youtube.com/@thunderlol_real"))

    GITHUB_LABEL = tkinter.Label(
        POPUP,
        text="Github: the-real-thunderlol",
        bg="#1f1f1f",
        fg="#4ea1ff",
        cursor="hand2",
        font=("Arial", 12, "underline")
    )
    GITHUB_LABEL.pack(padx=30, pady=5)
    GITHUB_LABEL.bind("<Button-1>", lambda event: webbrowser.open("https://github.com/the-real-thunderlol"))

    OK_BUTTON = tkinter.Button(
        POPUP,
        text="OK",
        width=10,
        command=POPUP.destroy
    )
    OK_BUTTON.pack(pady=(20, 20))

    POPUP.transient(POPUP.master)
    POPUP.grab_set()
