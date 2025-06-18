"""
Python OS Module Reference Guide
================================
A comprehensive reference of all important os module functions with examples.
"""

import os
import time
import shutil

def print_header(title):
    """Print a formatted header"""
    print(f"\n{'='*60}")
    print(f"  {title}")
    print(f"{'='*60}")

def basic_operations_reference():
    """Reference for basic OS operations"""
    print_header("BASIC OS OPERATIONS")
    
    print("1. os.getcwd() - Get current working directory")
    print(f"   Current directory: {os.getcwd()}")
    
    print("\n2. os.chdir(path) - Change current working directory")
    print("   os.chdir('/path/to/directory')")
    
    print("\n3. os.listdir(path) - List directory contents")
    print("   Returns list of files and directories")
    print(f"   Current contents: {os.listdir('.')}")
    
    print("\n4. os.name - Operating system name")
    print(f"   OS name: {os.name}")
    print("   'nt' for Windows, 'posix' for Unix/Linux/macOS")

def file_operations_reference():
    """Reference for file operations"""
    print_header("FILE OPERATIONS")
    
    print("1. os.path.exists(path) - Check if path exists")
    print(f"   Current file exists: {os.path.exists(__file__)}")
    
    print("\n2. os.path.isfile(path) - Check if path is a file")
    print(f"   This is a file: {os.path.isfile(__file__)}")
    
    print("\n3. os.path.isdir(path) - Check if path is a directory")
    print(f"   Current directory is dir: {os.path.isdir('.')}")
    
    print("\n4. os.path.getsize(path) - Get file size in bytes")
    print(f"   This file size: {os.path.getsize(__file__)} bytes")
    
    print("\n5. os.stat(path) - Get file status")
    stat = os.stat(__file__)
    print(f"   File stats: size={stat.st_size}, modified={time.ctime(stat.st_mtime)}")
    
    print("\n6. os.remove(path) - Remove a file")
    print("   os.remove('filename.txt')")
    
    print("\n7. os.unlink(path) - Remove a file (same as remove)")
    print("   os.unlink('filename.txt')")

def directory_operations_reference():
    """Reference for directory operations"""
    print_header("DIRECTORY OPERATIONS")
    
    print("1. os.makedirs(path, exist_ok=False) - Create directories recursively")
    print("   os.makedirs('parent/child/grandchild', exist_ok=True)")
    
    print("\n2. os.mkdir(path) - Create a single directory")
    print("   os.mkdir('new_directory')")
    
    print("\n3. os.rmdir(path) - Remove empty directory")
    print("   os.rmdir('empty_directory')")
    
    print("\n4. os.removedirs(path) - Remove directories recursively")
    print("   os.removedirs('parent/child/grandchild')")
    
    print("\n5. os.walk(top) - Walk directory tree")
    print("   for root, dirs, files in os.walk('.'):")
    print("       print(f'Directory: {root}')")
    print("       print(f'Subdirs: {dirs}')")
    print("       print(f'Files: {files}')")

def path_operations_reference():
    """Reference for path operations"""
    print_header("PATH OPERATIONS")
    
    print("1. os.path.join(path1, path2, ...) - Join path components")
    print(f"   Joined path: {os.path.join('folder', 'subfolder', 'file.txt')}")
    
    print("\n2. os.path.abspath(path) - Get absolute path")
    print(f"   Absolute path: {os.path.abspath('test.txt')}")
    
    print("\n3. os.path.normpath(path) - Normalize path")
    print(f"   Normalized: {os.path.normpath('folder/../folder/file.txt')}")
    
    print("\n4. os.path.relpath(path, start='.') - Get relative path")
    print(f"   Relative path: {os.path.relpath(__file__, '..')}")
    
    print("\n5. os.path.dirname(path) - Get directory name")
    print(f"   Directory: {os.path.dirname(__file__)}")
    
    print("\n6. os.path.basename(path) - Get base name")
    print(f"   Basename: {os.path.basename(__file__)}")
    
    print("\n7. os.path.splitext(path) - Split path and extension")
    name, ext = os.path.splitext(__file__)
    print(f"   Name: {name}, Extension: {ext}")
    
    print("\n8. os.path.split(path) - Split path into head and tail")
    head, tail = os.path.split(__file__)
    print(f"   Head: {head}, Tail: {tail}")

def environment_reference():
    """Reference for environment operations"""
    print_header("ENVIRONMENT OPERATIONS")
    
    print("1. os.environ - Environment variables dictionary")
    print(f"   Number of env vars: {len(os.environ)}")
    
    print("\n2. os.environ.get(key, default) - Get environment variable")
    print(f"   PATH: {os.environ.get('PATH', 'Not found')[:50]}...")
    
    print("\n3. os.environ[key] - Direct access (raises KeyError if not found)")
    print("   os.environ['PATH']")
    
    print("\n4. os.putenv(key, value) - Set environment variable")
    print("   os.putenv('MY_VAR', 'my_value')")
    
    print("\n5. os.getenv(key, default) - Get environment variable (same as environ.get)")
    print(f"   USER: {os.getenv('USER', 'Not found')}")

