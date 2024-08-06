# 🛠️ **Proxttk**: Terminal-Based GUI Application Builder

Welcome to **Proxttk**, the ultimate terminal-based tool for designing and generating Tkinter-based GUI applications! 🚀 With Proxttk, you can quickly prototype your GUI, set up widgets, and generate clean Tkinter code directly from the command line.

![Proxttk Logo](https://github.com/Proxlight/Proxttk/blob/main/Logo.png) <!-- Replace with your resized logo URL -->
<small><em>(© Proxlight 2024)</em></small>

## Features

- **📐 Set Application Size**: Easily define your app's dimensions.
- **🖍️ Add Widgets**: Include buttons, labels, entries, and textboxes.
- **🖼️ Add Image Widgets**: Use images for interactive buttons with hover effects.
- **✏️ Rounded Entries**: Design sleek, rounded text input fields.
- **🌆 Background Image**: Set a background image to enhance your app's appearance.
- **💾 Generate Code**: Preview and save your Tkinter code.
- **🚀 Run Application**: Execute your generated code right from the terminal.

## Getting Started

### Prerequisites

- Python 3.x
- Pillow (PIL) library
- Tkinter library

### Installation

1. **Clone the Repository:**

   ```sh
   git clone https://github.com/yourusername/proxttk.git
   ```

2. **Navigate to the Project Directory:**

   ```sh
   cd proxttk
   ```

3. **Install Dependencies:**

   ```sh
   pip install pillow
   ```

### Usage

1. **Run Proxttk:**

   ```sh
   python proxttk.py
   ```

2. **Follow the Terminal Prompts:**

   - **Set Application Name**: Define the name of your application.
   - **Set Application Size**: Specify the dimensions of your window.
   - **Add Widget**: Choose and customize widgets like buttons, labels, and more.
   - **Add Button with Image**: Incorporate images into buttons with hover effects.
   - **Add Rounded Entry**: Create stylish rounded text entries.
   - **Set Background Image**: Add a background image to your application.
   - **Generate Code**: Preview the Tkinter code generated by your inputs.
   - **Export Code as .py File**: Save the code as a `.py` file.
   - **Run Generated Application**: Execute the saved code to see your app in action.
   - **Exit**: Close the terminal application builder.

### Example

Here's an example of a Tkinter application generated by Proxttk. This example includes an image-based button with hover effects:

```python
import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk

class App:
    def __init__(self, root):
        root.title("MyApp")
        root.geometry("800x600")
        root.resizable(False, False)  # Make the window non-resizable

        # Load and resize image for the button
        img = Image.open("button_image.png")
        img = img.resize((150, 75), Image.LANCZOS)
        button_image = ImageTk.PhotoImage(img)

        button = tk.Button(root, image=button_image, borderwidth=0, highlightthickness=0, relief="flat")
        button.place(x=100, y=100, width=150, height=75)
        button.image = button_image  # Keep a reference to avoid garbage collection

        # Hover image effect
        hover_img = Image.open("button_hover_image.png")
        hover_img = hover_img.resize((150, 75), Image.LANCZOS)
        button_hover_image = ImageTk.PhotoImage(hover_img)

        def on_enter(event):
            button.config(image=button_hover_image)

        def on_leave(event):
            button.config(image=button_image)

        button.bind("<Enter>", on_enter)
        button.bind("<Leave>", on_leave)
        button.hover_image = button_hover_image  # Keep a reference to avoid garbage collection

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
```

In this example, the application window is 800x600 pixels, featuring a button with an image that changes when hovered over. 

![Example App](https://example.com/path/to/example_image.png) <!-- Replace with your example image URL -->

## Contributing

We welcome contributions! If you'd like to help out, please fork the repository and submit a pull request. For issues or feature requests, open an issue on GitHub.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

