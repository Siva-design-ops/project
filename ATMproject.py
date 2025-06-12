import tkinter as tk
from tkinter import messagebox, simpledialog


class ATMApp:
    def __init__(self,root):
        self.root=root
        self.root.title("ATM Machine")
        self.balance=1000.00
        self.pin="1234"
        self.create_login_screen()
    def create_login_screen(self):
        self.clear_screen()
        tk.Label(self.root,text="Enter PIN",font=("Arial",14)).pack(pady=10)
        self.pin_entry=tk.Entry(self.root,show="*",font=("Arial",14))
        self.pin_entry.pack(pady=5)
        tk.Button(self.root,text="Login",command=self.check_pin,font=("Arial",12)).pack(pady=10)
    def check_pin(self):
        if self.pin_entry.get()==self.pin:
            self.create_main_menu()
        else:
            messagebox.showerror("error","Incorrect PIN")
            
    def create_main_menu(self):
        self.clear_screen()
        tk.Label(self.root,text="ATM Main Menu",font=("Arial",16,"bold")).pack(pady=10)
        tk.Button(self.root,text="Check Balance",command=self.check_balance,width=20).pack(pady=5)
        tk.Button(self.root,text="Deposit",command=self.deposit,width=20).pack(pady=5)
        tk.Button(self.root,text="Withdraw",command=self.withdraw,width=20).pack(pady=5)
        tk.Button(self.root,text="Change pin",command=self.change_pin,width=20).pack(pady=5)
        tk.Button(self.root,text="Logout",command=self.create_login_screen,width=20).pack(pady=5)
    def check_balance(self):
        messagebox.showinfo("Balance",f"your balance is ₹{self.balance:.2f}")

        
    def deposit(self):
        try:
            amount=float(simpledialog.askstring("Deposit","Enter amount to deposit:"))
            if amount>0:
                self.balance+=amount
                messagebox.showinfo("Success",f"₹{amount:.2f} deposited succesfully")
            else:
                messagebox.showerror("Error","Enter a valid amount:")
        except:
            messagebox.showerror("Error","Invalid input")

            
    def withdraw(self):
        try:
            amount=float(simpledialog.askstring("withdraw","Enter amount to withdraw:"))
            if 0<amount<=self.balance:
                self.balance-=amount
                messagebox.showinfo("success",f"{amount:.2f} withdrawn successfully.")
            else:
                messagebox.showerror("Error","Insufficient balance or invalid amount.")
        except:
            messagebox.showerror("error","Invalid input.")

            
    def change_pin(self):
        current=simpledialog.askstring("change PIN","Enter current PIN:")
        if current==self.pin:
            new_pin=simpledialog.askstring("change PIN","Enter new PIN:")
            if new_pin:
                self.pin=new_pin
                messagebox.showinfo("Success","New PIN Changed successfully")
            else:
                messagebox.showerror("Error","New pin Cannot be empty")
        else:
            messagebox.showerror("Error","Incorrect Current PIN")

            
    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__=="__main__":
    root=tk.Tk()
    root.geometry("300x300")
    app=ATMApp(root)
    root.mainloop()
