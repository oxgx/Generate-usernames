#!/usr/bin/env python3

import sys
import os

def generate_potential_usernames(file_path):
    try:
        # Check if the file exists
        if not os.path.isfile(file_path):
            print(f"Error: The file '{file_path}' does not exist. Please provide a valid user list.")
            sys.exit(1)

        # Read the file with names
        with open(file_path, 'r') as file:
            names = file.readlines()
        
        usernames = []
        for full_name in names:
            full_name = full_name.strip()  # Remove leading/trailing whitespace
            parts = full_name.split()
            if len(parts) >= 2:
                first_name = parts[0]
                last_name = parts[1]
                # Add various potential username formats
                usernames.extend([
                    f"{first_name[0]}.{last_name}".lower(),  # f.smith
                    f"{first_name[0]}{last_name}".lower(),   # fsmith
                    f"{last_name}{first_name[0]}".lower(),   # smithf
                    f"{first_name}.{last_name}".lower(),     # fergus.smith
                    f"{first_name[0]}_{last_name}".lower(),  # f_smith
                    f"{first_name}{last_name}".lower(),      # fergussmith
                    f"{first_name}{last_name[0]}".lower(),   # ferguss
                    f"{first_name[0]}{last_name[0]}.admin".lower()  # jd.admin
                ])
        
        # Remove duplicates and filter out usernames with 2 characters only
        usernames = list(set(usernames))
        usernames = [u for u in usernames if len(u) > 2]

        # Print the generated usernames
        print("\nGenerated Usernames:")
        for username in usernames:
            print(username)

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist. Please provide a valid user list.")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    # Check if the script is called with a file argument
    if len(sys.argv) != 3 or sys.argv[1] != "-u":
        print("\nUsage: ./generateusers.py -u <users.txt>")
        print("  -u <users.txt> : Path to the text file containing the user list (one name per line).")
        print("\nExample:")
        print("  ./generateusers.py -u users.txt")
        sys.exit(1)

    # Get the file path from the command-line arguments
    file_path = sys.argv[2]
    generate_potential_usernames(file_path)
