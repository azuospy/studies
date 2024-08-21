import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tarefas")

        self.tasks = []

        # Frame para a lista de tarefas
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=10)

        # Caixa de entrada para novas tarefas
        self.task_entry = tk.Entry(self.frame, width=40)
        self.task_entry.pack(side=tk.LEFT, padx=10)

        # Botão para adicionar tarefa
        self.add_button = tk.Button(self.frame, text="Adicionar", command=self.add_task)
        self.add_button.pack(side=tk.LEFT)

        # Lista de tarefas
        self.task_listbox = tk.Listbox(self.root, width=50, height=10)
        self.task_listbox.pack(pady=10)

        # Botão para remover tarefa
        self.remove_button = tk.Button(self.root, text="Remover Selecionada", command=self.remove_task)
        self.remove_button.pack()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.update_task_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Entrada Inválida", "Digite uma tarefa para adicionar.")

    def remove_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            self.tasks.pop(selected_task_index[0])
            self.update_task_listbox()
        else:
            messagebox.showwarning("Seleção Inválida", "Selecione uma tarefa para remover.")

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
