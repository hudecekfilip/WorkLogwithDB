import datetime
import os

from database import Entry

class EntryTasks:
    def add_new_entry(self):
        self.task_name = self.task_username()
        self.task_date = self.date_of_the_task()
        self.task_title = self.title_of_the_task()
        self.task_time = self.time_spent()
        self.task_note = self.task_note_get()
        self.add_entries()
        input("You entry has been added. Press enter to return to the menu")


    def clear_screen(self):
        if os.name == 'nt':
            os.system('cls')
        else:
            print('\033c')


    def task_username(self):
        print("Insert your name:")
        self.task_name = input("< ")
        if not self.task_name:
            self.task_username()
        self.clear_screen()
        return self.task_name


    def date_of_the_task(self):
        print("Date of the task")
        print("Please use DD/MM/YYYY format:")
        self.task_date = input("> ")
        try:
            datetime.datetime.strptime(self.task_date, '%d/%m/%Y')
        except ValueError:
            print("Incorrect data format, should be DD/MM/YYYY!")
            input("Press enter to continue")
            self.date_of_the_task()
        self.clear_screen()
        return self.task_date


    def title_of_the_task(self):
        print("Title of the task")
        self.task_title = input("> ")
        if not self.task_title:
            print("You have to enter the title of the task!")
            input("Press enter to continue")
            self.title_of_the_task()
        self.clear_screen()
        return self.task_title


    def time_spent(self):
        print("Time spent (rounded minutes)")
        self.task_time = input("> ")
        try:
            self.task_time = int(self.task_time)
        except ValueError:
            print("You have to enter the time spent!")
            input("Press enter to continue")
            self.time_spent()
        self.clear_screen()
        return self.task_time


    def task_note_get(self):
        print("Enter your note (optional) or press enter to continue")
        self.task_note = input("< ")
        return self.task_note


    def add_entries(self):
        Entry.create(username = self.task_name,
                    date = self.task_date,
                    title = self.task_title,
                    spent = self.task_time,
                    note = self.task_note
                    )
