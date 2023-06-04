import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime

#Mendefinisikan class
class BudgetBuddyApp:
    #constructor mengambil argumen 'root' yang mempresentasikan root window program
    #memberi judul root window
    def __init__(self, root):
        self.root = root
        self.root.title("Budget Buddy")

        #membuat objek ttk untuk widget bertema
        self.style = ttk.Style()

        #mengatur style tabel
        self.style.configure("Treeview.Heading", font=("bold"), foreground="#7C5A4E")
        self.style.configure("Treeview", foreground="#7C5A50")

        #menginisialisasi method current_page kosong
        self.current_page = None
        #menginisialisasi list kosong untuk data budget dan expense
        self.budget_data = []
        self.expense_data = []

        #memanggil method yang digunakan untuk membuat halaman utama
        self.create_main_page()

    def create_main_page(self):
        #Memeriksa apabila ada instansi dari current_page
        if self.current_page:
            #Menyembunyikan current_page jika ada
            self.current_page.destroy()

        #Membuat frame current_page   
        self.current_page = tk.Frame(self.root)
        #mengatur warna frame
        self.current_page.configure(bg="#FCDFC1")

        title_label = tk.Label(self.current_page,
                               text="Budget Buddy",
                               font=("Lucida Calligraphy", 24, "bold"),
                               bg="#FCDFC1", fg="#7C5A4E")
        title_label.pack(pady=30)

        budget_button = tk.Button(self.current_page,
                                  text="Budget",
                                  font=("Lucida Calligraphy", 12),
                                  width=18,
                                  height=2,
                                  bg="#7C5A4E", fg="white",
                                  command=self.create_budget_page)
        budget_button.pack(pady=45)

        expense_button = tk.Button(self.current_page,
                                   text="Expense",
                                   font=("Lucida Calligraphy", 12),
                                   width=18,
                                   height=2,
                                   bg="#7C5A4E", fg="white",
                                   command=self.create_expense_page)
        expense_button.pack()

        exit_button = tk.Button(self.current_page,
                                text="Exit",
                                font=("Lucida Calligraphy", 12),
                                width=18,
                                height=2,
                                bg="#7C5A4E", fg="white",
                                command=self.root.quit)
        exit_button.pack(pady=45)

        #menampilkan current_page 
        self.current_page.pack(fill=tk.BOTH, expand=True)

    def create_budget_page(self):
        #Memeriksa apabila ada instansi dari current_page
        if self.current_page:
            self.current_page.destroy()

        self.current_page = tk.Frame(self.root)
        self.current_page.configure(bg="#FCDFC1")

        title_label = tk.Label(self.current_page,
                               text="Budget Page",
                               font=("Lucida Calligraphy", 20, "bold"),
                               bg="#FCDFC1", fg="#7C5A4E")
        title_label.pack(pady=10)

        period_label = tk.Label(self.current_page,
                                text="Period:",
                                font=("Lucida Calligraphy", 10),
                                bg="#FCDFC1", fg="#7C5A4E")
        period_label.pack()

        #mengambil bulan dan tahun saat ini dalam format Bulan Tahun
        current_month_year = datetime.now().strftime("%B %Y")
        #membuat entry untuk period
        period_entry = tk.Entry(self.current_page)
        #mengisi entry period dengan variabel current_month_year
        period_entry.insert(tk.END, current_month_year)
        period_entry.pack()

        category_label = tk.Label(self.current_page,
                                  text="Category:",
                                  font=("Lucida Calligraphy", 10),
                                  bg="#FCDFC1", fg="#7C5A4E")
        category_label.pack()

        category_entry = tk.Entry(self.current_page)
        category_entry.pack()

        amount_label = tk.Label(self.current_page,
                                text="Amount:",
                                font=("Lucida Calligraphy", 10),
                                bg="#FCDFC1", fg="#7C5A4E")
        amount_label.pack()

        amount_entry = tk.Entry(self.current_page)
        amount_entry.pack()

        add_button = tk.Button(self.current_page, 
                       text="Add", 
                       width=10, 
                       font=("Lucida Calligraphy", 10),
                       bg="#7C5A4E", fg="white",
                       command=lambda: self.add_budget_item(period_entry.get(), category_entry.get(), amount_entry.get()) 
                          if validate_amount(amount_entry.get()) else messagebox.showerror("Error", "Invalid amount"))
        add_button.pack(pady=10)
        
         #memeriksa apakah amount float 
        def validate_amount(value):
            try:
                float(value)
                return True
            except ValueError:
                return False

        budget_table = ttk.Treeview(self.current_page, columns=("Period", "Category", "Amount"), show="headings")
        budget_table.heading("Period", text="Period")
        budget_table.heading("Category", text="Category")
        budget_table.heading("Amount", text="Amount")
        budget_table.pack(pady=10)

        periods = set()
        for data in self.budget_data:
            if data["Period"] not in periods:
                periods.add(data["Period"])
                budget_table.insert("", tk.END, values=(data["Period"], data["Category"], data["Amount"]))
            else:
                budget_table.insert("", tk.END, values=("", data["Category"], data["Amount"]))

        exit_button = tk.Button(self.current_page,
                                text="Exit",
                                width=10,
                                font=("Lucida Calligraphy", 10),
                                bg="#7C5A4E", fg="white",
                                command=self.create_main_page)
        exit_button.pack(pady=10)

        self.current_page.pack(fill=tk.BOTH, expand=True)

    def create_expense_page(self):
        if self.current_page:
            self.current_page.destroy()

        self.current_page = tk.Frame(self.root)
        self.current_page.configure(bg="#FCDFC1")

        title_label = tk.Label(self.current_page,
                               text="Expense Page",
                               font=("Lucida Calligraphy", 20, "bold"),
                               bg="#FCDFC1", fg="#7C5A4E")
        title_label.pack(pady=10)

        date_label = tk.Label(self.current_page,
                              text="Date:",
                              font=("Lucida Calligraphy", 10),
                              bg="#FCDFC1", fg="#7C5A4E")
        date_label.pack()

        #mengambil tanggal saat ini dan ditampilkan dengan urutan tahun-bulan-tanggal
        current_date = datetime.now().strftime("%Y-%m-%d")
        date_entry = tk.Entry(self.current_page)
        date_entry.insert(tk.END, current_date)
        date_entry.pack()

        category_label = tk.Label(self.current_page,
                                  text="Category:",
                                  font=("Lucida Calligraphy", 10),
                                  bg="#FCDFC1", fg="#7C5A4E")
        category_label.pack()

        category_entry = tk.Entry(self.current_page)
        category_entry.pack()

        amount_label = tk.Label(self.current_page,
                                text="Amount:",
                                font=("Lucida Calligraphy", 10),
                                bg="#FCDFC1", fg="#7C5A4E")
        amount_label.pack()

        amount_entry = tk.Entry(self.current_page)
        amount_entry.pack()

        note_label = tk.Label(self.current_page,
                              text="Note:",
                              font=("Lucida Calligraphy", 10),
                              bg="#FCDFC1", fg="#7C5A4E")
        note_label.pack()

        note_entry = tk.Entry(self.current_page)
        note_entry.pack()

        add_button = tk.Button(self.current_page,
                       text="Add",
                       width=10,
                       font=("Lucida Calligraphy", 10),
                       bg="#7C5A4E", fg="white",
                       command=lambda: self.add_expense_item(date_entry.get(), category_entry.get(), amount_entry.get(), note_entry.get())
                          if validate_amount(amount_entry.get()) else messagebox.showerror("Error", "Invalid amount"))
        add_button.pack(pady=10)

        #memeriksa apakah amount sebuah float
        def validate_amount(value):
            try:
                float(value)
                return True
            except ValueError: 
                return False

        expense_table = ttk.Treeview(self.current_page, columns=("Date", "Category", "Amount", "Note"), show="headings")
        expense_table.heading("Date", text="Date")
        expense_table.heading("Category", text="Category")
        expense_table.heading("Amount", text="Amount")
        expense_table.heading("Note", text="Note")
        expense_table.pack(pady=10)

        dates = set()
        for data in self.expense_data:
            if data["Date"] not in dates:
                dates.add(data["Date"])
                expense_table.insert("", tk.END, values=(data["Date"], data["Category"], data["Amount"], data["Note"]))
            else:
                expense_table.insert("", tk.END, values=("", data["Category"], data["Amount"], data["Note"]))

        total_expense = sum(float(data["Amount"]) for data in self.expense_data)
        total_label = tk.Label(self.current_page,
                               text="Total Expense: {:.2f}".format(total_expense),
                               bg="#FCDFC1", fg="#7C5A4E")
        total_label.pack()

        exit_button = tk.Button(self.current_page,
                                text="Exit",
                                width=10,
                                font=("Lucida Calligraphy", 10),
                                bg="#7C5A4E", fg="white",
                                command=self.create_main_page)
        exit_button.pack(pady=10)

        self.current_page.pack(fill=tk.BOTH, expand=True)

    def add_budget_item(self, period, category, amount):
        if period and category and amount:
            self.budget_data.append({"Period": period, "Category": category, "Amount": amount})
            self.create_budget_page()
        else:
            messagebox.showerror("Error", "Please fill in all fields.")

    def add_expense_item(self, date, category, amount, note):
        if date and category and amount:
            self.expense_data.append({"Date": date, "Category": category, "Amount": amount, "Note": note})
            self.update_budget(category, amount)
            self.create_expense_page()
        else:
            messagebox.showerror("Error", "Please fill in all fields.")

    def update_budget(self, category, expense_amount):
        for data in self.budget_data:
            if data["Category"] == category:
                data["Amount"] = str(float(data["Amount"]) - float(expense_amount))
                break

if __name__ == "__main__":
    root = tk.Tk()
    app = BudgetBuddyApp(root)
    root.geometry("900x700")
    root.mainloop()
