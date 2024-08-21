import json
import os

# Nome do arquivo onde as tarefas serão armazenadas
TASKS_FILE = 'tasks.json'

# Função para carregar as tarefas do arquivo
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)
    return []

# Função para salvar as tarefas no arquivo
def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

# Função para exibir a lista de tarefas
def show_tasks(tasks):
    if not tasks:
        print("Nenhuma tarefa encontrada!")
        return
    print("\nLista de Tarefas:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

# Função para adicionar uma tarefa
def add_task(tasks):
    task = input("Digite a nova tarefa: ")
    tasks.append(task)
    save_tasks(tasks)
    print("Tarefa adicionada!")

# Função para remover uma tarefa
def remove_task(tasks):
    show_tasks(tasks)
    try:
        index = int(input("Digite o número da tarefa a ser removida: ")) - 1
        if 0 <= index < len(tasks):
            tasks.pop(index)
            save_tasks(tasks)
            print("Tarefa removida!")
        else:
            print("Número inválido!")
    except ValueError:
        print("Entrada inválida!")

# Função principal para o menu
def main():
    tasks = load_tasks()
    
    while True:
        print("\nMenu:")
        print("1. Mostrar Tarefas")
        print("2. Adicionar Tarefa")
        print("3. Remover Tarefa")
        print("4. Sair")

        choice = input("Escolha uma opção (1/2/3/4): ")

        if choice == '1':
            show_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
