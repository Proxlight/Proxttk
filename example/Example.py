import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk

class App:
    def __init__(self, root):
        root.title("Student Management")
        root.geometry("800x600")
        root.resizable(False, False)  # Make the window non-resizable

        self.bg_image = PhotoImage(file="image.png")
        bg_label = tk.Label(root, image=self.bg_image)
        bg_label.place(relwidth=1, relheight=1)

        canvas_0 = tk.Canvas(root, width=155, height=24, bg="#202227", highlightthickness=0)
        canvas_0.create_oval(0, 0, 0, 0, outline="#202227", width=2)
        canvas_0.create_oval(155-0, 0, 155, 0, outline="#202227", width=2)
        canvas_0.create_oval(0, 24-0, 0, 24, outline="#202227", width=2)
        canvas_0.create_oval(155-0, 24-0, 155, 24, outline="#202227", width=2)
        canvas_0.create_rectangle(0, 0, 155-0, 24, outline="#202227", width=2)
        canvas_0.create_rectangle(0, 0, 155, 24-0, outline="#202227", width=2)

        entry_0 = tk.Entry(root, bg="#202227", bd=0, highlightthickness=0)
        entry_0.insert(0, "Add student name here...")
        canvas_0.create_window(0, 0, anchor="nw", width=155-0, height=24-0, window=entry_0)

        canvas_0.place(x=45, y=296)

        canvas_1 = tk.Canvas(root, width=155, height=24, bg="#202227", highlightthickness=0)
        canvas_1.create_oval(0, 0, 0, 0, outline="#202227", width=2)
        canvas_1.create_oval(155-0, 0, 155, 0, outline="#202227", width=2)
        canvas_1.create_oval(0, 24-0, 0, 24, outline="#202227", width=2)
        canvas_1.create_oval(155-0, 24-0, 155, 24, outline="#202227", width=2)
        canvas_1.create_rectangle(0, 0, 155-0, 24, outline="#202227", width=2)
        canvas_1.create_rectangle(0, 0, 155, 24-0, outline="#202227", width=2)

        entry_1 = tk.Entry(root, bg="#202227", bd=0, highlightthickness=0)
        entry_1.insert(0, "Enter roll no here...")
        canvas_1.create_window(0, 0, anchor="nw", width=155-0, height=24-0, window=entry_1)

        canvas_1.place(x=44, y=371)

        # Load and resize image for the button
        img = Image.open("Button.png")
        img = img.resize((183, 49), Image.LANCZOS)
        button_image_2 = ImageTk.PhotoImage(img)

        button_2 = tk.Button(root, image=button_image_2, borderwidth=0, highlightthickness=0, relief="flat")
        button_2.place(x=31, y=431, width=183, height=49)
        # Keep a reference to avoid garbage collection
        button_2.image = button_image_2

        # Load and resize hover image for the button
        hover_img = Image.open("Button hover.png")
        hover_img = hover_img.resize((183, 49), Image.LANCZOS)
        button_hover_image_2 = ImageTk.PhotoImage(hover_img)

        def on_enter(event):
            button_2.config(image=button_hover_image_2)

        def on_leave(event):
            button_2.config(image=button_image_2)

        button_2.bind("<Enter>", on_enter)
        button_2.bind("<Leave>", on_leave)
        # Keep a reference to avoid garbage collection
        button_2.hover_image = button_hover_image_2

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
