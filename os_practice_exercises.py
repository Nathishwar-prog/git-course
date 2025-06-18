"""
Additional OS Module Practice Exercises
======================================
More challenging exercises to master the os module
"""

import os
import time
import shutil
import glob

def exercise_1_file_backup():
    """Exercise 1: Create a file backup system"""
    print("=" * 50)
    print("EXERCISE 1: FILE BACKUP SYSTEM")
    print("=" * 50)
    
    # Create source files
    source_dir = "source_files"
    backup_dir = "backup_files"
    
    os.makedirs(source_dir, exist_ok=True)
    os.makedirs(backup_dir, exist_ok=True)
    
    # Create some source files
    source_files = ["important.txt", "data.csv", "config.ini"]
    for file in source_files:
        file_path = os.path.join(source_dir, file)
        with open(file_path, 'w') as f:
            f.write(f"Important data for {file}")
    
    print(f"Created {len(source_files)} source files in {source_dir}/")
    
    # Backup files with timestamp
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    for file in source_files:
        source_path = os.path.join(source_dir, file)
        backup_path = os.path.join(backup_dir, f"{file}.{timestamp}")
        
        shutil.copy2(source_path, backup_path)
        print(f"Backed up: {file} -> {file}.{timestamp}")
    
    print(f"Backup completed in {backup_dir}/")

def exercise_2_file_organizer():
    """Exercise 2: Organize files by extension"""
    print("\n" + "=" * 50)
    print("EXERCISE 2: FILE ORGANIZER BY EXTENSION")
    print("=" * 50)
    
    # Create test files with different extensions
    test_files = [
        "document.pdf", "image.jpg", "video.mp4", "script.py",
        "data.csv", "readme.txt", "config.json", "archive.zip"
    ]
    
    organize_dir = "files_to_organize"
    os.makedirs(organize_dir, exist_ok=True)
    
    # Create test files
    for file in test_files:
        file_path = os.path.join(organize_dir, file)
        with open(file_path, 'w') as f:
            f.write(f"Content for {file}")
    
    print(f"Created {len(test_files)} test files in {organize_dir}/")
    
    # Organize files by extension
    for file in os.listdir(organize_dir):
        if os.path.isfile(os.path.join(organize_dir, file)):
            # Get file extension
            _, ext = os.path.splitext(file)
            ext = ext[1:] if ext else "no_extension"  # Remove the dot
            
            # Create extension directory
            ext_dir = os.path.join(organize_dir, ext)
            os.makedirs(ext_dir, exist_ok=True)
            
            # Move file to appropriate directory
            old_path = os.path.join(organize_dir, file)
            new_path = os.path.join(ext_dir, file)
            shutil.move(old_path, new_path)
            print(f"Moved {file} to {ext}/ directory")

def exercise_3_directory_scanner():
    """Exercise 3: Advanced directory scanner"""
    print("\n" + "=" * 50)
    print("EXERCISE 3: ADVANCED DIRECTORY SCANNER")
    print("=" * 50)
    
    def scan_directory(path=".", max_depth=3, current_depth=0):
        """Recursively scan directory with depth limit"""
        if current_depth > max_depth:
            return
        
        try:
            items = os.listdir(path)
            files = []
            dirs = []
            
            for item in items:
                item_path = os.path.join(path, item)
                if os.path.isfile(item_path):
                    files.append(item)
                elif os.path.isdir(item_path):
                    dirs.append(item)
            
            # Print current level
            indent = "  " * current_depth
            print(f"{indent}📁 {os.path.basename(path)}/")
            
            # Print files
            for file in files:
                file_path = os.path.join(path, file)
                size = os.path.getsize(file_path)
                print(f"{indent}  📄 {file} ({size} bytes)")
            
            # Recursively scan subdirectories
            for dir_name in dirs:
                dir_path = os.path.join(path, dir_name)
                scan_directory(dir_path, max_depth, current_depth + 1)
                
        except PermissionError:
            print(f"{indent}❌ Permission denied: {path}")
        except Exception as e:
            print(f"{indent}❌ Error scanning {path}: {e}")
    
    print("Scanning current directory structure:")
    scan_directory()

def exercise_4_file_monitor():
    """Exercise 4: Simple file change monitor"""
    print("\n" + "=" * 50)
    print("EXERCISE 4: FILE CHANGE MONITOR")
    print("=" * 50)
    
    monitor_dir = "monitor_test"
    os.makedirs(monitor_dir, exist_ok=True)
    
    # Create initial file
    test_file = os.path.join(monitor_dir, "watch_me.txt")
    with open(test_file, 'w') as f:
        f.write("Initial content")
    
    print(f"Created file to monitor: {test_file}")
    
    # Get initial stats
    initial_stat = os.stat(test_file)
    print(f"Initial modification time: {time.ctime(initial_stat.st_mtime)}")
    
    # Simulate file change
    print("Waiting 2 seconds, then modifying file...")
    time.sleep(2)
    
    with open(test_file, 'a') as f:
        f.write("\nModified content")
    
    # Check for changes
    new_stat = os.stat(test_file)
    print(f"New modification time: {time.ctime(new_stat.st_mtime)}")
    
    if new_stat.st_mtime > initial_stat.st_mtime:
        print("✅ File was modified!")
        print(f"File size changed from {initial_stat.st_size} to {new_stat.st_size} bytes")
    else:
        print("❌ No changes detected")

