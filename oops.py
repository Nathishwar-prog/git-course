"""
Python OS Module Mastery Program
================================
A comprehensive guide to mastering the os module with practical examples and exercises.
"""

import os
import time
import shutil
from pathlib import Path

def print_separator(title):
    """Print a formatted separator with title"""
    print(f"\n{'='*50}")
    print(f"  {title}")
    print(f"{'='*50}")

def section_1_basic_operations():
    """Section 1: Basic OS Operations"""
    print_separator("SECTION 1: BASIC OS OPERATIONS")
    
    print("1.1 Current Working Directory:")
    print(f"Current directory: {os.getcwd()}")
    
    print("\n1.2 List Directory Contents:")
    print("Files and folders in current directory:")
    for item in os.listdir('.'):
        print(f"  - {item}")
    
    print("\n1.3 Environment Variables:")
    print(f"PATH: {os.environ.get('PATH', 'Not found')[:100]}...")
    print(f"USER: {os.environ.get('USER', 'Not found')}")
    print(f"OS: {os.name}")

def section_2_file_operations():
    """Section 2: File Operations"""
    print_separator("SECTION 2: FILE OPERATIONS")
    
    # Create test files
    test_files = ['test1.txt', 'test2.txt', 'temp_folder']
    
    print("2.1 Creating test files and folders:")
    for file in test_files:
        if file.endswith('.txt'):
            with open(file, 'w') as f:
                f.write(f"This is {file}")
            print(f"  Created: {file}")
        else:
            os.makedirs(file, exist_ok=True)
            print(f"  Created folder: {file}")
    
    print("\n2.2 File Information:")
    for file in os.listdir('.'):
        if os.path.isfile(file) and file.endswith('.txt'):
            stat = os.stat(file)
            print(f"  {file}:")
            print(f"    Size: {stat.st_size} bytes")
            print(f"    Created: {time.ctime(stat.st_ctime)}")
            print(f"    Modified: {time.ctime(stat.st_mtime)}")
    
    print("\n2.3 Path Operations:")
    current_path = os.getcwd()
    print(f"  Current path: {current_path}")
    print(f"  Directory name: {os.path.dirname(current_path)}")
    print(f"  Base name: {os.path.basename(current_path)}")
    print(f"  Absolute path: {os.path.abspath('test1.txt')}")
    print(f"  Path exists: {os.path.exists('test1.txt')}")
    print(f"  Is file: {os.path.isfile('test1.txt')}")
    print(f"  Is directory: {os.path.isdir('temp_folder')}")

def section_3_advanced_operations():
    """Section 3: Advanced Operations"""
    print_separator("SECTION 3: ADVANCED OPERATIONS")
    
    print("3.1 Walking Directory Tree:")
    print("Directory structure:")
    for root, dirs, files in os.walk('.'):
        level = root.replace('.', '').count(os.sep)
        indent = ' ' * 2 * level
        print(f"{indent}{os.path.basename(root)}/")
        subindent = ' ' * 2 * (level + 1)
        for file in files:
            print(f"{subindent}{file}")
    
    print("\n3.2 File Permissions:")
    for file in os.listdir('.'):
        if os.path.isfile(file) and file.endswith('.txt'):
            mode = os.stat(file).st_mode
            print(f"  {file}: {oct(mode)}")
    
    print("\n3.3 Path Joining:")
    path1 = "folder1"
    path2 = "subfolder"
    path3 = "file.txt"
    full_path = os.path.join(path1, path2, path3)
    print(f"  Joined path: {full_path}")
    
    print("\n3.4 Path Splitting:")
    sample_path = "/home/user/documents/file.txt"
    print(f"  Original: {sample_path}")
    print(f"  Directory: {os.path.dirname(sample_path)}")
    print(f"  Filename: {os.path.basename(sample_path)}")
    print(f"  Name without ext: {os.path.splitext(os.path.basename(sample_path))[0]}")
    print(f"  Extension: {os.path.splitext(sample_path)[1]}")

