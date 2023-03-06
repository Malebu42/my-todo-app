def get_todos():
    with open('files/todos.txt', 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

while True:
    user_action = input("type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = get_todos()
        todos.append(todo + '\n')
        '''
        with open('files/todos.txt', 'r') as file: #easier access to file
            todos = file.readlines()
        todos.append(todo)
              
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
    elif user_action.startswith("show"):
        with open('files/todos.txt', 'r') as file:
            todos = file.readlines()

        # new_todos = [item.strip('\n') for items in todos]

        for index, item in enumerate(todos):  # enumerate to print both
            item = item.strip('\n')
            row = f"{index + 1}-{item}"  # f for style
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = get_todos()
            print("Here is todos exsisting", todos)

            new_todo = input("enter new todo: ")
            todos[number] = new_todo + '\n'

            print("Here is it how it will be", todos)

            with open('venv/todos.txt', 'w') as file:
                file.writelines(todos)
        except ValueError:
            print("command not valid")
            continue

    elif user_action.startswith("complete"):
        try:
            numberdel = int(user_action[9:])

            todos = get_todos()
            index = numberdel - 1
            todo_to_remove = todos[index]
            todos.pop(index)

            with open('files/todos.txt', 'w') as file:
                file.writelines(todos)

            message = f"Todo: {todo_to_remove} was removed from the List."
            print(message)
        except IndexError:
            print("no item with that number")

    elif "exit" in user_action:
        print("exiting...")
        break
    else:
        print("not a valid command")
