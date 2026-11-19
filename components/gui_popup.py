import tkinter

def show_popup(COPIED_FILES, SETTINGS_PATH):
    POPUP = tkinter.Toplevel()

    POPUP.title("Wuthering Waves")
    POPUP.resizable(False, False)

    POPUP.configure(bg="#1f1f1f")

    MESSAGE_LABEL = tkinter.Label(
        POPUP,
        text="Patches applied:\n" + "\n".join(COPIED_FILES) + "\n\nPath: " + str(SETTINGS_PATH),
        bg="#1f1f1f",
        fg="white",
        font=("Arial", 11),
        justify="left"
    )
    MESSAGE_LABEL.pack(padx=30, pady=(30, 20))

    OK_BUTTON = tkinter.Button(
        POPUP,
        text="OK",
        width=10,
        command=POPUP.destroy
    )
    OK_BUTTON.pack(pady=(0, 20))

    POPUP.transient(POPUP.master)
    POPUP.grab_set()
