# Generate Usernames Script

A simple Python script to generate potential usernames from a list of full names. It supports multiple username formats, including admin-specific formats like `jd.admin`.

## Features
- Reads a list of names from a text file.
- Generates various potential usernames, including:
  - `j.doe`
  - `jdoe`
  - `doej`
  - `j.doe.admin`
- Handles duplicates and filters out usernames with fewer than three characters.

## Requirements
- Python 3.x

## Installation
1. Clone the repository:
```
git clone https://github.com/yourusername/generate-usernames.git
cd generate-usernames
```
2. Make the script executable:
```
chmod +x generateusers.py
```

## Usage
Run the script with a text file containing the list of names (one name per line).

### Command Syntax
```
./generateusers.py -u <users.txt>
```

### Example
Input file (`users.txt`):
```
Fergus Smith
Hugo Bear
Steven Kerb
Shaun Coins
Bowie Taylor
Sophie Driver
```

Command:
```
./generateusers.py -u users.txt
```

Output:
```
Generated Usernames:
f.smith
fsmith
smithf
fergus.smith
f_smith
fergussmith
ferguss
fs.admin
h.bear
hbear
bearh
hugo.bear
...
```

## Error Handling
- If the input file is missing:
```
Error: The file '<users.txt>' does not exist. Please provide a valid user list.
```
- If incorrect arguments are passed:
```
Usage: ./generateusers.py -u <users.txt>
  -u <users.txt> : Path to the text file containing the user list (one name per line).

Example:
  ./generateusers.py -u users.txt
```

## Contribution
Feel free to open an issue or submit a pull request if you want to add new features or fix bugs.


