import tkinter as tk
from tkinter import ttk, messagebox
import math

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ماشین حساب نساجی")
        self.root.geometry("900x300")
        self.root.resizable(True, True)
        
        # Create notebook (tabs)
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Create frames for each part
        self.create_part1_tab()
        self.create_part2_tab()
        self.create_part3_tab()
        self.create_part4_tab()
        
    def create_part1_tab(self):
        # وزن تئوری تولید در دقیقه:= (سرعت * تعداد سر نخ * نمره به دنیر)/900000
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="ذوب ریسی/وزن تئوری تولید در دقیقه")
        
        ttk.Label(frame, text="سرعت:").grid(row=0, column=0, padx=5, pady=5, sticky='e')
        self.velocity_entry = ttk.Entry(frame)
        self.velocity_entry.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(frame, text="تعداد سر نخ:").grid(row=1, column=0, padx=5, pady=5, sticky='e')
        self.Sting_num_entry = ttk.Entry(frame)
        self.Sting_num_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(frame, text="نمره به دنیر:").grid(row=2, column=0, padx=5, pady=5, sticky='e')
        self.Denier_entry = ttk.Entry(frame)
        self.Denier_entry.grid(row=2, column=1, padx=5, pady=5)
        
        calc_btn = ttk.Button(frame, text="محاسبه", command=self.calculate_part1)
        calc_btn.grid(row=3, column=0, columnspan=2, pady=10)
        
        self.result1 = ttk.Label(frame, text="نتیجه: ")
        self.result1.grid(row=4, column=0, columnspan=2)
    
    def create_part2_tab(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="ذوب ریسی/وزن تئوری تولید در زمان فعالیت ")
        
        ttk.Label(frame, text=" وزن تئوری تولید در دقیقه:").grid(row=0, column=0, padx=5, pady=5, sticky='e')
        self.Tmass_entry = ttk.Entry(frame)
        self.Tmass_entry.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(frame, text="زمان کارکرد ماشین به دقیقه:").grid(row=1, column=0, padx=5, pady=5, sticky='e')
        self.WT_entry = ttk.Entry(frame)
        self.WT_entry.grid(row=1, column=1, padx=5, pady=5)
        
        calc_btn = ttk.Button(frame, text="محاسبه", command=self.calculate_part2)
        calc_btn.grid(row=2, column=0, columnspan=2, pady=10)
        
        self.result2 = ttk.Label(frame, text="نتیجه: ")
        self.result2.grid(row=3, column=0, columnspan=2)
    
    def create_part3_tab(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="ذوب ریسی/وزن تئوری محصول تولیدی")
        
        ttk.Label(frame, text="درصد مستربچ:").grid(row=0, column=0, padx=5, pady=5, sticky='e')
        self.mp_entry = ttk.Entry(frame)
        self.mp_entry.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(frame, text="وزن چیپس:").grid(row=1, column=0, padx=5, pady=5, sticky='e')
        self.CHW_entry = ttk.Entry(frame)
        self.CHW_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(frame, text="درصد روغن :").grid(row=2, column=0, padx=5, pady=5, sticky='e')
        self.OP_entry = ttk.Entry(frame)
        self.OP_entry.grid(row=2, column=1, padx=5, pady=5)
        
        calc_btn = ttk.Button(frame, text="محاسبه", command=self.calculate_part3)
        calc_btn.grid(row=3, column=0, columnspan=2, pady=10)
        
        self.result3 = ttk.Label(frame, text="نتیجه: ")
        self.result3.grid(row=4, column=0, columnspan=2)
    
    def create_part4_tab(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="ذوب ریسی/تعداد بوبین کامل تئوری")
        
        ttk.Label(frame, text="وزن تئوری محصول تولیدی:").grid(row=0, column=0, padx=5, pady=5, sticky='e')
        self.WTP_entry = ttk.Entry(frame)
        self.WTP_entry.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(frame, text="وزن بوبین کامل:").grid(row=1, column=0, padx=5, pady=5, sticky='e')
        self.WBH_entry = ttk.Entry(frame)
        self.WBH_entry.grid(row=1, column=1, padx=5, pady=5)
        
        calc_btn = ttk.Button(frame, text="محاسبه", command=self.calculate_part4)
        calc_btn.grid(row=2, column=0, columnspan=2, pady=10)
        
        self.result4 = ttk.Label(frame, text="نتیجه: ")
        self.result4.grid(row=3, column=0, columnspan=2)
    
    # Calculation functions with error handling
    def calculate_part1(self):
        try:
            velocity = float(self.velocity_entry.get())
            Sting_num = float(self.Sting_num_entry.get())
            Denier_entry = float(self.Denier_entry.get())
            
            result = (Denier_entry * Sting_num * velocity)/900000
            self.result1.config(text=f"جواب: {result:.2f}")
        except ValueError:
            messagebox.showerror("Error", "ورودی تعریف نشده! لطفا فقط عدد وارد کنید")
    
    def calculate_part2(self):
        try:
            Tmass = float(self.Tmass_entry.get())
            WTM_var = float(self.WT_entry.get())
            result = Tmass * WTM_var
            self.result2.config(text=f"جواب: {result:.2f}")
        except ValueError:
            messagebox.showerror("Error", "ورودی تعریف نشده! لطفا فقط عدد وارد کنید")
    
    def calculate_part3(self):
        try:
            CHW_var = float(self.CHW_entry.get())
            OP_var = float(self.OP_entry.get())
            mp_var = float(self.mp_entry.get())
            result = CHW_var + (mp_var * CHW_var) +(CHW_var+OP_var)/10000
            self.result3.config(text=f"جواب: {result:.2f}")
        except ValueError:
            messagebox.showerror("Error", "ورودی تعریف نشده! لطفا فقط عدد وارد کنید")
    
    def calculate_part4(self):
        try:
            WTP_var = float(self.WTP_entry.get())
            WBH_var = float(self.WBH_entry.get())
            result = WTP_var/WBH_var
            self.result4.config(text=f"جواب: {result:.2f}")
        except ValueError:
            messagebox.showerror("Error", "ورودی تعریف نشده! لطفا فقط عدد وارد کنید")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()