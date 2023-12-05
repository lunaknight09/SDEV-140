
# Pass in the file name, open and read through file,
#return a list of lists representing rows in the file.
def read_file_into_lists(file_name):

    parsed_vals = []

    with open(file_name, 'r') as input_file:
        rows = input_file.readlines()

        for row in rows:
            items = row.split(',')
            print(items)

            for i in range(0, len(items), 1):
                #trim any whitespace - spaces, newlines, etc.
                cleaned_item = items[i].strip()
            
            parsed_vals.append(items)

    return parsed_vals


if __name__ == "__main__":
    STUDENTS_FILE_PATH = 'students.csv'

    read_file_into_lists(STUDENTS_FILE_PATH)
