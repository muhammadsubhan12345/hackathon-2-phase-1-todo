from todo import Todo

todos = []
next_id = 1


def add_todo(title, description):
    global next_id
    todo = Todo(next_id, title, description)
    todos.append(todo)
    next_id += 1
    return todo


def get_all_todos():
    return todos


def get_todo_by_id(todo_id):
    for todo in todos:
        if todo.id == todo_id:
            return todo
    return None


def update_todo(todo_id, title=None, description=None):
    todo = get_todo_by_id(todo_id)
    if todo:
        todo.update(title, description)
        return True
    return False


def delete_todo(todo_id):
    todo = get_todo_by_id(todo_id)
    if todo:
        todos.remove(todo)
        return True
    return False


def toggle_complete(todo_id):
    todo = get_todo_by_id(todo_id)
    if todo:
        todo.toggle_complete()
        return True
    return False