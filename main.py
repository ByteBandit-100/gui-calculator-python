from tkinter.messagebox import showerror
import ttkbootstrap as tk

def set_val(val):
    current = out_var.get()
    out_var.set(current + val)

def clear_out():
    out_var.set('')

def step_back():
    current = out_var.get()
    out_var.set(current[:-1])

def calculate():
    current = out_var.get()
    if current[0]== '=':
        calc = eval(current[1:])
    else:
        calc = eval(current)
    out_var.set(f"={calc}")

def create_frame1():
    frame1 = tk.Frame(root)
    frame1.pack(pady=10,padx=10)

    output_lab = tk.Entry(frame1, textvariable=out_var, font=('Consolas', 24), width=18)
    output_lab.pack(pady=8)

def create_frame2():
    frame2 = tk.Frame(root)
    frame2.pack(pady=8,padx=8)
    ops = ('C', '<-', '+', '-', 1, 2, 3, '*', 4, 5, 6, '/', 7, 8, 9, '.', 0, '=')
    k = 0
    for i in range(5):
        for j in range(4):
            if ops[k] == 'C':
                btn = tk.Button(frame2, text=ops[k], cursor='hand2',width=6, command=lambda: clear_out(),bootstyle='WARNING')
                btn.grid(row=0, column=0, padx=6, pady=7,ipady=18)
            elif ops[k] == '<-':
                btn = tk.Button(frame2, text=ops[k], cursor='hand2',width=6,command=lambda: step_back(),bootstyle='WARNING')
                btn.grid(row=0, column=1, padx=6, pady=7,ipady=18)
            elif ops[k] == '=':
                btn = tk.Button(frame2, text=ops[k], cursor='hand2',width=6,command=lambda: calculate(),bootstyle='SUCCESS')
                btn.grid(row=4, column=1, padx=6, pady=7,ipady=18,columnspan=3,sticky='we')
            else:
                btn = tk.Button(frame2, text=ops[k], cursor='hand2',width=6,command=lambda val=ops[k]: set_val(str(val)))
                btn.grid(row=i, column=j, padx=6, pady=7,ipady=18)
            k += 1
            if k == 18: break

if __name__ == '__main__':
    root = tk.Window(themename="darkly")
    root.geometry('370x550')
    root.resizable(False,False)
    root.iconbitmap('./calc.ico')
    root.config(padx=10,pady=10)
    out_var = tk.StringVar()
    create_frame1()
    create_frame2()
    root.mainloop()