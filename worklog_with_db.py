import sys

from database import Entry
from entry_tasks import EntryTasks
from search_in_existing import SearchInExisting


class WorkLogWithDB(Entry, EntryTasks, SearchInExisting):
    def __init__(self):
        self.initialize()
        while True:
            self.to_do = self.what_to_do()
            self.choose_what_to_do(self.to_do)


    def what_to_do(self):
        print("WORK LOG")
        print("What would you like to do?:")
        print("a) Add new entry")
        print("b) Search in existing entries")
        print("c) Quit program")
        self.to_do = input("> ")
        self.clear_screen()
        return self.to_do


    def choose_what_to_do(self, to_do):
        if self.to_do.upper() == "A":
            self.add_new_entry()
        elif self.to_do.upper() == "B":
            self.search_in_existing()
        elif self.to_do.upper() == "C":
            print("Thank you for using the Work Log program.")
            print("Come again soon.")
            sys.exit(0)
        else:
            print("Enter a,b or c!")
            self.what_to_do()



if __name__ == '__main__':
	WorkLogWithDB()
