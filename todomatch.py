#todos = []

while True:
    user_actions = input("type add, show, exit or edit: ")

    match user_actions:
        case "add":
            todo = input("enter todo: ") + "\n"

            with open('files/todos.txt', 'r') as file: #easier access to file
                todos = file.readlines()
            todos.append(todo)
            '''
            file = open('files/todos.txt', 'r') # automaticaly creates a List
            todos = file.readlines()
            file.close()
            '''
            with open('files/todos.txt', 'w') as file:
                file.writelines(todos)
            '''
            file = open('files/todos.txt', 'w') #opens txt file #w for write/r for read
            file.writelines(todos)
            file.close()
            '''
        case "show":
            with open('files/todos.txt', 'r') as file:
                todos = file.readlines()

            #new_todos = [item.strip('\n') for items in todos]

            for index, item in enumerate(todos): #enumerate to print both
                item = item.strip('\n')
                row = f"{index+1}-{item}" #f for style
                print(row)

        case "exit":
            print("exiting...")
            break
        case "edit":
            number = int(input("Number of todo to edit: "))
            number = number - 1

            with open('files/todos.txt', 'r') as file:
                todos = file.readlines()
            print("Here is todos exsisting", todos)

            new_todo = input("enter new todo: ")
            todos[number] = new_todo + '\n'

            print("Here is it how it will be", todos)

            with open('venv/todos.txt', 'w') as file:
                file.writelines(todos)

        case "complete":
            numberdel = int(input("Number of todo to complete: "))

            with open('files/todos.txt', 'r') as file:
                todos = file.readlines()
            index = numberdel - 1
            todo_to_remove = todos[index]
            todos.pop(index)

            with open('files/todos.txt', 'w') as file:
                file.writelines(todos)

            message = f"Todo: {todo_to_remove} was removed from the List."
            print(message)

        case "sort":
            todos.sort()
        case whatever:
            print("u entered a unknown command")