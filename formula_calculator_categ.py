import tkinter as tk
from tkinter import ttk, messagebox
import math

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ماشین حساب نساجی")
        self.root.geometry("1100x500")
        self.root.resizable(True, True)
        
        # Create main notebook for categories
        self.main_notebook = ttk.Notebook(root)
        self.main_notebook.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Create category frames
        self.create_melt_spinning_tab()
        self.create_weaving_tab()
        self.create_finishing_tab()
        self.create_quality_tab()
        
    def create_melt_spinning_tab(self):
        category_frame = ttk.Frame(self.main_notebook)
        self.main_notebook.add(category_frame, text="ذوب ریسی")
        
        # Create sub-notebook for this category
        sub_notebook = ttk.Notebook(category_frame)
        sub_notebook.pack(fill='both', expand=True, padx=5, pady=5)
        
        # Create 4 tabs within category
        frame1 = ttk.Frame(sub_notebook)
        frame2 = ttk.Frame(sub_notebook)
        frame3 = ttk.Frame(sub_notebook)
        frame4 = ttk.Frame(sub_notebook)
        
        sub_notebook.add(frame1, text="وزن تئوری تولید در دقیقه")
        sub_notebook.add(frame2, text="وزن تئوری تولید در زمان فعالیت")
        sub_notebook.add(frame3, text="وزن تئوری محصول تولیدی")
        sub_notebook.add(frame4, text="تعداد بوبین کامل تئوری")
        
        self.create_part1_tab(frame1)
        self.create_part2_tab(frame2)
        self.create_part3_tab(frame3)
        self.create_part4_tab(frame4)
        
    def create_part1_tab(self, parent):
        # وزن تئوری تولید در دقیقه:= (سرعت * تعداد سر نخ * نمره به دنیر)/900000
        ttk.Label(parent, text="سرعت:").grid(row=0, column=0, padx=5, pady=5, sticky='e')
        self.velocity_entry = ttk.Entry(parent)
        self.velocity_entry.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(parent, text="تعداد سر نخ:").grid(row=1, column=0, padx=5, pady=5, sticky='e')
        self.Sting_num_entry = ttk.Entry(parent)
        self.Sting_num_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(parent, text="نمره به دنیر:").grid(row=2, column=0, padx=5, pady=5, sticky='e')
        self.Denier_entry = ttk.Entry(parent)
        self.Denier_entry.grid(row=2, column=1, padx=5, pady=5)
        
        calc_btn = ttk.Button(parent, text="محاسبه", command=self.calculate_part1)
        calc_btn.grid(row=3, column=0, columnspan=2, pady=10)
        
        self.result1 = ttk.Label(parent, text="نتیجه: ")
        self.result1.grid(row=4, column=0, columnspan=2)
        
    def create_part2_tab(self, parent):
        ttk.Label(parent, text=" وزن تئوری تولید در دقیقه:").grid(row=0, column=0, padx=5, pady=5, sticky='e')
        self.Tmass_entry = ttk.Entry(parent)
        self.Tmass_entry.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(parent, text="زمان کارکرد ماشین به دقیقه:").grid(row=1, column=0, padx=5, pady=5, sticky='e')
        self.WT_entry = ttk.Entry(parent)
        self.WT_entry.grid(row=1, column=1, padx=5, pady=5)
        
        calc_btn = ttk.Button(parent, text="محاسبه", command=self.calculate_part2)
        calc_btn.grid(row=2, column=0, columnspan=2, pady=10)
        
        self.result2 = ttk.Label(parent, text="نتیجه: ")
        self.result2.grid(row=3, column=0, columnspan=2)
    
    def create_part3_tab(self, parent):
        ttk.Label(parent, text="درصد مستربچ:").grid(row=0, column=0, padx=5, pady=5, sticky='e')
        self.mp_entry = ttk.Entry(parent)
        self.mp_entry.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(parent, text="وزن چیپس:").grid(row=1, column=0, padx=5, pady=5, sticky='e')
        self.CHW_entry = ttk.Entry(parent)
        self.CHW_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(parent, text="درصد روغن :").grid(row=2, column=0, padx=5, pady=5, sticky='e')
        self.OP_entry = ttk.Entry(parent)
        self.OP_entry.grid(row=2, column=1, padx=5, pady=5)
        
        calc_btn = ttk.Button(parent, text="محاسبه", command=self.calculate_part3)
        calc_btn.grid(row=3, column=0, columnspan=2, pady=10)
        
        self.result3 = ttk.Label(parent, text="نتیجه: ")
        self.result3.grid(row=4, column=0, columnspan=2)
    
    def create_part4_tab(self, parent):
        ttk.Label(parent, text="وزن تئوری محصول تولیدی:").grid(row=0, column=0, padx=5, pady=5, sticky='e')
        self.WTP_entry = ttk.Entry(parent)
        self.WTP_entry.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(parent, text="وزن بوبین کامل:").grid(row=1, column=0, padx=5, pady=5, sticky='e')
        self.WBH_entry = ttk.Entry(parent)
        self.WBH_entry.grid(row=1, column=1, padx=5, pady=5)
        
        calc_btn = ttk.Button(parent, text="محاسبه", command=self.calculate_part4)
        calc_btn.grid(row=2, column=0, columnspan=2, pady=10)
        
        self.result4 = ttk.Label(parent, text="نتیجه: ")
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
            result = CHW_var + (mp_var * CHW_var) + (CHW_var + OP_var)/10000
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
    
    def create_weaving_tab(self):
        category_frame = ttk.Frame(self.main_notebook)
        self.main_notebook.add(category_frame, text="تکسچره")
        
        sub_notebook = ttk.Notebook(category_frame)
        sub_notebook.pack(fill='both', expand=True, padx=5, pady=5)
        
        # Create 4 weaving tabs
        for i in range(4):
            frame = ttk.Frame(sub_notebook)
            sub_notebook.add(frame, text=f"تکسچره Tab {i+1}")
            self.create_dummy_tab(frame, f"محتوای تکسچره {i+1}")
    
    def create_finishing_tab(self):
        category_frame = ttk.Frame(self.main_notebook)
        self.main_notebook.add(category_frame, text="تابندگی")
        
        sub_notebook = ttk.Notebook(category_frame)
        sub_notebook.pack(fill='both', expand=True, padx=5, pady=5)
        
        # Create 4 finishing tabs
        for i in range(4):
            frame = ttk.Frame(sub_notebook)
            sub_notebook.add(frame, text=f"تابندگی Tab {i+1}")
            self.create_dummy_tab(frame, f"محتوای تابندگی {i+1}")
    
    def create_quality_tab(self):
        category_frame = ttk.Frame(self.main_notebook)
        self.main_notebook.add(category_frame, text="بافندگی")
        
        sub_notebook = ttk.Notebook(category_frame)
        sub_notebook.pack(fill='both', expand=True, padx=5, pady=5)
        
        # Create 4 quality tabs
        for i in range(4):
            frame = ttk.Frame(sub_notebook)
            sub_notebook.add(frame, text=f"بافندگی  Tab {i+1}")
            self.create_dummy_tab(frame, f"محتوای  بافندگی {i+1}")
    
    def create_dummy_tab(self, parent, content):
        # Placeholder content for other tabs
        label = ttk.Label(parent, text=f"این قسمت در حال توسعه است: {content}")
        label.pack(pady=50)
        
        entry = ttk.Entry(parent)
        entry.pack(pady=5)
        
        btn = ttk.Button(parent, text="دکمه نمونه", command=lambda: messagebox.showinfo("اطلاع", "این یک تب نمونه است"))
        btn.pack(pady=5)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()