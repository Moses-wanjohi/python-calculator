import tkinter as tk
import math

class AdvancedCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Dark Calculator")
        self.root.geometry("380x500")
        self.root.resizable(False, False)
        
        
        self.root.configure(bg="#1e1e1e")

        
        self.entry = tk.Entry(
            root, 
            font=("Segoe UI", 22), 
            bg="#2d2d2d", 
            fg="#ffffff", 
            bd=0, 
            justify="right",
            insertbackground="white"
        )
        self.entry.grid(row=0, column=0, columnspan=4, ipady=15, padx=15, pady=(20, 15), sticky="nsew")

        self.create_buttons()

    def create_buttons(self):
        
        buttons = [
            ('sin', 1, 0, '#3a3a3a', '#00e5ff'), ('cos', 1, 1, '#3a3a3a', '#00e5ff'), ('tan', 1, 2, '#3a3a3a', '#00e5ff'), ('√', 1, 3, '#3a3a3a', '#00e5ff'),
            ('x²', 2, 0, '#3a3a3a', '#00e5ff'), ('π', 2, 1, '#3a3a3a', '#00e5ff'), ('C', 2, 2, '#e63946', '#ffffff'), ('⌫', 2, 3, '#e63946', '#ffffff'),
            ('7', 3, 0, '#2d2d2d', '#ffffff'), ('8', 3, 1, '#2d2d2d', '#ffffff'), ('9', 3, 2, '#2d2d2d', '#ffffff'), ('/', 3, 3, '#ff9500', '#ffffff'),
            ('4', 4, 0, '#2d2d2d', '#ffffff'), ('5', 4, 1, '#2d2d2d', '#ffffff'), ('6', 4, 2, '#2d2d2d', '#ffffff'), ('*', 4, 3, '#ff9500', '#ffffff'),
            ('1', 5, 0, '#2d2d2d', '#ffffff'), ('2', 5, 1, '#2d2d2d', '#ffffff'), ('3', 5, 2, '#2d2d2d', '#ffffff'), ('-', 5, 3, '#ff9500', '#ffffff'),
            ('0', 6, 0, '#2d2d2d', '#ffffff'), ('.', 6, 1, '#2d2d2d', '#ffffff'), ('=', 6, 2, '#007acc', '#ffffff'), ('+', 6, 3, '#ff9500', '#ffffff'),
        ]

        
        for i in range(7):
            self.root.grid_rowconfigure(i, weight=1)
        for j in range(4):
            self.root.grid_columnconfigure(j, weight=1)

        
        for (text, row, col, bg, fg) in buttons:
            cmd = lambda x=text: self.on_button_click(x)
            tk.Button(
                self.root,
                text=text,
                font=("Segoe UI", 12, "bold"),
                bg=bg,
                fg=fg,
                activebackground="#505050",
                activeforeground="#ffffff",
                bd=0,
                relief="flat",
                command=cmd
            ).grid(row=row, column=col, padx=4, pady=4, sticky="nsew")

    def on_button_click(self, value):
        current = self.entry.get()

        if value == 'C':
            self.entry.delete(0, tk.END)
        elif value == '⌫':
            self.entry.delete(len(current)-1, tk.END)
        elif value == '=':
            self.calculate()
        elif value == 'x²':
            self.entry.insert(tk.END, '**2')
        elif value == 'π':
            self.entry.insert(tk.END, str(math.pi))
        elif value in ('sin', 'cos', 'tan', '√'):
            self.entry.insert(tk.END, f"{value}(")
        else:
            self.entry.insert(tk.END, value)

    def calculate(self):
        expr = self.entry.get()
        
        
        expr = expr.replace('√(', 'math.sqrt(')
        expr = expr.replace('sin(', 'math.sin(math.radians(')
        expr = expr.replace('cos(', 'math.cos(math.radians(')
        expr = expr.replace('tan(', 'math.tan(math.radians(')

        
        open_parens = expr.count('(')
        close_parens = expr.count(')')
        expr += ')' * (open_parens - close_parens)

        try:
            
            result = eval(expr, {"__builtins__": None, "math": math})
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, f"{result:.8g}")
        except Exception:
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, "Error")

if __name__ == "__main__":
    root = tk.Tk()
    app = AdvancedCalculator(root)
    root.mainloop()