def exercise_5_path_utilities():
    """Exercise 5: Path utility functions"""
    print("\n" + "=" * 50)
    print("EXERCISE 5: PATH UTILITY FUNCTIONS")
    print("=" * 50)
    
    def normalize_path(path):
        """Normalize a path and make it absolute"""
        return os.path.abspath(os.path.normpath(path))
    
    def get_relative_path(from_path, to_path):
        """Get relative path from one location to another"""
        return os.path.relpath(to_path, from_path)
    
    def is_subdirectory(parent, child):
        """Check if child is a subdirectory of parent"""
        parent = normalize_path(parent)
        child = normalize_path(child)
        return child.startswith(parent)
    
    # Test paths
    test_paths = [
        "folder1/../folder2/./file.txt",
        "C:/Users/username/Documents",
        "relative/path/to/file",
        "./current/directory"
    ]
    
    print("Path normalization examples:")
    for path in test_paths:
        normalized = normalize_path(path)
        print(f"  {path} -> {normalized}")
    
    # Test relative paths
    print("\nRelative path examples:")
    base_path = "/home/user"
    target_paths = [
        "/home/user/documents/file.txt",
        "/home/user/downloads/image.jpg",
        "/home/other/file.txt"
    ]
    
    for target in target_paths:
        relative = get_relative_path(base_path, target)
        print(f"  From {base_path} to {target} -> {relative}")
    
    # Test subdirectory check
    print("\nSubdirectory check examples:")
    parent = "/home/user"
    children = [
        "/home/user/documents",
        "/home/user/documents/work",
        "/home/other"
    ]
    
    for child in children:
        is_sub = is_subdirectory(parent, child)
        print(f"  {child} is subdirectory of {parent}: {is_sub}")

def exercise_6_environment_explorer():
    """Exercise 6: Environment variables explorer"""
    print("\n" + "=" * 50)
    print("EXERCISE 6: ENVIRONMENT VARIABLES EXPLORER")
    print("=" * 50)
    
    def analyze_environment():
        """Analyze and display environment information"""
        print("System Information:")
        print(f"  Operating System: {os.name}")
        print(f"  Platform: {os.sys.platform}")
        
        print("\nImportant Environment Variables:")
        important_vars = [
            'PATH', 'HOME', 'USER', 'USERNAME', 'TEMP', 'TMP',
            'PYTHONPATH', 'PYTHONHOME', 'LANG', 'LC_ALL'
        ]
        
        for var in important_vars:
            value = os.environ.get(var, 'Not set')
            if var == 'PATH' and len(value) > 100:
                value = value[:100] + "..."
            print(f"  {var}: {value}")
        
        print(f"\nTotal Environment Variables: {len(os.environ)}")
        
        # Show some interesting patterns
        print("\nEnvironment Variables by Pattern:")
        patterns = ['PYTHON', 'PATH', 'HOME', 'USER']
        
        for pattern in patterns:
            matching_vars = [var for var in os.environ.keys() 
                           if pattern.upper() in var.upper()]
            if matching_vars:
                print(f"  Variables containing '{pattern}': {matching_vars}")
    
    analyze_environment()

def cleanup_exercises():
    """Clean up all exercise directories"""
    print("\n" + "=" * 50)
    print("CLEANING UP EXERCISE FILES")
    print("=" * 50)
    
    dirs_to_remove = [
        "source_files", "backup_files", "files_to_organize",
        "monitor_test"
    ]
    
    for dir_name in dirs_to_remove:
        if os.path.exists(dir_name):
            try:
                shutil.rmtree(dir_name)
                print(f"Removed directory: {dir_name}")
            except Exception as e:
                print(f"Error removing {dir_name}: {e}")

def main():
    """Run all exercises"""
    print("🐍 ADDITIONAL OS MODULE PRACTICE EXERCISES 🐍")
    print("These exercises will help you master advanced OS operations!")
    
    try:
        exercise_1_file_backup()
        # exercise_2_file_organizer()
        # exercise_3_directory_scanner()
        # exercise_4_file_monitor()
        # exercise_5_path_utilities()
        # exercise_6_environment_explorer()
        
        print("\n" + "=" * 50)
        print("ALL EXERCISES COMPLETED!")
        print("=" * 50)
        
        # Ask if user wants to clean up
        cleanup = input("\nDo you want to clean up exercise files? (y/n): ").lower()
        if cleanup == 'y':
            cleanup_exercises()
        else:
            print("Exercise files preserved for further practice.")
            
    except KeyboardInterrupt:
        print("\n\nExercise interrupted by user.")
        cleanup_exercises()

if __name__ == "__main__":
    main() 