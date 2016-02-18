class DBReaderException(Exception):
    pass

class DBReader:

    def __init__(self, file_contents=[]):
        if not file_contents:
            file_contents = self.read_file()
        self.cleaned_data = self.clean_file(file_contents)

    @staticmethod
    def clean_file(file_contents):
        return [line.split(',') for line in file_contents]

    def read_file(self):
        with open("database") as infile:
            data = infile.readlines()
        return data

    # def add_to_file(self):
        # with open("A_database", "a") as outfile:
            # outfile.write("yo lol")

    def filter_by_username(self, username):
        return [line for line in self.cleaned_data if line[0].lower() == username.lower()]

    # def filter_by_password(self, password):
        # return [line for line in self.cleaned_data if line[0].lower() == password.lower()]

    def get_by_username(self, username):
        results = self.filter_by_username(username)
        print(results)
        if len(results) > 1:
            raise DBReaderException("Found more than one record for {}".format(username))
        elif len(results) == 0:
            raise DBReaderException("No records found for name: {}".format(username))
        else:
            return results[0]

'''
   def get_by_password(self, password):
        results = self.filter_by_password(password)
        if len(results) > 1:
            raise DBReaderException("Found more than one record for {}".format(password))
        elif len(results) == 0:
            raise DBReaderException("No records found for password: {}".format(password))
        else:
            return results[0]'''
