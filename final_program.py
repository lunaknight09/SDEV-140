import datetime

def parse_date(date_str):
    try:
        date_object = datetime.datetime.strptime(date_str, "%Y/%m/%d").date()
        return date_object.strftime("%Y%m%d")
    except ValueError:
        print(f"Invalid visit date: {date_str}. Skipping visit date.")
        return None

def read_dat_file(file_path):
    data = {}
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line and '~' in line:
                fields = [field.strip() for field in line.split('~')]
                account_id = fields[0]
                
                if len(account_id) != 5:
                    print(f"Invalid Account ID: {account_id}. Skipping account record.")
                    continue

                dates = [parse_date(date) for date in fields[1:]]
                valid_dates = [date for date in dates if date is not None]

                if valid_dates:
                    data[account_id] = valid_dates

    return data

def main():
    file_path = 'final_program_input-1.dat'
    healthcare_data = read_dat_file(file_path)

    while True:
        user_input = input("Enter an account ID or 'q' to quit: ")
        if user_input.lower() == 'q':
            break

        if user_input in healthcare_data:
            account_id = user_input
            visit_dates = healthcare_data[account_id]
            formatted_dates = ';'.join(visit_dates)
            print(f"{account_id};{formatted_dates}")
        else:
            print("Account ID does not exist.")

if __name__ == "__main__":
    main()
