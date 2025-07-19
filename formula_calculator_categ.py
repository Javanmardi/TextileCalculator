import tkinter as tk
from tkinter import ttk, messagebox
import math

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ماشین حساب نساجی")
        self.root.geometry("800x300")
        self.root.resizable(True, True)
        
        # Create main notebook for categories
        self.main_notebook = ttk.Notebook(root)
        self.main_notebook.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Create category frames
        self.create_melt_spinning_tab()
        self.create_texture_tab()
        self.create_radiance_tab()
        self.create_weaving_tab()

    #create_melt_spinning_tab    
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
        frame5 = ttk.Frame(sub_notebook)
        frame6 = ttk.Frame(sub_notebook)
        
        sub_notebook.add(frame1, text="وزن تئوری تولید در دقیقه")
        sub_notebook.add(frame2, text="وزن تئوری تولید در زمان فعالیت")
        sub_notebook.add(frame3, text="وزن تئوری محصول تولیدی")
        sub_notebook.add(frame4, text="تعداد بوبین کامل تئوری")
        sub_notebook.add(frame5, text="وزن ضایعات کل")
        sub_notebook.add(frame6, text="راندمان تولید")
        
        self.create_part1_tab(frame1)
        self.create_part2_tab(frame2)
        self.create_part3_tab(frame3)
        self.create_part4_tab(frame4)
        self.create_part5_tab(frame5)
        self.create_part6_tab(frame6)
        
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
    
    def create_part5_tab(self, parent):
        ttk.Label(parent, text="ضایعات ثابت  :").grid(row=0, column=0, padx=5, pady=5, sticky='e')
        self.CS_entry = ttk.Entry(parent)
        self.CS_entry.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(parent, text="وزن  ضایعات خط:").grid(row=1, column=0, padx=5, pady=5, sticky='e')
        self.LSW_entry = ttk.Entry(parent)
        self.LSW_entry.grid(row=1, column=1, padx=5, pady=5)
        
        calc_btn = ttk.Button(parent, text="محاسبه", command=self.calculate_part5)
        calc_btn.grid(row=2, column=0, columnspan=2, pady=10)
        
        self.result5 = ttk.Label(parent, text="نتیجه: ")
        self.result5.grid(row=3, column=0, columnspan=2)
    
    def create_part6_tab(self, parent):
        ttk.Label(parent, text="وزن محصول نهایی واقعی:").grid(row=0, column=0, padx=5, pady=5, sticky='e')
        self.WAP_entry = ttk.Entry(parent)
        self.WAP_entry.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(parent, text="وزن تئوری تولید در زمان فعالیت :").grid(row=1, column=0, padx=5, pady=5, sticky='e')
        self.WTA_entry = ttk.Entry(parent)
        self.WTA_entry.grid(row=1, column=1, padx=5, pady=5)
        
        calc_btn = ttk.Button(parent, text="محاسبه", command=self.calculate_part6)
        calc_btn.grid(row=2, column=0, columnspan=2, pady=10)
        
        self.result6 = ttk.Label(parent, text="نتیجه: ")
        self.result6.grid(row=3, column=0, columnspan=2)

    
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
    
    def calculate_part5(self):
        try:
            CS_var = float(self.CS_entry.get())
            LSW_var = float(self.LSW_entry.get())
            result = CS_var + LSW_var
            self.result5.config(text=f"جواب: {result:.2f}")
        except ValueError:
            messagebox.showerror("Error", "ورودی تعریف نشده! لطفا فقط عدد وارد کنید")
    
    def calculate_part6(self):
        try:
            WAP_var = float(self.WAP_entry.get())
            WTA_var = float(self.WTA_entry.get())
            result = WAP_var / WTA_var
            self.result6.config(text=f"جواب: {result:.2f}")
        except ValueError:
            messagebox.showerror("Error", "ورودی تعریف نشده! لطفا فقط عدد وارد کنید")

    #create_texture_tab
    def create_texture_tab(self):
        category_frame = ttk.Frame(self.main_notebook)
        self.main_notebook.add(category_frame, text="تکسچره")
        
        # Create sub-notebook for this category
        sub_notebook = ttk.Notebook(category_frame)
        sub_notebook.pack(fill='both', expand=True, padx=5, pady=5)
        

        # Create 4 tabs within category
        frame1 = ttk.Frame(sub_notebook)
        frame2 = ttk.Frame(sub_notebook)
        frame3 = ttk.Frame(sub_notebook)
        frame4 = ttk.Frame(sub_notebook)

        
        sub_notebook.add(frame1, text="وزن تئوری تولید (کیلوگرم)")
        sub_notebook.add(frame2, text="نمره نخ خروجی (دنیر)")
        sub_notebook.add(frame3, text="راندمان تولید (%)")
        sub_notebook.add(frame4, text="راندمان کیفی(%)")
        
        self.create_part7_tab(frame1)
        self.create_part8_tab(frame2)
        self.create_part9_tab(frame3)
        self.create_part10_tab(frame4)
    
    def create_part7_tab(self, parent):
        ttk.Label(parent, text="تعداد پوزیشن:").grid(row=0, column=0, padx=5, pady=5, sticky='e')
        self.NP_entry = ttk.Entry(parent)
        self.NP_entry.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(parent, text="مدت زمان تولید(دقیقه):").grid(row=1, column=0, padx=5, pady=5, sticky='e')
        self.PT_entry = ttk.Entry(parent)
        self.PT_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(parent, text="سرعت تولید (متر بر دقیقه):").grid(row=2, column=0, padx=5, pady=5, sticky='e')
        self.PV_entry = ttk.Entry(parent)
        self.PV_entry.grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(parent, text="نمره نخ خروجی (دنیر):").grid(row=3, column=0, padx=5, pady=5, sticky='e')
        self.ONT_entry = ttk.Entry(parent)
        self.ONT_entry.grid(row=3, column=1, padx=5, pady=5)

        calc_btn = ttk.Button(parent, text="محاسبه", command=self.calculate_part7)
        calc_btn.grid(row=4, column=0, columnspan=2, pady=10)
        
        self.result7 = ttk.Label(parent, text="نتیجه: ")
        self.result7.grid(row=5, column=0, columnspan=2)

    def create_part8_tab(self, parent):
        ttk.Label(parent, text="نمره نخ ورودی (دسی تکس):").grid(row=0, column=0, padx=5, pady=5, sticky='e')
        self.TIN_entry = ttk.Entry(parent)
        self.TIN_entry.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(parent, text="نسبت کشش:").grid(row=1, column=0, padx=5, pady=5, sticky='e')
        self.VR_entry = ttk.Entry(parent)
        self.VR_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(parent, text="درصد روغن:").grid(row=2, column=0, padx=5, pady=5, sticky='e')
        self.OR_entry = ttk.Entry(parent)
        self.OR_entry.grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(parent, text="درصد تغذیه کش (در صورت وجود):").grid(row=3, column=0, padx=5, pady=5, sticky='e')
        self.FVP_entry = ttk.Entry(parent)
        self.FVP_entry.grid(row=3, column=1, padx=5, pady=5)

        ttk.Label(parent, text="نمره کش (در صورت وجود):").grid(row=4, column=0, padx=5, pady=5, sticky='e')
        self.VN_entry = ttk.Entry(parent)
        self.VN_entry.grid(row=4, column=1, padx=5, pady=5)
        
        calc_btn = ttk.Button(parent, text="محاسبه", command=self.calculate_part8)
        calc_btn.grid(row=5, column=0, columnspan=2, pady=10)
        
        self.result8 = ttk.Label(parent, text="نتیجه: ")
        self.result8.grid(row=6, column=0, columnspan=2)

    def create_part9_tab(self, parent):
        ttk.Label(parent, text="میزان نخ تولید شده واقعی (کیلوگرم):").grid(row=0, column=0, padx=5, pady=5, sticky='e')
        self.TROA_entry = ttk.Entry(parent)
        self.TROA_entry.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(parent, text="وزن تئوری تولید (کیلوگرم):").grid(row=1, column=0, padx=5, pady=5, sticky='e')
        self.PTWK_entry = ttk.Entry(parent)
        self.PTWK_entry.grid(row=1, column=1, padx=5, pady=5)
        
        calc_btn = ttk.Button(parent, text="محاسبه", command=self.calculate_part9)
        calc_btn.grid(row=2, column=0, columnspan=2, pady=10)
        
        self.result9 = ttk.Label(parent, text="نتیجه: ")
        self.result9.grid(row=3, column=0, columnspan=2)

    def create_part10_tab(self, parent):
        ttk.Label(parent, text="میزان نخ تولید شده واقعی (کیلوگرم):").grid(row=0, column=0, padx=5, pady=5, sticky='e')
        self.RTA_entry = ttk.Entry(parent)
        self.RTA_entry.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(parent, text="میزان درجات کیفی تولید شده (کیلوگرم):").grid(row=1, column=0, padx=5, pady=5, sticky='e')
        self.ADQP_entry = ttk.Entry(parent)
        self.ADQP_entry.grid(row=1, column=1, padx=5, pady=5)

        
        calc_btn = ttk.Button(parent, text="محاسبه", command=self.calculate_part10)
        calc_btn.grid(row=2, column=0, columnspan=2, pady=10)
        
        self.result10 = ttk.Label(parent, text="نتیجه: ")
        self.result10.grid(row=3, column=0, columnspan=2)

    def calculate_part7(self):
        try:
            NP_entry_var = float(self.NP_entry.get())
            PT_entry_var = float(self.PT_entry.get())
            PV_entry_var = float(self.PV_entry.get())
            ONT_entry_var = float(self.ONT_entry.get())
            
            result = (PV_entry_var * PT_entry_var * NP_entry_var*ONT_entry_var)/9000000
            self.result7.config(text=f"جواب: {result:.2f}")
        except ValueError:
            messagebox.showerror("Error", "ورودی تعریف نشده! لطفا فقط عدد وارد کنید")
    
    def calculate_part8(self):
        try:
            TIN_entry_var = float(self.TIN_entry.get())
            VR_entry_var = float(self.VR_entry.get())
            OR_entry_var = float(self.OR_entry.get())
            FVP_entry_var = float(self.FVP_entry.get())
            VN_entry_var = float(self.VN_entry.get())
            
            result = ((TIN_entry_var*0.9)/VR_entry_var)+((OR_entry_var/100)*(TIN_entry_var/VR_entry_var)+((FVP_entry_var/100)*VN_entry_var))
            self.result8.config(text=f"جواب: {result:.2f}")
        except ValueError:
            messagebox.showerror("Error", "ورودی تعریف نشده! لطفا فقط عدد وارد کنید")

    def calculate_part9(self):
        try:
            TROA_entry_var = float(self.TROA_entry.get())
            PTWK_entry_var = float(self.PTWK_entry.get())
            
            result = (TROA_entry_var/PTWK_entry_var)*100
            self.result9.config(text=f"جواب: {result:.2f}")
        except ValueError:
            messagebox.showerror("Error", "ورودی تعریف نشده! لطفا فقط عدد وارد کنید")

    def calculate_part10(self):
        try:
            RTA_entry_var = float(self.RTA_entry.get())
            ADQP_entry_var = float(self.ADQP_entry.get())
            
            result =100-((ADQP_entry_var/RTA_entry_var)*100)
            self.result10.config(text=f"جواب: {result:.2f}")
        except ValueError:
            messagebox.showerror("Error", "ورودی تعریف نشده! لطفا فقط عدد وارد کنید")

    #create_radiance_tab
    def create_radiance_tab(self):
        category_frame = ttk.Frame(self.main_notebook)
        self.main_notebook.add(category_frame, text="تابندگی")
        
        # Create sub-notebook for this category
        sub_notebook = ttk.Notebook(category_frame)
        sub_notebook.pack(fill='both', expand=True, padx=5, pady=5)

        # Create 4 tabs within category
        frame1 = ttk.Frame(sub_notebook)
        frame2 = ttk.Frame(sub_notebook)
        
        sub_notebook.add(frame1, text="تعداد تاب در متر")
        sub_notebook.add(frame2, text="نمره نخ خروجی")

        
        self.create_part11_tab(frame1)
        self.create_part12_tab(frame2)

    def create_part11_tab(self, parent):
        ttk.Label(parent, text="سرعت برداشت :").grid(row=0, column=0, padx=5, pady=5, sticky='e')
        self.VC_entry = ttk.Entry(parent)
        self.VC_entry.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(parent, text="سرعت تویستر :").grid(row=1, column=0, padx=5, pady=5, sticky='e')
        self.VTS_entry = ttk.Entry(parent)
        self.VTS_entry.grid(row=1, column=1, padx=5, pady=5)

        calc_btn = ttk.Button(parent, text="محاسبه", command=self.calculate_part11)
        calc_btn.grid(row=2, column=0, columnspan=2, pady=10)
        
        self.result11 = ttk.Label(parent, text="نتیجه: ")
        self.result11.grid(row=3, column=0, columnspan=2)

    def create_part12_tab(self, parent):
        ttk.Label(parent, text="نمره نخ ورودی:").grid(row=0, column=0, padx=5, pady=5, sticky='e')
        self.ETN_entry = ttk.Entry(parent)
        self.ETN_entry.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(parent, text="تعداد تاب در متر:").grid(row=1, column=0, padx=5, pady=5, sticky='e')
        self.TNM_entry = ttk.Entry(parent)
        self.TNM_entry.grid(row=1, column=1, padx=5, pady=5)

        calc_btn = ttk.Button(parent, text="محاسبه", command=self.calculate_part12)
        calc_btn.grid(row=2, column=0, columnspan=2, pady=10)
        
        self.result12 = ttk.Label(parent, text="نتیجه: ")
        self.result12.grid(row=3, column=0, columnspan=2)


    def calculate_part11(self):
        try:
            VC_entry_var = float(self.VC_entry.get())
            VTS_entry_var = float(self.VTS_entry.get())
            
            result = VTS_entry_var / VC_entry_var
            self.result11.config(text=f"جواب: {result:.2f}")
        except ValueError:
            messagebox.showerror("Error", "ورودی تعریف نشده! لطفا فقط عدد وارد کنید")

    def calculate_part12(self):
        try:
            ETN_entry_var = float(self.ETN_entry.get())
            TNM_entry_var = float(self.TNM_entry.get())
            
            result = ETN_entry_var+(ETN_entry_var*(TNM_entry_var/35000))
            self.result12.config(text=f"جواب: {result:.2f}")
        except ValueError:
            messagebox.showerror("Error", "ورودی تعریف نشده! لطفا فقط عدد وارد کنید")

    
    #create_weaving_tab (PENDING)
    def create_weaving_tab(self):
        category_frame = ttk.Frame(self.main_notebook)
        self.main_notebook.add(category_frame, text="بافندگی")
        
        # Create sub-notebook for this category
        sub_notebook = ttk.Notebook(category_frame)
        sub_notebook.pack(fill='both', expand=True, padx=5, pady=5)
        

        # Create 4 tabs within category
        frame1 = ttk.Frame(sub_notebook)
        frame2 = ttk.Frame(sub_notebook)
        frame3 = ttk.Frame(sub_notebook)

        
        sub_notebook.add(frame1, text="وزن گرد بر")
        sub_notebook.add(frame2, text="وزن متر طول")
        sub_notebook.add(frame3, text="تعداد رشته نخ چله پیچی ")
    
        
        self.create_part13_tab(frame1)
        self.create_part14_tab(frame2)
        self.create_part15_tab(frame3)
   
    def create_part13_tab(self, parent):
        ttk.Label(parent, text=" تراکم پود :").grid(row=0, column=0, padx=5, pady=5, sticky='e')
        self.TPP_entry = ttk.Entry(parent)
        self.TPP_entry.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(parent, text="نمره تار :").grid(row=1, column=0, padx=5, pady=5, sticky='e')
        self.TNN_entry = ttk.Entry(parent)
        self.TNN_entry.grid(row=1, column=1, padx=5, pady=5)
        
        ttk.Label(parent, text="نمره پود:").grid(row=2, column=0, padx=5, pady=5, sticky='e')
        self.PNN_entry = ttk.Entry(parent)
        self.PNN_entry.grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(parent, text=" تراکم تار:").grid(row=3, column=0, padx=5, pady=5, sticky='e')
        self.TTT_entry = ttk.Entry(parent)
        self.TTT_entry.grid(row=3, column=1, padx=5, pady=5)

        calc_btn = ttk.Button(parent, text="محاسبه", command=self.calculate_part13)
        calc_btn.grid(row=4, column=0, columnspan=2, pady=10)
        
        self.result13 = ttk.Label(parent, text="نتیجه: ")
        self.result13.grid(row=5, column=0, columnspan=2)
    
    def calculate_part13(self):
        try:
            TNN_entry_var = float(self.TNN_entry.get())
            PNN_entry_var = float(self.PNN_entry.get())
            TTT_entry_var = float(self.TTT_entry.get())
            TPP_entry_var = float(self.TPP_entry.get())
            
            
            result = (TPP_entry_var*PNN_entry_var/9000)*(TTT_entry_var*TNN_entry_var/9000)*1.05
            self.result13.config(text=f"جواب: {result:.2f}")
        except ValueError:
            messagebox.showerror("Error", "ورودی تعریف نشده! لطفا فقط عدد وارد کنید")

    def create_part14_tab(self, parent):
        ttk.Label(parent, text=" عرض:").grid(row=0, column=0, padx=5, pady=5, sticky='e')
        self.WWV_entry = ttk.Entry(parent)
        self.WWV_entry.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(parent, text="وزن گرد بر").grid(row=1, column=0, padx=5, pady=5, sticky='e')
        self.WRC_entry = ttk.Entry(parent)
        self.WRC_entry.grid(row=1, column=1, padx=5, pady=5)

        calc_btn = ttk.Button(parent, text="محاسبه", command=self.calculate_part14)
        calc_btn.grid(row=2, column=0, columnspan=2, pady=10)
        
        self.result14 = ttk.Label(parent, text="نتیجه: ")
        self.result14.grid(row=3, column=0, columnspan=2)
    
    def calculate_part14(self):
        try:
            WWV_entry_var = float(self.WWV_entry.get())
            WRC_entry_var = float(self.WRC_entry.get())

            
            
            result = WRC_entry_var*WWV_entry_var
            self.result14.config(text=f"جواب: {result:.2f}")
        except ValueError:
            messagebox.showerror("Error", "ورودی تعریف نشده! لطفا فقط عدد وارد کنید")

    def create_part15_tab(self, parent):
        ttk.Label(parent, text=" ظرفیت قفسه :").grid(row=0, column=0, padx=5, pady=5, sticky='e')
        self.SCC_entry = ttk.Entry(parent)
        self.SCC_entry.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(parent, text="تعداد سرنخ کل :").grid(row=1, column=0, padx=5, pady=5, sticky='e')
        self.TNTN_entry = ttk.Entry(parent)
        self.TNTN_entry.grid(row=1, column=1, padx=5, pady=5)
        
        calc_btn = ttk.Button(parent, text="محاسبه", command=self.calculate_part15)
        calc_btn.grid(row=2, column=0, columnspan=2, pady=10)
        
        self.result15 = ttk.Label(parent, text="نتیجه: ")
        self.result15.grid(row=3, column=0, columnspan=2)
    
    def calculate_part15(self):
        try:
            SCC_entry_var = float(self.SCC_entry.get())
            TNTN_entry_var = float(self.TNTN_entry.get())

            

            result = TNTN_entry_var//((TNTN_entry_var//SCC_entry_var)+1)
            self.result15.config(text=f"جواب: {result:.2f}")
        except ValueError:
            messagebox.showerror("Error", "ورودی تعریف نشده! لطفا فقط عدد وارد کنید")



    # def create_dummy_tab(self, parent, content):
    #     # Placeholder content for other tabs
    #     label = ttk.Label(parent, text=f"این قسمت در حال توسعه است: {content}")
    #     label.pack(pady=50)
        
    #     entry = ttk.Entry(parent)
    #     entry.pack(pady=5)
        
    #     btn = ttk.Button(parent, text="دکمه نمونه", command=lambda: messagebox.showinfo("اطلاع", "این یک تب نمونه است"))
    #     btn.pack(pady=5)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()