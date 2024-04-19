from datetime import datetime
import os

current_date = datetime.now().date()
date = input("Enter the Date of Journal Entering: ")
mood = input("Please rate your mood of today(from 1 to 10): ")
journal = input("Please enter the journal text: ")

with open(f"{os.getcwd()}\PythonPerDayPractice\App1-ToDoApp\Journal\Journal-{date}.txt","w") as file:
    txt = f"Journalling Date:{current_date}\nEvents Date:{date}\n\nCurrent Mood:{mood}\n\nJournal:\n{journal}"
    file.write(txt)


