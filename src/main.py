import storage


def display_menu():
    print("\n" + "="*40)
    print("TODO APPLICATION")
    print("="*40)
    print("1. Add a todo")
    print("2. View all todos")
    print("3. Update a todo")
    print("4. Delete a todo")
    print("5. Mark todo as complete/incomplete")
    print("6. Exit")
    print("="*40)


def add_todo():
    title = input("Enter title: ").strip()
    description = input("Enter description: ").strip()
    
    todo = storage.add_todo(title, description)
    print(f"Todo added with ID: {todo.id}")


def view_all_todos():
    todos = storage.get_all_todos()
    
    if not todos:
        print("\nNo todos found.")
    else:
        print("\n" + "="*40)
        for todo in todos:
            print(todo)
            print("-"*40)


def update_todo():
    try:
        todo_id = int(input("Enter todo ID to update: "))
        todo = storage.get_todo_by_id(todo_id)
        
        if not todo:
            print(f"Todo with ID {todo_id} not found.")
            return
        
        print(f"\nCurrent title: {todo.title}")
        new_title = input("Enter new title (or press Enter to skip): ").strip()
        
        print(f"Current description: {todo.description}")
        new_description = input("Enter new description (or press Enter to skip): ").strip()
        
        storage.update_todo(
            todo_id,
            title=new_title if new_title else None,
            description=new_description if new_description else None
        )
        print("Todo updated successfully.")
        
    except ValueError:
        print("Invalid input. Please enter a valid ID.")


def delete_todo():
    try:
        todo_id = int(input("Enter todo ID to delete: "))
        
        if storage.delete_todo(todo_id):
            print(f"Todo with ID {todo_id} deleted successfully.")
        else:
            print(f"Todo with ID {todo_id} not found.")
            
    except ValueError:
        print("Invalid input. Please enter a valid ID.")


def mark_complete_incomplete():
    try:
        todo_id = int(input("Enter todo ID to mark complete/incomplete: "))
        
        if storage.toggle_complete(todo_id):
            todo = storage.get_todo_by_id(todo_id)
            status = "complete" if todo.completed else "incomplete"
            print(f"Todo marked as {status}.")
        else:
            print(f"Todo with ID {todo_id} not found.")
            
    except ValueError:
        print("Invalid input. Please enter a valid ID.")


def main():
    while True:
        display_menu()
        choice = input("\nEnter your choice: ").strip()
        
        if choice == "1":
            add_todo()
        elif choice == "2":
            view_all_todos()
        elif choice == "3":
            update_todo()
        elif choice == "4":
            delete_todo()
        elif choice == "5":
            mark_complete_incomplete()
        elif choice == "6":
            print("Exiting application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()