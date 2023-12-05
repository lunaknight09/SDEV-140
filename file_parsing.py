import os
from datetime import datetime
from typing import Dict
from typing import List


def cleanup_data(data: List[List[str]], input_date_string: str,
                 output_date_string: str,
                 data_start_line_number: int) -> List[List[str]]:
    """
    Cleans up the source data.
    Name is split into first and last name.
    Date of birth is converted to the desired format.
    Grade is validated.
    Output is in the format: [last_name, first_name, date_of_birth, grade]
    """
    cleaned_data = []
    line_number = data_start_line_number

    for record in data:
        if len(record) != 4:
            raise ValueError(
                f"Error on line {line_number}: Invalid number of fields in record."
            )

        ##################################################
        # ID
        ##################################################
        # We are assuming ID will be six characters.
        student_id = name_parts = record[0]
        if len(student_id) != 6:
            raise ValueError(
                f"Error on line {line_number}: ID must be six characters.")

        ##################################################
        # First Name and Last Name
        ##################################################
        # Split name into first and last name
        name_parts = record[1].split(' ')
        if len(name_parts) != 2:
            raise ValueError(
                f"Error on line {line_number}: First and last name are required in name field."
            )
        first_name = name_parts[0]
        last_name = name_parts[1]

        ##################################################
        # Date of Birth
        ##################################################
        # Date of birth is optional
        # If provided make sure it's a valid date
        date_of_birth = record[2]
        formatted_date_of_birth = ''
        if date_of_birth != '':
            try:
                # Convert the date to a datetime data type
                date = datetime.strptime(date_of_birth, input_date_string)

                # Convert the date back to a string in the desired format
                formatted_date_of_birth = date.strftime(output_date_string)

            except ValueError:
                raise ValueError(
                    f"Error on line {line_number}: Invalid date of birth.")

        ##################################################
        # Grade
        ##################################################
        # Grade needs to match one of the following.
        VALID_GRADES = ['A', 'B', 'C', 'D', 'F']
        grade = record[3]

        if grade.upper() not in VALID_GRADES:
            raise ValueError(f"Error on line {line_number}: Invalid grade.")

        # Add the cleaned data to the list
        cleaned_data.append([
            student_id, last_name, first_name, formatted_date_of_birth, grade
        ])
        line_number += 1

    return cleaned_data


def parse_csv_to_stripped_list(file_path: str) -> List[List[str]]:
    """
    Parses a CSV file into a list of lists.
    The outer list represents the rows in the CSV file.
    The inner lists represent the fields in each row.
    The only cleanup performed is to strip whitespace from the fields.
    """
    data = []

    # Use a context manager to open the file.
    with open(file_path, 'r') as file:
        lines = file.readlines()

        for line in lines:
            # Split the line into a list of fields.
            fields = line.split(',')
            # Strip whitespace from each field.
            for i in range(len(fields)):
                fields[i] = fields[i].strip()
            data.append(fields)

    return data


def print_students(data: List[List[str]]) -> None:
    """
    Prints the student data in a formatted table.
    """
    # The colon indicates we are using the format method.
    # The format method will automatically convert the data to the desired type.
    # The less than symbol indicates we are left justifying the field.
    # The number indicates the width of the field.
    # The letter indicates the data type.
    # s = string (default)
    # d = integer
    # f = float
    # e = scientific notation
    # % = percentage
    print("{:<10}{:<20}{:<10}{:>10}".format("ID", "Name", "DOB", "Grade"))
    print("{:<10}{:<20}{:<10}{:>10}".format("--", "----", "---", "-----"))
    for record in data:
        # Use the format method to pad each field to a specific width
        print("{:<10}{:<20}{:<10}{:>10}".format(record[0],
                                                f"{record[1]}, {record[2]}",
                                                record[3], record[4]))


def remove_duplicates(data: List[List[str]]) -> List[List[str]]:
    """
    Removes duplicate records from the data.
    Data in the file are unique by ID.
    """
    added_ids = []
    unique_data = []

    for record in data:
        student_id = record[0]
        if student_id not in added_ids:
            added_ids.append(student_id)
            unique_data.append(record)

    return unique_data


def validate_header_fields(header_fields: List[str],
                           expected_fields: List[str]) -> bool:
    """
    Validates if the header fields in a CSV file match the expected fields.
    Comparison is case-insensitive.
    Returns True if the header fields match the expected fields, False otherwise.
    """

    # Check if the number of fields provided in the file header matches
    # the number of fields expected.
    if len(header_fields) != len(expected_fields):
        return False

    for i in range(0, len(header_fields), 1):
        if header_fields[i].lower() != expected_fields[i].lower():
            return False

    return True


def write_output_to_file(output_file: str, data_rows: List[List[str]]) -> None:
    """
    Writes the provided data rows to a file.
    """
    # Use a context manager to open the file.
    with open(output_file, 'w') as file:
        for record in data_rows:
            # Join the fields into a single string separated by commas.
            # Add a newline character to the end of each line.
            file.write(','.join(record) + '\n')


# Main script
if __name__ == "__main__":

    STUDENTS_FILE_PATH = 'students.csv'
    STUDENTS_HEADER_FIELDS = ['id', 'name', 'dob', 'grade']
    OUTPUT_PATH = 'output.csv'

    # Parse CSV
    # Be sure to wrap this in a try/except block to handle the FileNotFoundError
    try:
        parsed_data = parse_csv_to_stripped_list(STUDENTS_FILE_PATH)
    except FileNotFoundError as e:
        print("File not found: " + e)
        exit()

    # Check for an empty file
    if len(parsed_data) == 0:
        print("Empty file.")
        exit()

    # Check if the header field is in the expected format
    # We haven't seen 'exit()' before. It's a built-in function that
    # terminates the program. It's similar to 'return' in a function, but
    # it's used in the main script instead of a function.
    header_row = parsed_data[0]
    if not validate_header_fields(header_row, STUDENTS_HEADER_FIELDS):
        print("Invalid header fields. Expected:" + str(STUDENTS_HEADER_FIELDS))
        exit()

    # This is an example of list slicing. It's a way to get a subset of a list.
    data_rows = parsed_data[1:]

    # Data Cleanup
    try:
        data_rows = cleanup_data(data_rows, '%Y-%m-%d', '%Y%m%d', 2)
    except ValueError as e:
        print(e)
        exit()

    # Remove duplicates
    data_rows = remove_duplicates(data_rows)

    # Sort the data by last name
    # TODO: Sort with a basic sorting algorithm instead of built-in sort.
    data_rows = sorted(data_rows, key=lambda x: x[1])

    # Display the results - print to the console
    print_students(data_rows)

    # Write the results to a file
    try:
        write_output_to_file(OUTPUT_PATH, data_rows)
    except PermissionError as e:
        print("Unable to write to file: " + e)
        exit()
