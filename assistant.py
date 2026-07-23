
def greet():
    print("Friday: Hello!")

def show_help():
    print('''
    Available commands:
    - Hello
    - Help
    - Exit
    ''')

COMMANDS = {"hello" : greet,
            "help" : show_help,
            }

def start_assistant():
    print("-" * 20)
    print("      Welcome to Friday")
    print("-" * 20)

    while True:
        command = input("\nYou: ").strip().lower()
        if command == "exit":
            print("Friday: Goodnight")
            break
        action = COMMANDS.get(command)
        if action: 
            action()
        else:
            print("Friday: Sorry, I don't understand that.")