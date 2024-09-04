from helper import display_file_content, display_menu, FileChoice, Command

files = {
    FileChoice.NEWS_DECLINE: 'news_decline.csv',
    FileChoice.SNAKES_COUNT: 'snakes_count_10.csv',
    FileChoice.TREES: 'trees.csv'
}

def handle_choice(choice):
    try:
        file_choice = FileChoice(choice)
        file_name = files[file_choice]
        
        command_input = input("Enter the command (H for head, T for tail, D for df): ").strip().upper()
        command = Command(command_input)
        
        if file_choice in files:
            display_file_content(file_name, command)
        else:
            print("Invalid file choice. Please run the script again and select a valid option.")
    except (ValueError, KeyError):
        print("Invalid input. Please enter a valid option letter for command and a number for file.")

if __name__ == "__main__":
    # Display menu
    display_menu(files)
    
    # Get user input
    choice = input("Enter the number of the file you want to view: ")
    
    # Handle user choice
    handle_choice(choice)