def section_4_practical_exercises():
    """Section 4: Practical Exercises"""
    print_separator("SECTION 4: PRACTICAL EXERCISES")
    
    print("Exercise 1: File Organizer")
    print("Creating a simple file organizer...")
    
    # Create exercise directory structure
    exercise_dir = "file_organizer"
    os.makedirs(exercise_dir, exist_ok=True)
    
    # Create sample files
    sample_files = [
        "document.pdf",
        "image.jpg", 
        "video.mp4",
        "script.py",
        "data.csv",
        "readme.txt"
    ]
    
    for file in sample_files:
        file_path = os.path.join(exercise_dir, file)
        with open(file_path, 'w') as f:
            f.write(f"Sample content for {file}")
    
    print(f"  Created {len(sample_files)} sample files in {exercise_dir}/")
    
    print("\nExercise 2: File Counter")
    file_count = 0
    dir_count = 0
    
    for item in os.listdir('.'):
        if os.path.isfile(item):
            file_count += 1
        elif os.path.isdir(item):
            dir_count += 1
    
    print(f"  Files: {file_count}")
    print(f"  Directories: {dir_count}")
    
    print("\nExercise 3: File Size Calculator")
    total_size = 0
    for file in os.listdir('.'):
        if os.path.isfile(file):
            size = os.path.getsize(file)
            total_size += size
            print(f"  {file}: {size} bytes")
    
    print(f"  Total size: {total_size} bytes ({total_size/1024:.2f} KB)")

def section_5_cleanup():
    """Section 5: Cleanup"""
    print_separator("SECTION 5: CLEANUP")
    
    print("Cleaning up test files...")
    
    # Remove test files
    test_files = ['test1.txt', 'test2.txt', 'temp_folder', 'file_organizer']
    
    for item in test_files:
        try:
            if os.path.isfile(item):
                os.remove(item)
                print(f"  Removed file: {item}")
            elif os.path.isdir(item):
                shutil.rmtree(item)
                print(f"  Removed directory: {item}")
        except Exception as e:
            print(f"  Error removing {item}: {e}")

def interactive_practice():
    """Interactive practice session"""
    print_separator("INTERACTIVE PRACTICE")
    
    print("Let's practice some OS operations interactively!")
    
    while True:
        print("\nChoose an operation:")
        print("1. List current directory contents")
        print("2. Show current working directory")
        print("3. Create a new file")
        print("4. Create a new directory")
        print("5. Show file information")
        print("6. Exit")
        
        choice = input("\nEnter your choice (1-6): ").strip()
        
        if choice == '1':
            print("\nCurrent directory contents:")
            for item in os.listdir('.'):
                item_type = "📁" if os.path.isdir(item) else "📄"
                print(f"  {item_type} {item}")
        
        elif choice == '2':
            print(f"\nCurrent working directory: {os.getcwd()}")
        
        elif choice == '3':
            filename = input("Enter filename: ").strip()
            if filename:
                try:
                    with open(filename, 'w') as f:
                        f.write("This is a test file created by OS module practice!")
                    print(f"Created file: {filename}")
                except Exception as e:
                    print(f"Error creating file: {e}")
        
        elif choice == '4':
            dirname = input("Enter directory name: ").strip()
            if dirname:
                try:
                    os.makedirs(dirname, exist_ok=True)
                    print(f"Created directory: {dirname}")
                except Exception as e:
                    print(f"Error creating directory: {e}")
        
        elif choice == '5':
            filename = input("Enter filename to check: ").strip()
            if filename and os.path.exists(filename):
                stat = os.stat(filename)
                print(f"\nFile: {filename}")
                print(f"Size: {stat.st_size} bytes")
                print(f"Created: {time.ctime(stat.st_ctime)}")
                print(f"Modified: {time.ctime(stat.st_mtime)}")
            else:
                print("File not found!")
        
        elif choice == '6':
            print("Goodbye! Keep practicing!")
            break
        
        else:
            print("Invalid choice. Please try again.")

def main():
    """Main function to run the OS module mastery program"""
    print("🐍 PYTHON OS MODULE MASTERY PROGRAM 🐍")
    print("This program will teach you the OS module through practical examples!")
    
    # Run all sections
    section_1_basic_operations()
    section_2_file_operations()
    section_3_advanced_operations()
    section_4_practical_exercises()
    section_5_cleanup()
    
    # Interactive practice
    interactive_practice()

if __name__ == "__main__":
    main()