def process_operations_reference():
    """Reference for process operations"""
    print_header("PROCESS OPERATIONS")
    
    print("1. os.getpid() - Get current process ID")
    print(f"   Current PID: {os.getpid()}")
    
    print("\n2. os.getppid() - Get parent process ID")
    print(f"   Parent PID: {os.getppid()}")
    
    print("\n3. os.system(command) - Execute shell command")
    print("   os.system('ls -la')  # Unix/Linux")
    print("   os.system('dir')     # Windows")
    
    print("\n4. os.popen(command) - Execute command and get output")
    print("   output = os.popen('echo hello').read()")

def file_permissions_reference():
    """Reference for file permissions"""
    print_header("FILE PERMISSIONS")
    
    print("1. os.access(path, mode) - Check file access")
    print(f"   Readable: {os.access(__file__, os.R_OK)}")
    print(f"   Writable: {os.access(__file__, os.W_OK)}")
    print(f"   Executable: {os.access(__file__, os.X_OK)}")
    
    print("\n2. os.chmod(path, mode) - Change file permissions")
    print("   os.chmod('file.txt', 0o644)  # rw-r--r--")
    
    print("\n3. os.umask(mask) - Set file creation mask")
    print("   old_mask = os.umask(0o022)")

def advanced_operations_reference():
    """Reference for advanced operations"""
    print_header("ADVANCED OPERATIONS")
    
    print("1. os.path.expanduser(path) - Expand user home directory")
    print(f"   Expanded: {os.path.expanduser('~/documents')}")
    
    print("\n2. os.path.expandvars(path) - Expand environment variables")
    print(f"   Expanded: {os.path.expandvars('$HOME/documents')}")
    
    print("\n3. os.path.samefile(path1, path2) - Check if paths point to same file")
    print(f"   Same file: {os.path.samefile(__file__, __file__)}")
    
    print("\n4. os.path.getmtime(path) - Get modification time")
    print(f"   Modified: {time.ctime(os.path.getmtime(__file__))}")
    
    print("\n5. os.path.getctime(path) - Get creation time")
    print(f"   Created: {time.ctime(os.path.getctime(__file__))}")
    
    print("\n6. os.path.getatime(path) - Get access time")
    print(f"   Accessed: {time.ctime(os.path.getatime(__file__))}")

def practical_examples():
    """Practical examples of common OS operations"""
    print_header("PRACTICAL EXAMPLES")
    
    print("1. Create a backup of a file:")
    print("   import shutil")
    print("   shutil.copy2('original.txt', 'backup.txt')")
    
    print("\n2. Find all Python files in a directory:")
    print("   python_files = [f for f in os.listdir('.') if f.endswith('.py')]")
    
    print("\n3. Get total size of a directory:")
    print("   total_size = sum(os.path.getsize(f) for f in os.listdir('.') if os.path.isfile(f))")
    
    print("\n4. Create a directory if it doesn't exist:")
    print("   os.makedirs('new_folder', exist_ok=True)")
    
    print("\n5. Walk through all files in a directory tree:")
    print("   for root, dirs, files in os.walk('.'):")
    print("       for file in files:")
    print("           print(os.path.join(root, file))")
    
    print("\n6. Check if a file is older than 24 hours:")
    print("   import time")
    print("   file_age = time.time() - os.path.getmtime('file.txt')")
    print("   is_old = file_age > 24 * 3600")

def common_patterns():
    """Common patterns and best practices"""
    print_header("COMMON PATTERNS & BEST PRACTICES")
    
    print("1. Always use os.path.join() for path construction:")
    print("   ✅ Good: os.path.join('folder', 'file.txt')")
    print("   ❌ Bad: 'folder' + '/' + 'file.txt'")
    
    print("\n2. Check if file exists before operations:")
    print("   if os.path.exists('file.txt'):")
    print("       with open('file.txt', 'r') as f:")
    print("           content = f.read()")
    
    print("\n3. Use exist_ok=True with makedirs to avoid errors:")
    print("   os.makedirs('new_folder', exist_ok=True)")
    
    print("\n4. Handle permissions gracefully:")
    print("   try:")
    print("       os.remove('file.txt')")
    print("   except PermissionError:")
    print("       print('Permission denied')")
    
    print("\n5. Use absolute paths for critical operations:")
    print("   abs_path = os.path.abspath('relative/path')")
    
    print("\n6. Clean up temporary files:")
    print("   try:")
    print("       # Create and use temp file")
    print("       pass")
    print("   finally:")
    print("       if os.path.exists('temp.txt'):")
    print("           os.remove('temp.txt')")

def main():
    """Display the complete OS module reference"""
    print("🐍 PYTHON OS MODULE COMPLETE REFERENCE 🐍")
    print("This reference covers all important os module functions and patterns!")
    
    basic_operations_reference()
    file_operations_reference()
    directory_operations_reference()
    path_operations_reference()
    environment_reference()
    process_operations_reference()
    file_permissions_reference()
    advanced_operations_reference()
    practical_examples()
    common_patterns()
    
    print("\n" + "="*60)
    print("  REFERENCE COMPLETE!")
    print("  Use this as a quick reference while practicing!")
    print("="*60)

if __name__ == "__main__":
    main() 