import os
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import Canvas

class TerminalAppBuilder:
    def __init__(self):
        self.app_name = "MyApp"
        self.app_size = "800x600"
        self.bg_image = None
        self.widgets = []

    def set_app_name(self):
        self.app_name = input("Enter application name (default 'MyApp'): ") or "MyApp"

    def set_app_size(self):
        size = input("Enter application size (widthxheight, default '800x600'): ")
        self.app_size = size if size else "800x600"

    def add_widget(self):
        widget_type = input("Enter widget type (e.g., button, label, entry, textbox, or 'back' to return to the previous menu): ").strip().lower()
        if widget_type == 'back':
            return
        x = input("Enter x position (default '0'): ") or "0"
        y = input("Enter y position (default '0'): ") or "0"
        color = input("Enter widget color (default 'black'): ") or "black"
        width = input(f"Enter {widget_type} width (default '100'): ") or "100"
        height = input(f"Enter {widget_type} height (default '30'): ") or "30"
        if not self.is_valid_color(color):
            print(f"Invalid color name '{color}'. Setting to default 'black'.")
            color = "black"
        borderless = input("Make widget borderless? (yes/no, default 'no'): ").strip().lower() == 'yes'
        self.widgets.append({
            'type': widget_type,
            'x': x,
            'y': y,
            'color': color,
            'width': width,
            'height': height,
            'borderless': borderless
        })
        self.update_code_preview()

    def add_image_widget(self):
        file_path = input("Enter image file path (or 'back' to return to the previous menu): ").strip()
        if file_path.lower() == 'back':
            return
        hover_file_path = input("Enter hover image file path (or 'skip' to skip): ").strip()
        if hover_file_path.lower() == 'skip':
            hover_file_path = None
        x = input("Enter x position (default '0'): ") or "0"
        y = input("Enter y position (default '0'): ") or "0"
        width = input("Enter button width (default '100'): ") or "100"
        height = input("Enter button height (default '50'): ") or "50"
        self.widgets.append({
            'type': 'button_image',
            'x': x,
            'y': y,
            'image': file_path,
            'hover_image': hover_file_path,
            'width': width,
            'height': height
        })
        self.update_code_preview()

    def add_rounded_entry_widget(self):
        x = input("Enter x position (default '0'): ") or "0"
        y = input("Enter y position (default '0'): ") or "0"
        width = input("Enter entry width (default '200'): ") or "200"
        height = input("Enter entry height (default '30'): ") or "30"
        corner_radius = int(input("Enter corner radius (default '10'): ") or "10")
        border_color = input("Enter border color (default 'black'): ") or "black"
        color = input("Enter entry color (default 'white'): ") or "white"
        default_text = input("Enter default text in the entry (default 'Entry'): ") or "Entry"

        self.widgets.append({
            'type': 'rounded_entry',
            'x': x,
            'y': y,
            'width': width,
            'height': height,
            'corner_radius': corner_radius,
            'border_color': border_color,
            'color': color,
            'default_text': default_text
        })
        self.update_code_preview()

    def set_background_image(self):
        file_path = input("Enter background image file path (or 'skip' to skip): ").strip()
        if file_path.lower() == 'skip':
            return
        if not os.path.isfile(file_path):
            print("File does not exist. Skipping.")
            return
        self.bg_image = file_path
        self.update_code_preview()

    def is_valid_color(self, color_name):
        try:
            root = tk.Tk()
            root.tk_setPalette(background=color_name)
            root.destroy()
            return True
        except tk.TclError:
            return False

    def generate_code(self):
        width, height = self.app_size.split('x')
        code = f'''import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk

class App:
    def __init__(self, root):
        root.title("{self.app_name}")
        root.geometry("{self.app_size}")
        root.resizable(False, False)  # Make the window non-resizable
'''

        if self.bg_image:
            code += f'''
        self.bg_image = PhotoImage(file="{self.bg_image}")
        bg_label = tk.Label(root, image=self.bg_image)
        bg_label.place(relwidth=1, relheight=1)
'''

        for idx, widget in enumerate(self.widgets):
            x, y = widget['x'], widget['y']
            width, height = widget['width'], widget['height']
            if widget['type'] == 'button':
                color = widget['color']
                code += f'''
        button_{idx} = tk.Button(root, text="Button", bg="{color}")
        button_{idx}.place(x={x}, y={y}, width={width}, height={height})
'''
            elif widget['type'] == 'label':
                color = widget['color']
                code += f'''
        label_{idx} = tk.Label(root, text="Label", bg="{color}")
        label_{idx}.place(x={x}, y={y}, width={width}, height={height})
'''
            elif widget['type'] == 'entry':
                color = widget['color']
                borderless = widget['borderless']
                code += f'''
        entry_{idx} = tk.Entry(root, bg="{color}", bd={0 if borderless else 1})
        entry_{idx}.place(x={x}, y={y}, width={width}, height={height})
'''
            elif widget['type'] == 'textbox':
                color = widget['color']
                borderless = widget['borderless']
                code += f'''
        textbox_{idx} = tk.Text(root, bg="{color}", bd={0 if borderless else 1})
        textbox_{idx}.place(x={x}, y={y}, width={width}, height={height})
'''
            elif widget['type'] == 'button_image':
                code += f'''
        # Load and resize image for the button
        img = Image.open("{widget['image']}")
        img = img.resize(({widget['width']}, {widget['height']}), Image.LANCZOS)
        button_image_{idx} = ImageTk.PhotoImage(img)

        button_{idx} = tk.Button(root, image=button_image_{idx}, borderwidth=0, highlightthickness=0, relief="flat")
        button_{idx}.place(x={x}, y={y}, width={widget['width']}, height={widget['height']})
        # Keep a reference to avoid garbage collection
        button_{idx}.image = button_image_{idx}
'''

                if widget['hover_image']:
                    code += f'''
        # Load and resize hover image for the button
        hover_img = Image.open("{widget['hover_image']}")
        hover_img = hover_img.resize(({widget['width']}, {widget['height']}), Image.LANCZOS)
        button_hover_image_{idx} = ImageTk.PhotoImage(hover_img)

        def on_enter(event):
            button_{idx}.config(image=button_hover_image_{idx})

        def on_leave(event):
            button_{idx}.config(image=button_image_{idx})

        button_{idx}.bind("<Enter>", on_enter)
        button_{idx}.bind("<Leave>", on_leave)
        # Keep a reference to avoid garbage collection
        button_{idx}.hover_image = button_hover_image_{idx}
'''
            elif widget['type'] == 'rounded_entry':
                corner_radius = widget['corner_radius']
                border_color = widget['border_color']
                color = widget['color']
                default_text = widget['default_text']
                code += f'''
        canvas_{idx} = tk.Canvas(root, width={width}, height={height}, bg="{border_color}", highlightthickness=0)
        canvas_{idx}.create_oval(0, 0, {2*corner_radius}, {2*corner_radius}, outline="{border_color}", width=2)
        canvas_{idx}.create_oval({width}-{2*corner_radius}, 0, {width}, {2*corner_radius}, outline="{border_color}", width=2)
        canvas_{idx}.create_oval(0, {height}-{2*corner_radius}, {2*corner_radius}, {height}, outline="{border_color}", width=2)
        canvas_{idx}.create_oval({width}-{2*corner_radius}, {height}-{2*corner_radius}, {width}, {height}, outline="{border_color}", width=2)
        canvas_{idx}.create_rectangle({corner_radius}, 0, {width}-{corner_radius}, {height}, outline="{border_color}", width=2)
        canvas_{idx}.create_rectangle(0, {corner_radius}, {width}, {height}-{corner_radius}, outline="{border_color}", width=2)

        entry_{idx} = tk.Entry(root, bg="{color}", bd=0, highlightthickness=0)
        entry_{idx}.insert(0, "{default_text}")
        canvas_{idx}.create_window({corner_radius}, {corner_radius}, anchor="nw", width={width}-{2*corner_radius}, height={height}-{2*corner_radius}, window=entry_{idx})

        canvas_{idx}.place(x={x}, y={y})
'''

        code += '''
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
'''

        return code

    def save_code(self, code):
        file_name = input("Enter the filename to save the code (e.g., app.py): ") or "app.py"
        if not file_name.endswith(".py"):
            file_name += ".py"
        with open(file_name, "w") as f:
            f.write(code)
        print(f"Code saved to {file_name}")

    def run_code(self, file_name):
        if not os.path.isfile(file_name):
            print(f"File {file_name} does not exist. Cannot run.")
            return
        os.system(f'python "{file_name}"')

    def update_code_preview(self):
        print("\nGenerated Code Preview:\n")
        code = self.generate_code()
        print(code)

    def run(self):
        while True:
            print("\n1. Set Application Name")
            print("2. Set Application Size")
            print("3. Add Widget")
            print("4. Add Button with Image")
            print("5. Add Rounded Entry")
            print("6. Set Background Image")
            print("7. Generate Code")
            print("8. Export Code as .py File")
            print("9. Run Generated Application")
            print("10. Exit")
            choice = input("Choose an option: ").strip()

            if choice == "1":
                self.set_app_name()
            elif choice == "2":
                self.set_app_size()
            elif choice == "3":
                self.add_widget()
            elif choice == "4":
                self.add_image_widget()
            elif choice == "5":
                self.add_rounded_entry_widget()
            elif choice == "6":
                self.set_background_image()
            elif choice == "7":
                self.update_code_preview()
            elif choice == "8":
                code = self.generate_code()
                self.save_code(code)
            elif choice == "9":
                file_name = input("Enter the filename of the code to run (e.g., app.py): ").strip()
                self.run_code(file_name)
            elif choice == "10":
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    builder = TerminalAppBuilder()
    builder.run()
