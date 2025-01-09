import tkinter as tk

class ButtonDemo:
    def __init__(self, root):
        # assign root Tk as our own value, define title and window dimension
        self.root = root
        self.root.title("Button Example Program")
        self.root.geometry("500x525")
        self.num_clicks = 0

        self.label = tk.Label(
            root,
            text="Clicks: 0",
            font=("Times New Roman", 14)
        )
        self.label.pack()

        self.btn = tk.Button(
            root,
            text="Click me~",
            anchor="center",
            command=self.increment_click
        )
        self.btn.pack()

        self.res_btn = tk.Button(
            root,
            text="RESET",
            anchor="center",
            command=self.res_click
        )
        self.res_btn.pack()

    def increment_click(self):
        self.num_clicks += 1
        self.label.config(text=f"Clicks: {self.num_clicks}")

    def res_click(self):
        self.num_clicks = 0
        self.label.config(text=f"Clicks: 0")

if __name__ == "__main__":
    root = tk.Tk()
    # call buttonDemo and pass in root as an arguement
    ButtonDemo(root)

    root.mainloop()
