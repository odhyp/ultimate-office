import tkinter as tk
from tkinter import ttk, filedialog
import sv_ttk

welcome_text = """This is welcome message
Welcome to Ultimate Office by Odhy Pradhana
This app is meant to help with 9-5 menial tasks"""


def main():
    # Initialize
    root = tk.Tk()
    root.title("Ultimate Office by Odhy Pradhana")
    root.option_add("*tearOff", False)

    # Responsive grid
    root.columnconfigure(index=0, weight=1)
    root.columnconfigure(index=1, weight=1)
    root.columnconfigure(index=2, weight=1)
    root.rowconfigure(index=0, weight=1)
    root.rowconfigure(index=1, weight=1)
    root.rowconfigure(index=2, weight=1)

# ---------------------------------------------------------------------------------
    # Welcome - Frame
    welcome_frame = ttk.LabelFrame(root, text="Placeholder Title",
                                   padding=(20, 10))
    welcome_frame.grid(row=0, column=0,
                       padx=(20, 10), pady=(20, 10),
                       columnspan=2,
                       sticky="nsew")

    # Welcome - Message
    welcome_message = ttk.Label(welcome_frame, text=welcome_text)
    welcome_message.grid(row=0, column=0, padx=5, pady=10, sticky="nsew")

# ---------------------------------------------------------------------------------
    # Menu - Frame
    frame_menu = ttk.LabelFrame(root, text="Menu",
                                padding=(20, 10))
    frame_menu.grid(row=1, column=0,
                    padx=(20, 10), pady=(20, 10),
                    rowspan=2,
                    sticky="nsew")

    # Menu - Control Variables
    var_radio = tk.IntVar()

    # Menu - Radiobuttons
    radio1 = ttk.Radiobutton(frame_menu, text="This is Radiobutton 1",
                             variable=var_radio, value=1)
    radio2 = ttk.Radiobutton(frame_menu, text="This is Radiobutton 2",
                             variable=var_radio, value=2)
    radio3 = ttk.Radiobutton(frame_menu, text="This is Radiobutton 3",
                             variable=var_radio, value=3)

    radio1.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
    radio2.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
    radio3.grid(row=2, column=0, padx=5, pady=5, sticky="nsew")

    # Light/dark mode button
    button = ttk.Button(root, text="Light/Dark Mode",
                        command=sv_ttk.toggle_theme)
    button.grid(row=1, column=1,
                padx=(20, 10), pady=(20, 10),
                sticky="nsew")

# ---------------------------------------------------------------------------------
    # File Upload - Frame
    frame_file_upload = ttk.LabelFrame(root, text="Uploaded Files",
                                       padding=(20, 10))
    frame_file_upload.grid(row=1, column=1,
                           padx=(20, 10), pady=(20, 10),
                           sticky="nsew")


# ---------------------------------------------------------------------------------
    # Submit - Frame
    frame_submit = ttk.Frame(root, padding=(20, 1))
    frame_submit.grid(row=2, column=1,
                      padx=(0), pady=(0),
                      sticky="wn")

    uploaded_files = list()

    def UploadAction(event=None):
        filenames = list(filedialog.askopenfilenames(
            title="Select a file",
            filetypes=[("All files", "*.*"),
                       ("Text files", "*.txt")
                       ]))
        uploaded_files.append(filenames)

    sample_text = ttk.Label(frame_file_upload, text=uploaded_files)
    sample_text.grid(row=0, column=0,
                     padx=5, pady=5,
                     sticky="nw")

    # File Upload - Button
    browse_file = ttk.Button(
        frame_submit, text="Browse File", command=UploadAction)
    browse_file.grid(row=1, column=0, padx=0, pady=0, sticky="nsew")


# ---------------------------------------------------------------------------------
    # Sun Valley TTK Theme
    sv_ttk.set_theme("light")

    # Center the window, and set minsize
    root.update()
    root.minsize(root.winfo_width(), root.winfo_height())
    x_cordinate = int((root.winfo_screenwidth()/2) - (root.winfo_width()/2))
    y_cordinate = int((root.winfo_screenheight()/2) - (root.winfo_height()/2))
    root.geometry("+{}+{}".format(x_cordinate, y_cordinate))

    # Start the main loop
    root.mainloop()


if __name__ == '__main__':
    main()
