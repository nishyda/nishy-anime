from pathlib import Path
import sys
import webbrowser
import json
import csv
from PySide6.QtWidgets import (QRadioButton, QListWidgetItem, QFormLayout, QLineEdit, QHBoxLayout, QLabel, QApplication, QVBoxLayout, QDialog, QPushButton, QListWidget, QDialogButtonBox)
from PySide6 import QtCore
from PySide6 import QtGui
from cx_Freeze import setup, Executable

setup(
    name="NishyAnime",
    version="2.3",
    description="NishyAnime - Interactive anime list for use with streaming websites",
    executables=[Executable("main.py", target_name="NishyAnime", base="Win32GUI") if sys.platform == "win32" or sys.platform == "cygwin" else Executable("main.py", target_name="NishyAnime")],
    )
