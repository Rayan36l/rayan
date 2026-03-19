# --- Homework 1 + 2 Review: Vocabulary & Commands ---
# 1. Git vs. GitHub: Git is local version control; GitHub is the online hosting service.
# 2. Terminal vs. Command Line: Terminal is the window; Command Line is where you type instructions.
# 3. Local vs. Remote Repository: Local is on your computer; Remote is on a server.
# 4. Version Control: A system that records changes to files over time.
# 5. Staging Area: A file that stores information about what will go into your next commit.
# 6. git add: Adds changes to the staging area.
# 7. git commit: Captures a snapshot of currently staged changes.
# 8. git push: Updates the remote repository with local commits.
# 9. git status: Displays the state of the working directory and staging area.
# 10. git pull: Fetches and merges changes from the remote to local.
# 11. pwd: Print Working Directory.
# 12. ls: Lists all files and directories in the current folder.
# 13. cd: Change Directory.
# 14. nano: Command-line based text editor.
# 15. touch: Creates a new, empty file.
# 16. mv: Moves or renames files/folders.
# 17. rm: Deletes a file.
# 18. cat: Displays file contents in the terminal.

# --- Section 3.2: Directory Tree Navigation ---
# 1. Command to see current working directory: pwd
# 2. Command to list all files in the current directory: ls
# 3. Commands to move to brianna_repo and pull changes: cd ../brianna_repo then git pull
# 4. Command to move homework.py to the homework/ folder: mv homework.py ../judy_decal/homework/
# 5. Command to move yourself to the homework/ folder: cd ../judy_decal/homework/
# 6. Command to see the contents of homework.py in the terminal: cat homework.py
# 7. Commands to save and push changes: git add, git commit -m "message", git push
# 8. Command to resolve the 'rejected' error: git pull (to integrate remote changes first)
# 9. Absolute path to move to Recent/: ~/python_decal/Recent/

# --- Section 4: Homework 3 Review ---
def checkDataType(input_data):
    """Returns a string indicating the data type of the input."""
    return type(input_data).__name__ 

def evenOrOdd(integer):
    """Returns 'Even' if the integer is even, and 'Odd' otherwise."""
    if integer % 2 == 0:
        return 'Even'
    return 'Odd' 

# --- Section 5: Loops ---
def sumWithLoop(int_list):
    """Returns the sum of a list of integers using a loop."""
    total = 0
    for num in int_list:
        total += num
    return total 

# --- Section 6: Homework 4 Review ---
def duplicateList(original_list):
    """Returns a new list with each element duplicated."""
    new_list = []
    for item in original_list:
        new_list.append(item)
        new_list.append(item)
    return new_list 

def square(num):
    """Corrected function to return the square of a number."""
    return num * num 

# --- Section 7.2: Favorite Function Execution ---
if __name__ == "__main__":
    # Calling evenOrOdd as the 'favorite function' for the screenshot
    test_val = 38
    result = evenOrOdd(test_val)
    print(f"Testing my favorite function (evenOrOdd) with input {test_val}:")
    print(f"The result is: {result}") 