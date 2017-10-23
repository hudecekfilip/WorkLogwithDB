import unittest
import unittest.mock as mock

from playhouse.test_utils import test_database
from peewee import *
from datetime import datetime
from mock import patch

from database import Entry
from entry_tasks import EntryTasks
from search_in_existing import SearchInExisting
from worklog_with_db import WorkLogWithDB

TEST_DB = SqliteDatabase(':memory:')
TEST_DB.connect()
TEST_DB.create_tables([Entry], safe=True)

DATA = {
    "username": "Filip Hudecek",
    "date": "25/01/1990",
    "title": "Test Entry",
    "spent": 45,
    "note": "These are my notes.",
}

class WorkLogTests(unittest.TestCase):

    def test_task_username(self):
        foo = EntryTasks()
        with mock.patch('builtins.input', side_effect=["Filip Hudecek"],
            return_value=DATA["username"]):
                self.assertEqual(foo.task_username(), DATA["username"])


    def test_get_date(self):
        foo = EntryTasks()
        with mock.patch('builtins.input',
            side_effect=["25/01/1990"],
            return_value=DATA["date"]):
                assert foo.date_of_the_task() == DATA["date"]


    def test_title_of_the_task(self):
        foo = EntryTasks()
        with mock.patch('builtins.input',
            side_effect=["Test Entry"],
            return_value=DATA["title"]):
            assert foo.title_of_the_task() == DATA["title"]


    def test_taks_note_get(self):
        foo = EntryTasks()
        with mock.patch('builtins.input', side_effect=["These are my notes."],
            return_value=DATA["note"]):
            assert foo.task_note_get() == DATA["note"]


    def test_username(self):
        foo = EntryTasks()
        self.assertEqual(foo.task_username_2("Filip"), "Filip")


    def test_dates(self):
        foo = EntryTasks()
        self.assertEqual(foo.date_of_the_task_2("25/01/1990"), "25/01/1990")


    def test_title(self):
        foo = EntryTasks()
        self.assertEqual(foo.title_of_the_task_2("Test Title"), "Test Title")


    def test_time(self):
        foo = EntryTasks()
        self.assertEqual(foo.time_spent_2(45), 45)


    def test_note(self):
        foo = EntryTasks()
        self.assertEqual(foo.task_note_get_2("Test Note"), "Test Note")


    @patch('__main__.SearchInExisting.search_by_what')
    def test_search_by_employee(self, mock):
        arg = "A"
        foo = SearchInExisting()
        foo.search_by_what(arg)
        self.assertTrue(mock.called)


    @patch('__main__.SearchInExisting.search_by_dates')
    def test_search_by_dates(self, mock):
        arg = "B"
        foo = SearchInExisting()
        foo.search_by_what(arg)
        self.assertTrue(mock.called)


    @patch('__main__.SearchInExisting.search_by_times')
    def test_search_by_times(self, mock):
        arg = "C"
        foo = SearchInExisting()
        foo.search_by_what(arg)
        self.assertTrue(mock.called)


    @patch('__main__.SearchInExisting.search_by_search_term')
    def test_search_by_search_term(self, mock):
        arg = "D"
        foo = SearchInExisting()
        foo.search_by_what(arg)
        self.assertTrue(mock.called)


    @patch('__main__.SearchInExisting.search_in_existing')
    def test_what_to_do(self, mock):
        arg = "Q"
        foo = SearchInExisting()
        foo.search_by_what(arg)
        self.assertTrue(mock.called)


    @patch('__main__.SearchInExisting.search_in_existing')
    def test_in_existing(self, mock):
        arg = "R"
        foo = SearchInExisting()
        foo.next_edit_delete_or_return_2(arg)
        self.assertTrue(mock.called)


if __name__ == "__main__":
    unittest.main()
