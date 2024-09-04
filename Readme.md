# File Management Script

## Overview

This project consists of a Python script that allows users to view the contents of different CSV files. 
Users can choose a file and specify whether they want to see the first 5 rows, the last 5 rows, or the entire file. 
The code is organized into two files: `app.py` and `helper.py`.

## Files

### `helper.py`

This file contains helper functions and enumerations used by the main script.

### Enumerations
**FileChoice:** Enum for file choices

```
class FileChoice(Enum):
    NEWS_DECLINE = "1"
    SNAKES_COUNT = "2"
    TREES = "3" 
```    
Defines options for file choices. Each value corresponds to a user selection.

**Command:** Enum for commands

```
class Command(Enum):
    HEAD = "H"
    TAIL = "T"
    DF = "D"
Defines commands for viewing data: H for the first 5 rows, T for the last 5 rows, and D for the entire content.
```

##  Functions
* **display_file_content**(file_name, command)

```
def display_file_content(file_name, command):
    df = pd.read_csv(file_name)
    print(f"\n--- Contents of {file_name} ---\n")
    
    if command == Command.HEAD:
        print("First 5 rows (head):")
        print(df.head())
    elif command == Command.TAIL:
        print("Last 5 rows (tail):")
        print(df.tail())
    elif command == Command.DF:
        print(f"\nFull content of {file_name}:")
        print(df)
    else:
        print("Invalid command. Please use 'H', 'T', or 'D'.")
```
Reads the specified CSV file into a DataFrame and displays content based on the given command. Handles different commands: HEAD, TAIL, and DF. If an invalid command is provided, an error message is shown.

* **display_menu**(files)

```
def display_menu(files):
    print("Please choose a file to view:")
    for choice, file_name in files.items():
        print(f"{choice.value} - {file_name}")
    
    print("\nAvailable commands:")
    for command in Command:
        print(f"{command.value} - {command.name.lower()}")
```
Displays a menu of available files and commands. Lists files and their corresponding choices and available commands with their descriptions.

### `add.py`
This file contains the main logic of the application and utilizes functions from helper.py.

## Code Explanation
1. **Imports** 
```
from helper import display_file_content, display_menu, FileChoice, Command
```

Imports necessary functions and enumerations from helper.py.

2. **Files Dictionary**
```
files = {
    FileChoice.NEWS_DECLINE: 'news_decline.csv',
    FileChoice.SNAKES_COUNT: 'snakes_count_10.csv',
    FileChoice.TREES: 'trees.csv'
}
```
A dictionary mapping file choices to their corresponding CSV filenames.

3. **Function** *handle_choice(choice)*
```
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

```

- __Try Block:__ Attempts to convert the user's file choice and command into enumerations and retrieves the file content.
- __If Block:__ Displays file content based on user command.
- __Except Block:__ Catches ValueError and KeyError exceptions and prints an error message if invalid input is provided.

4. **Main Block**

```
if __name__ == "__main__":
    display_menu(files)
    
    choice = input("Enter the number of the file you want to view: ")
    
    handle_choice(choice)

```
- __Display Menu:__ Calls display_menu to show available files and commands.
- __Get User Input:__ Prompts the user to select a file.
- __Handle User Choice:__ Calls handle_choice to process the user's file selection and command.



