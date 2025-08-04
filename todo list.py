import tkinter as tk
from tkinter import messagebox, filedialog

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("400x400")
        self.tasks = []
        # edhi entry part.
        self.task_entry = tk.Entry(self.root, width=40)
        self.task_entry.pack(pady=10)
        # entrypart ki button echanu.
        tk.Button(self.root, text="Add Task", command=self.add_task).pack()

        # edhi listbox part.
        self.task_listbox = tk.Listbox(self.root, width=50, height=10)
        self.task_listbox.pack(pady=10)
        # listbox ki echina buttons.
        tk.Button(self.root, text="Delete Selected", command=self.delete_task).pack(pady=5)
        tk.Button(self.root, text="Clear All", command=self.clear_tasks).pack(pady=5)
        tk.Button(self.root, text="Save Tasks", command=self.save_tasks).pack(pady=5)
        tk.Button(self.root, text="Load Tasks", command=self.load_tasks).pack(pady=5)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.update_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter a task")

    def delete_task(self):
        selected = self.task_listbox.curselection()
        if selected:
            index = selected[0]
            del self.tasks[index]
            self.update_listbox()
        else:
            messagebox.showwarning("Selection Error", "Please select a task to delete")

    def clear_tasks(self):
        if messagebox.askyesno("Confirm", "Clear all tasks?"):
            self.tasks.clear()
            self.update_listbox()

    def save_tasks(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[("Text Files"," ")])
        if file_path:
            with open(file_path, 'w') as file:
                for task in self.tasks:
                    file.write(task + "\n")
            messagebox.showinfo("Success", "Tasks saved successfully")

    def load_tasks(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files"," ")])
        if file_path:
            with open(file_path, 'r') as file:
                self.tasks = [line.strip() for line in file.readlines()]
            self.update_listbox()

    def update_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

#app ni run cheyantaniki edhi.
if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
