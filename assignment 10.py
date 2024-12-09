import tkinter as tk
from tkinter import messagebox

class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Task Manager")
        self.root.geometry("600x600")
        self.root.config(bg="#8B0000")  # Soft beige background

        # Task list
        self.tasks = []

        # Title Label
        self.title_label = tk.Label(self.root, text="Task Manager", font=("Papyrus", 35, "bold"), bg="#F2E3D5", fg="BLACK")  # Purple text
        self.title_label.pack(pady=20)

        # Task Entry
        self.task_entry_label = tk.Label(self.root, text="Enter Task:", bg="#F2E3D5", font=("Segoe", 18, "bold"), fg="#8A2BE2")  # Soft purple label
        self.task_entry_label.pack(pady=5)
        self.task_entry = tk.Entry(self.root, font=("Rockwell", 18), width=35, bd=3, fg="black", bg="#F8F8FF")  # Off-white background
        self.task_entry.pack(pady=10)

        # Add Task Button
        self.add_button = tk.Button(self.root, text="Add Task", font=("Algerian", 18, "bold"), bg="#3498db", fg="white", command=self.add_task)
        self.add_button.pack(pady=10)

        # Scrollbar
        self.scrollbar = tk.Scrollbar(self.root)

        # Task Listbox
        self.task_listbox = tk.Listbox(self.root, width=50, height=10, font=("Segoe", 14), selectmode=tk.SINGLE, bd=3, fg="black", bg="#F8F8FF", yscrollcommand=self.scrollbar.set)
        self.task_listbox.pack(pady=20)

        # Configure the scrollbar to be linked to the listbox
        self.scrollbar.config(command=self.task_listbox.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Task Control Buttons
        self.mark_complete_button = tk.Button(self.root, text="Mark as Completed", font=("Algerian", 14, "bold"), bg="#27ae60", fg="white", command=self.mark_as_completed)
        self.mark_complete_button.pack(pady=5)

        self.delete_button = tk.Button(self.root, text="Delete Task", font=("Algerian", 14, "bold"), bg="#e74c3c", fg="white", command=self.delete_task)
        self.delete_button.pack(pady=5)

        self.view_button = tk.Button(self.root, text="View All Tasks", font=("Algerian", 14, "bold"), bg="#f39c12", fg="white", command=self.view_all_tasks)
        self.view_button.pack(pady=5)

    def add_task(self):
        task = self.task_entry.get()
        if task != "":
            self.tasks.append({"task": task, "completed": False})
            self.task_entry.delete(0, tk.END)
            self.view_all_tasks()
        else:
            messagebox.showwarning("Input Error", "Please enter a task.")

    def mark_as_completed(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task_index = selected_task_index[0]
            self.tasks[task_index]["completed"] = True
            self.view_all_tasks()
        else:
            messagebox.showwarning("Selection Error", "Please select a task to mark as completed.")

    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task_index = selected_task_index[0]
            del self.tasks[task_index]
            self.view_all_tasks()
        else:
            messagebox.showwarning("Selection Error", "Please select a task to delete.")

    def view_all_tasks(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            task_str = f"{task['task']} - {'Completed' if task['completed'] else 'Pending'}"
            self.task_listbox.insert(tk.END, task_str)


if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()

