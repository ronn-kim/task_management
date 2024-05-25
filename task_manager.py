import os

TASK_FILE =  'tasks.txt'

def load_task():
    try:
        with open(TASK_FILE, 'r') as file:
            tasks = file.read().splitlines()
        return tasks
    except FileNotFoundError:
        return[]

def save_task(tasks):
    with open(TASK_FILE, 'w') as file:
        file.write("\n".join(tasks))
    


def display_task(tasks):
    if not tasks:
        print('not a task')
    else:
        print("\nTask:")
        for idx, tasks in enumerate(tasks, start=1):
            print(f"{idx}. {tasks}")
    print()

def add_tasks(tasks):
    task = input('enter new task')
    if task:
        tasks.append(task)
        save_task(task)
        print(f"task '{task}' added.")
    else:
        print('task cannot be empty')
    print()

def delete_task(tasks):
    display_task(tasks)
    try:

        task_id =int(input('enter task to delete'))
        if 0 <= task_id <len(tasks):
            removed = tasks.pop(task_id)
            save_task(tasks)
            print(f" task '{removed}' deleted")
        else:
            print('invalid task')
    except ValueError:
        print('please enter a valid value')
    print()

def main():
    while True:
        print('Task manager')
        print('1. Display task')
        print('2. Add Task')
        print('3. Delete Task')
        print('4. Exit')
        choice = input('choose an option: ').strip()

        tasks = load_task()

        if choice == '1':
            display_task(tasks)
        elif choice == '2':
            add_tasks(tasks)
        elif choice == '3':
            delete_task(tasks)
        elif choice == '4':
            print('goodbye! ')
            break
        else:
            print('Invalid choice. Please try again!.')
        print()

if __name__ == '__main__':
    main()

