# PyContact and Notes Manager

## Overview
This project provides a command-line interface (CLI) tool for managing contacts and notes efficiently. 
It includes commands for adding, updating, searching, and removing contacts and notes, 
as well as managing tags and additional fields like addresses, birthdays, and emails.

## Installation
```sh
Pull repository locally
git pull https://github.com/chertoha/woolf-python-basic-final.git


Create a virtual environment:
python -m venv venv

Activate virtual environment:
Windows:
.\venv\Scripts\activate

Linux/MacOS:
source venv/bin/activate

Install dependencies from the requirements.txt file:
pip install -r requirements.txt

Start CLI application:
python main.py
```
---

## Contact Management Commands

### find-contacts
- Description: Searches for contacts.
- Usage:
  - find-contacts: Returns all contacts.
  - find-contacts <search_term>: Returns contacts where the search term matches any field.

### add-contact
- Description: Adds a new contact.
- Usage:
  - add-contact <name> <phone>
  - Requires at least two arguments (name and phone).
  - Adds a phone to an existing contact or creates a new contact if it doesn't exist.

### remove-contact
- Description: Deletes a contact by name.
- Usage:
  - remove-contact <name>
  - Requires confirmation (`Y` or `N`).

### update-name
- Description: Updates the name of an existing contact.
- Usage:
  - update-name <old_name> <new_name>

### update-phone
- Description: Updates a phone number for an existing contact.
- Usage:
  - update-phone <name> <old_phone> <new_phone>
  - Validates input and ensures the new phone does not already exist.

### remove-phone
- Description: Deletes a phone number from a contact.
- Usage:
  - remove-phone <name> <phone>
  - Requires confirmation (`Y` or `N`).

### address
- Description: Adds or updates the address for a contact.
- Usage:
  - address <name> <address>

### clear-address
- Description: Clears the address field of a contact.
- Usage:
  - clear-address <name>
  - Requires confirmation (`Y` or `N`).

### birthday
- Description: Adds or updates the birthday of a contact.
- Usage:
  - birthday <name> <DD.MM.YYYY>

### clear-birthday
- Description: Clears the birthday field of a contact.
- Usage:
  - clear-birthday <name>
  - Requires confirmation (`Y` or `N`).

### birthdays
- Description: Displays a list of upcoming birthdays in entered days.
- Usage:
  - birthdays <days>
  - Ensures the number of days is an integer. If not, returns "number of days must be an integer".

### email
- Description: Adds or updates the email for a contact.
- Usage:
  - email <name> <email>
  - Validates the email format.

### clear-email
- Description: Clears the email field of a contact.
- Usage:
  - clear-email <name>
  - Requires confirmation (`Y` or `N`).

---

## Notes Management Commands

### add-note
- Description: Adds a new note.
- Usage:
  - add-note <title> <text>

### update-note
- Description: Updates the text of an existing note.
- Usage:
  - update-note <title> <text>

### update-note-title
- Description: Updates the title of an existing note.
- Usage:
  - update-note-title <old_title> <new_title>

### remove-note
- Description: Deletes a note.
- Usage:
  - remove-note <title>
  - Requires confirmation (`Y` or `N`).

### find-notes
- Description: Searches for notes by title or text.
- Usage:
  - find-notes <search_term>
  - Returns all notes if no argument is provided. 

### add-tags
- Description: Adds tags to an existing note.
- Usage:
  - add-tags <title> <tags>
  - Ignores duplicate tags.

### remove-tags
- Description: Removes tags from an existing note.
- Usage:
  - remove-tags <title> <tags>
  - Requires confirmation (`Y` or `N`).

### find-tags
- Description: Searches for notes by tags.
- Usage:
  - find-tags <tag>

---
## Help Command
- Description: Displays a list of all available commands with descriptions and examples.
- Usage:
  - help

---

## Notes
- All confirmation prompts accept Y or N in any case (e.g., y, n, Y, `N`).
- Proper validation ensures data integrity and user-friendly error messages.
