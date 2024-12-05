# 'posix': For Unix-like OS (Linux, macOS, etc.)
# 'nt': For Windows
# 'java': For Java platform (when running in a Jython environment)
import os
print(os.name)

# Check for environment variables that may indicate OS type
# print(os.environ)

# 'Windows': For Windows
# 'Linux': For Linux-based systems
# 'Darwin': For macOS (as it's built on Unix-based Darwin)
import platform
os_name = platform.system()
os_version = platform.release()
print(f"Operating System: {os_name}")
print(f"Version: {os_version}")


# Handling Specific OS Logic:
os_name = platform.system()

if os_name == "Windows":
    print("This is a Windows system.")
elif os_name == "Linux":
    print("This is a Linux system.")
elif os_name == "Darwin":
    print("This is a macOS system.")
else:
    print("Unknown operating system.")
    
    
# Other Useful Platform Info:
# Machine type (e.g., x86_64, i386, etc.)
machine_type = platform.machine()
print(f"Machine type: {machine_type}")

# Architecture (32-bit or 64-bit)
architecture = platform.architecture()
print(f"Architecture: {architecture}")

# Using sys module for Python-specific checks:
import sys

print(f"Python Version: {sys.version}")
print(f"Platform: {sys.platform}")


# Summary of Methods:
# os.name: Basic OS type (e.g., 'posix', 'nt').
# platform.system(): More specific OS name (e.g., 'Windows', 'Linux', 'Darwin').
# platform.release(): The version of the OS.
# platform.version(): Detailed version information.
# sys.platform: Platform identifier (e.g., 'win32', 'linux').

