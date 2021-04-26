import sys
from cx_Freeze import setup, Executable

setup(
    name = "Book Store",
    version = "1.0",
    description = "Mochan Book Store",
    executables = [Executable("book_store.py", base = "Win32GUI")])