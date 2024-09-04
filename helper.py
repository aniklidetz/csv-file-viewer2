import pandas as pd
from enum import Enum

# Enum for file choices
class FileChoice(Enum):
    NEWS_DECLINE = "1"
    SNAKES_COUNT = "2"
    TREES = "3"

# Enum for commands with single-letter options
class Command(Enum):
    HEAD = "H"
    TAIL = "T"
    DF = "D"

def display_file_content(file_name, command):
    # Reading the CSV file into a DataFrame
    df = pd.read_csv(file_name)
    
    print(f"\n--- Contents of {file_name} ---\n")
    
    if command == Command.HEAD:
        # Display the first 5 rows of the file (by default)
        print("First 5 rows (head):")
        print(df.head())
    elif command == Command.TAIL:
        # Display the last 5 rows (by default)
        print("Last 5 rows (tail):")
        print(df.tail())
    elif command == Command.DF:
        # Display the entire file content
        print(f"\nFull content of {file_name}:")
        print(df)
    else:
        print("Invalid command. Please use 'H', 'T', or 'D'.")

def display_menu(files):
    print("Please choose a file to view:")
    for choice, file_name in files.items():
        print(f"{choice.value} - {file_name}")
    
    print("\nAvailable commands:")
    for command in Command:
        print(f"{command.value} - {command.name.lower()}")
