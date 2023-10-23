from datetime import datetime
import csv

now = datetime.now()
time_string = now.strftime("%d-%b-%Y %H:%M:%S")

datas = []

class Task:
    date = time_string
    counter = 1
    def __init__(self, title, body):
        self.task_date = self.date
        self.num = Task.counter
        self.title = title
        self.body = body
        datas.append(self)
        Task.counter += 1

    def __str__(self):
        return f"{self.num}.-\n{self.title}\n{self.body}\n---------------------\n{self.task_date}\n---------------------"
    
    def delete_task(self):
        print(f"{self.num} has been remove")
        datas.remove(self)



def main():
    load_from_csv()
    while True:
        print("Welcome to your Task List\n")
        display_task()
        print("\nWhat would you like to do")
        print("1. + Add Task")
        print("2. - Remove Task")
        print("3. Exit")
        choice = input()

        if choice == "1":
            title = input("Task title: ")
            body = input("Task content: ")
            task = Task(title, body)
            print("Task added")
        
        if choice == "2":
            select = int(input("Which taks would you like to remove: "))
            selected_task = find_task(select)
            if selected_task:
                selected_task.delete_task()
        
        if choice == "3":
            print("Tasks has been save in pc")
            save_to_csv()
            break

def find_task(n):
    for data in datas:
        if data.num == n:
            return data

def display_task():
    if len(datas) == 0:
        print("There's no task add yet")
    else:
        for data in datas:
            print(data)

def save_to_csv():
    with open("Task.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Task number", "Task title", "Task content", "Date created"])
        for data in datas:
            writer.writerow([data.num, data.title, data.body, data.task_date])

def load_from_csv():
    try:
        with open("Task.csv", mode="r") as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            for row in reader:
                task_num, task_title, task_body, task_date = row
                task = Task(task_title, task_body)
                task.num = int(task_num)
                task.task_date = task_date
    except FileNotFoundError:
        print("There's no tasks saved. System will created a file to stored them")

if __name__ == "__main__":
    main()
