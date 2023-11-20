def validate_input(user_input):
    if len(user_input) < 3 or user_input[1] != ' ' or user_input[0] not in ['a', 'b']:
        return False
    return True

def extract_name(user_input):
    return user_input[2:]

def assign_to_team(team, name):
    if team == 'a':
        team_a.append(name)
    else:
        team_b.append(name)

def display_teams():
    print("A-Team:", team_a)
    print("B-Team:", team_b)

def main():
    print("Welcome to the Team Assignment Program!")
    while True:
        user_input = input("Enter 'a [name]' or 'b [name]' to assign a member, or type 'quit' to exit: ")

        if user_input.lower() == 'quit':
            break

        if validate_input(user_input):
            team = user_input[0]
            name = extract_name(user_input)
            assign_to_team(team, name)
            display_teams()
        else:
            print("Invalid input. Please enter a valid assignment in the format 'a [name]' or 'b [name]'.")

if __name__ == "__main__":
    team_a = []
    team_b = []
    main()