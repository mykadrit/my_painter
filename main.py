import tkinter as tk
from tkinter import colorchooser

class PaintApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Paint Program")

        self.canvas = tk.Canvas(root, bg="white", width=800, height=600)
        self.canvas.pack(expand=tk.YES, fill=tk.BOTH)

        self.setup_tools()
        self.setup_menu()

        self.color = "black"
        self.brush_size = 2
        self.old_x = None
        self.old_y = None

        self.canvas.bind("<B1-Motion>", self.paint)
        self.canvas.bind("<ButtonRelease-1>", self.reset)

    def paint(self, event):
        x, y = event.x, event.y

        if self.old_x and self.old_y:
            self.canvas.create_line(self.old_x, self.old_y, x, y, width=self.brush_size, fill=self.color, capstyle=tk.ROUND, smooth=tk.TRUE)

        self.old_x = x
        self.old_y = y

    def reset(self, event):
        self.old_x = None
        self.old_y = None

    def change_brush_size(self, size):
        self.brush_size = size

    def change_color(self):
        color = colorchooser.askcolor()[1]
        if color:
            self.color = color

    def setup_tools(self):
        self.tools_frame = tk.Frame(self.root, bg="gray")
        self.tools_frame.pack(side=tk.LEFT, fill=tk.Y)

        tk.Label(self.tools_frame, text="Brush Size", font=("Helvetica", 12), bg="gray").pack(pady=10)
        tk.Button(self.tools_frame, text="Small", command=lambda: self.change_brush_size(2)).pack()
        tk.Button(self.tools_frame, text="Medium", command=lambda: self.change_brush_size(5)).pack()
        tk.Button(self.tools_frame, text="Large", command=lambda: self.change_brush_size(10)).pack()

        tk.Button(self.tools_frame, text="Change Color", command=self.change_color).pack(pady=10)

    def setup_menu(self):
        menu_bar = tk.Menu(self.root)
        self.root.config(menu=menu_bar)

        file_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Exit", command=self.root.destroy)

if __name__ == "__main__":
    root = tk.Tk()
    app = PaintApp(root)
    root.mainloop()
