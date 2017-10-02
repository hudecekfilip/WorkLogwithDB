from database import Entry

class SearchInExisting:
    def search_in_existing(self):
        self.search_output = self.search_in_existing_choose()
        self.search_by_what()


    def search_by_what(self):
        if self.search_output.upper() == "A":
            self.search_by_employee()
        elif self.search_output.upper() == "B":
            self.search_by_dates()
        elif self.search_output.upper() == "C":
            self.search_by_times()
        elif self.search_output.upper() == "D":
            self.search_by_search_term()
        elif self.search_output.upper() == "E":
            self.what_to_do()
        else:
            print("You entered the wrong value!")
            self.search_in_existing()


    def search_in_existing_choose(self):
        print("Do you want search by:")
        print("a) Employee name")
        print("b) Dates")
        print("c) Time")
        print("d) Search term")
        print("e) Return to menu")
        self.search_output = input("> ")
        self.clear_screen()
        return self.search_output


    def search_by_employee(self):
        self.employee = self.available_employees()
        self.print_entries(Entry.username==self.employee)


    def search_by_dates(self):
        self.bla_date = self.available_dates()
        self.print_entries(Entry.date==self.bla_date)


    def search_by_times(self):
        self.time_time = self.available_times()
        self.print_entries(Entry.spent==self.time_time)


    def search_by_search_term(self):
        self.ids = self.search_by_all()
        self.print_entries_all()


    def available_employees(self):
        users = []
        count = 1
        for user in Entry.select():
            users.append(user.username)
        users = list(set(users))
        print("Search by Employee, insert name: ")
        for user in users:
            print("{} | {}".format(count, user))
            count += 1
        self.employee = input("< ")
        if not self.employee in users:
            print("You entered a wrong name. This is name is not in the DB!")
            self.search_by_employee()
        return self.employee


    def print_entries(self, val1):
        count = 1
        for each in Entry.select().where(val1):
            print("ID: {}".format(each.id))
            print("Username: {}".format(each.username))
            print("Date: {}".format(each.date))
            print("Title {}".format(each.title))
            print("Time Spent: {}".format(each.spent))

            if not each.note:
                print("Notes: NONE")
            else:
                print("Notes: {}".format(each.note))

            print("\nResult(s) {} of {}".format(count,
                len(Entry.select().where(val1))))
            print("[N]ext, [E]dit, [D]elete, [R]eturn to search menu")
            self.row = Entry.get(Entry.id == each.id)
            count += 1
            self.next_edit_delete_or_return()


    def next_edit_delete_or_return(self):
        self.edit = input("< ")
        if self.edit.upper() == "N":
            pass
        elif self.edit.upper() == "E":
            self.add_new_entry()
            self.row.delete_instance()
            print("The entry has been edited!")
        elif self.edit.upper() == "D":
            self.row.delete_instance()
            print("The entry has been deleted!")
        elif self.edit.upper() == "R":
            self.search_in_existing()
        else:
            self.next_edit_delete_or_return()


    def available_dates(self):
        dates = []
        count = 1
        for date in Entry.select():
            dates.append(date.date)
        dates = list(set(dates))
        print("Search by Date, insert date: ")
        for date in dates:
            print("{} | {}".format(count, date))
            count += 1
        self.bla_date = input("< ")
        print(self.bla_date)
        if not self.bla_date in dates:
            print("You entered a wrong date. This is date is not in the DB!")
            self.search_by_dates()
        return self.bla_date


    def available_times(self):
        times = []
        count = 1
        for time in Entry.select():
            times.append(time.spent)
        print(times)
        try:
            self.time_time = int(input("< "))
        except ValueError:
            print("Please enter the number")
            self.available_times()
        if not self.time_time in times:
            print("You entered a wrong time. This time is not in the DB!")
            self.search_by_times()
        return self.time_time


    def search_by_all(self):
        self.ids = []
        count = 1

        print("Insert search term")
        text = input("< ")

        check_title = Entry.select().where(Entry.title.contains(text))
        check_note = Entry.select().where(Entry.note.contains(text))

        if check_title:
            for each in check_title:
                self.ids.append(each.id)
        elif check_note:
            for each in check_note:
                self.ids.append(each.id)

        self.ids = list(set(self.ids))

        return self.ids


    def print_entries_all(self):
        count = 1
        for idcko in self.ids:
            for each in Entry.select().where(Entry.id==idcko):
                print("ID: {}".format(each.id))
                print("Username: {}".format(each.username))
                print("Date: {}".format(each.date))
                print("Title {}".format(each.title))
                print("Time Spent: {}".format(each.spent))

                if not each.note:
                    print("Notes: NONE")
                else:
                    print("Notes: {}".format(each.note))

                print("\nResult(s) {} of {}".format(count,
                    len(self.ids)))
                print("[N]ext, [E]dit, [D]elete, [R]eturn to search menu")
                self.row = Entry.get(Entry.id == each.id)
                self.next_edit_delete_or_return()
            count += 1
