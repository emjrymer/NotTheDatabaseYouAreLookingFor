import unittest

from unittest import mock

from NotTheDatabase import DBReader, DBReaderException


class DatabaseTestCase(unittest.TestCase):

    def test_db_reader_can_format_expected_file_structure(self):
        expected_input = ["emily1,pa$$word,emily wivell,pink,owl", "1ylime,passw0rd,emily wivell,pink,owl"]
        expected_output = [["emily1", "pa$$word", "emily wivell", "pink", "owl"], ["1ylime", "passw0rd", "emily wivell", "pink", "owl"]]
        self.assertEqual(DBReader.clean_file(expected_input), expected_output)

    def test_db_reader_can_format_expected_file_structure_in_init(self):
        expected_input = ["emily1,pa$$word,emily wivell,pink,owl", "1ylime,passw0rd,emily wivell,pink,owl"]
        expected_output = [["emily1", "pa$$word", "emily wivell", "pink", "owl"], ["1ylime", "passw0rd", "emily wivell", "pink", "owl"]]
        db_reader = DBReader(expected_input)
        self.assertEqual(db_reader.cleaned_data, expected_output)

    def test_user_input_same_as_username_in_database(self):
        file_input = ["emily1,pa$$word,emily wivell,pink,owl", "1ylime,passw0rd,emily wivell,pink,owl"]
        db_reader = DBReader(file_input)
        self.assertEqual(db_reader.get_by_username("emily1"), ["emily1", "pa$$word", "emily wivell", "pink", "owl"])
        self.assertEqual(db_reader.get_by_username("1ylime"), ["1ylime", "passw0rd", "emily wivell", "pink", "owl"])

    def test_db_reader_can_get_by_username_error_if_mult_same_username(self):
        file_input = ["emily1,pa$$word,emily wivell,pink,owl", "emily1,pa$$word,emily wivell,pink,owl"]
        db_reader = DBReader(file_input)
        with self.assertRaises(DBReaderException):
            db_reader.get_by_username("emily1")

    def test_db_reader_can_filter_many_entries_of_username_in_list(self):
        file_input = ["emily1,pa$$word,emily wivell,pink,owl", "1ylime,passw0rd,emily wivell,pink,owl", "emily1,different,pa$$word,emily wivell,pink,owl"]
        db_reader = DBReader(file_input)
        self.assertEqual(db_reader.filter_by_username("emily1"), [["emily1", "pa$$word", "emily wivell", "pink", "owl"], ["emily1", "different", "pa$$word", "emily wivell", "pink", "owl"]])

    def test_db_reader_can_get_by_username_in_any_case(self):
        file_input = ["emily1,pa$$word,emily wivell,pink,owl", "1ylime,passw0rd,emily wivell,pink,owl"]
        db_reader = DBReader(file_input)
        self.assertEqual(db_reader.get_by_username("eMiLy1"), ["emily1", "pa$$word", "emily wivell", "pink", "owl"])

    def test_db_reader_will_return_empty_list_if_not_found(self):
        db_reader = DBReader(["emily1,pa$$word,emily wivell,pink,owl", "1ylime,passw0rd,emily wivell,pink,owl"])
        self.assertRaises(Exception)
        db_reader = db_reader.get_by_username("1ylime")

    @mock.patch("NotTheDatabase.DBReader.read_file")
    def test_db_reader_will_read_database_if_no_contents_provided(self, read_file):
        read_file.return_value = ["emily1,pa$$word,emily wivell,pink,owl", "1ylime,passw0rd,emily wivell,pink,owl"]
        db_reader = DBReader()
        read_file.assert_called_once_with()

'''    def test_password_input_same_as_password_in_database(self):
        file_input = ["emily1,pa$$word,emily wivell,pink,owl", "1ylime,passw0rd,emily wivell,pink,owl"]
        db_reader = DBReader(file_input)
        self.assertEqual(db_reader.get_by_password("pa$$word"), ["emily1", "pa$$word", "emily wivell", "pink", "owl"])
        #self.assertEqual(db_reader.get_by_password("1ylime"), ["1ylime", "passw0rd", "emily wivell", "pink", "owl"])'''
