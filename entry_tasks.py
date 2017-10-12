import datetime
import os

from database import Entry

class EntryTasks:
    def add_new_entry(self):
        self.task_name = self.task_username()
        self.task_username_2(self.task_name)
        self.task_date = self.date_of_the_task()
        self.date_of_the_task_2(self.task_date)
        self.task_title = self.title_of_the_task()
        self.title_of_the_task_2(self.task_title)
        self.task_time = self.time_spent()
        self.time_spent_2(self.task_time)
        self.task_note = self.task_note_get()
        self.task_note_get_2(self.task_note)
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
        return self.task_name


    def task_username_2(self, arg):
        if not arg:
            self.task_username()
        else:
            self.clear_screen()
            return arg


    def date_of_the_task(self):
        print("Date of the task")
        print("Please use DD/MM/YYYY format:")
        self.task_date = input("> ")
        return self.task_date


    def date_of_the_task_2(self, arg2):
        try:
            datetime.datetime.strptime(arg2, '%d/%m/%Y')
        except ValueError:
            self.date_of_the_task()
        else:
            self.clear_screen()
            return arg2


    def title_of_the_task(self):
        print("Title of the task")
        self.task_title = input("> ")
        return self.task_title


    def title_of_the_task_2(self, arg3):
        if not arg3:
            print("You have to enter the title of the task!")
            input("Press enter to continue")
            self.title_of_the_task()
        self.clear_screen()
        return arg3


    def time_spent(self):
        print("Time spent (rounded minutes)")
        self.task_time = input("> ")


    def time_spent_2(self, arg4):
        try:
            int(arg4)
        except ValueError:
            print("You have to enter the time spent!")
            input("Press enter to continue")
            self.time_spent()
        self.clear_screen()
        return arg4


    def task_note_get(self):
        print("Enter your note (optional) or press enter to continue")
        self.task_note = input("< ")
        return self.task_note


    def task_note_get_2(self, arg5):
        if not arg5:
            print("You have to enter the title of the task!")
            input("Press enter to continue")
            self.task_note_get()
        self.clear_screen()
        return arg5


    def add_entries(self):
        Entry.create(username = self.task_name,
                    date = self.task_date,
                    title = self.task_title,
                    spent = self.task_time,
                    note = self.task_note
                    )
