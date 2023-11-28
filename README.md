# Phase 3 Project Swimmers, SwimTeams, and SwimLeagues Command Line Interface

This program will first greet you with a list of options that you can choose from.

# Example Run Through ONLY:

Please select an option:
0. Exits the program (alternatives are: quit, Quit, Exit, EXIT, QUIT, q, e)
1. Displays this menu again (alternatives are: help, h, HELP, Help, ?)
2. List all instances of Swimmer.
3. Find an instance by ID for Swimmer.
4. Find an instance by NAME for Swimmer.
5. Find an instance by AGE for Swimmer.
6. Create a new instance of Swimmer.
7. Update an instance of Swimmer.
8. Delete an instance of Swimmer.
9. List all instances of SwimTeam.
10. Find an instance by ID for SwimTeam.
11. Find an instance by NAME for SwimTeam.
12. Find an instance by AGE for SwimTeam.
13. Create a new instance of SwimTeam.
14. Update an instance of SwimTeam.
15. Delete an instance of SwimTeam.
16. List all instances of SwimLeague.
17. Find an instance by ID for SwimLeague.
18. Find an instance by NAME for SwimLeague.
19. Find an instance by AGE for SwimLeague.
20. Create a new instance of SwimLeague.
21. Update an instance of SwimLeague.
22. Delete an instance of SwimLeague.
23. List the Swimmers on the SwimTeam.
24. List the SwimLeague for the SwimTeam.
25. List the Swimmers in the SwimLeague.
26. List the SwimTeams in the SwimLeague.
27. List the SwimTeam for the Swimmer.
28. List the SwimLeague for the Swimmer.
> 3
Enter the id: 1
Invalid id 1 used here! No Swimmers found with that id!
> 4
Enter the name here: Twerp
Invalid name Twerp used here! No Swimmers found with that name!
> 5
Enter the age: 10
Invalid age 10 used here! No Swimmers found with that age!
> 0
Goodbye!

# Explanation of Options:

From there, it will do one of the options that you selected.

For EACH Class (Swimmer, SwimTeam, and SwimLeague), you are given options to list all instances of it and see related instances to an instance.

Options: 2, 9, 16, (respectively) and 23 - 28 inclusive list all instances of something or list related objects to one instance. Look up for the instance is done via ID for 23 - 28 inclusive.

For EACH Class (Swimmer, SwimTeam, and SwimLeague), you are given options to look up an instance via ID, NAME, and AGE.

When asked about one instance, instance look up is usually done via ID, but you can also look it via NAME and AGE (options 3 - 5 inclusive, 10 - 12 inclusive, 17 - 19 inclusive), respecively.

For EACH Class (Swimmer, SwimTeam, and SwimLeague), you have options to create a new one, update one, or delete one (options 6 - 8 inclusive, 13 - 15 inclusive, 20 - 22 inclusive), respecively.

Option 0, e, q, Quit, quit, exit, Exit, EXIT, QUIT all exit the program.

Option 1, help, h, Help, HELP, or ? allow you to see the menu again.

If you enter something that is not allowed, it is not allowed or out of range if it was the correct type.

## KNOWN ISSUE
NOTE: Database is cleared when the interface opens, so it is synced with the instances created and displayed by the interface.

# Other Notes:
The database is an SQLite Database. So you can use the SQLite DB Browser, or VS Code and SQLite and SQLite Viewer Extensions to view it, etc. There are other tools out there to view, and modify it. Just to name a few.

# Phase 3 CLI+ORM Project Template

## Learning Goals

- Discuss the basic directory structure of a CLI.
- Outline the first steps in building a CLI.

---

## Introduction

You now have a basic idea of what constitutes a CLI. Fork and clone this lesson
for a project template for your CLI.

Take a look at the directory structure:

```console
.
├── Pipfile
├── Pipfile.lock
├── README.md
└── lib
    ├── models
    │   ├── __init__.py
    │   └── model_1.py
    ├── cli.py
    ├── debug.py
    └── helpers.py
```

Note: The directory also includes two files named `CONTRIBUTING.md` and
`LICENSE.md` that are specific to Flatiron's curriculum. You can disregard or
delete the files if you want.

---

## Generating Your Environment

You might have noticed in the file structure- there's already a Pipfile!

Install any additional dependencies you know you'll need for your project by
adding them to the `Pipfile`. Then run the commands:

```console
pipenv install
pipenv shell
```

---

## Generating Your CLI

A CLI is, simply put, an interactive script and prompts the user and performs
operations based on user input.

The project template has a sample CLI in `lib/cli.py` that looks like this:

```py
# lib/cli.py

from helpers import (
    exit_program,
    helper_1
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            helper_1()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Some useful function")


if __name__ == "__main__":
    main()
```

The helper functions are located in `lib/helpers.py`:

```py
# lib/helpers.py

def helper_1():
    print("Performing useful function#1.")


def exit_program():
    print("Goodbye!")
    exit()
```

You can run the template CLI with `python lib/cli.py`, or include the shebang
and make it executable with `chmod +x`. The template CLI will ask for input, do
some work, and accomplish some sort of task.

Past that, CLIs can be whatever you'd like, as long as you follow the project
requirements.

Of course, you will update `lib/cli.py` with prompts that are appropriate for
your application, and you will update `lib/helpers.py` to replace `helper_1()`
with a useful function based on the specific problem domain you decide to
implement, along with adding other helper functions to the module.

In the `lib/models` folder, you should rename `model_1.py` with the name of a
data model class from your specific problem domain, and add other classes to the
folder as needed. The file `lib/models/__init__.py` has been initialized to
create the necessary database constants. You need to add import statements to
the various data model classes in order to use the database constants.

You are also welcome to implement a different module and directory structure.
However, your project should be well organized, modular, and follow the design
principal of separation of concerns, which means you should separate code
related to:

- User interface
- Data persistence
- Problem domain rules and logic

---

## Updating README.md

`README.md` is a Markdown file that should describe your project. You will
replace the contents of this `README.md` file with a description of **your**
actual project.

Markdown is not a language that we cover in Flatiron's Software Engineering
curriculum, but it's not a particularly difficult language to learn (if you've
ever left a comment on Reddit, you might already know the basics). Refer to the
cheat sheet in this assignments's resources for a basic guide to Markdown.

### What Goes into a README?

This README serves as a template. Replace the contents of this file to describe
the important files in your project and describe what they do. Each Python file
that you edit should get at least a paragraph, and each function should be
described with a sentence or two.

Describe your actual CLI script first, and with a good level of detail. The rest
should be ordered by importance to the user. (Probably functions next, then
models.)

Screenshots and links to resources that you used throughout are also useful to
users and collaborators, but a little more syntactically complicated. Only add
these in if you're feeling comfortable with Markdown.

---

## Conclusion

A lot of work goes into a good CLI, but it all relies on concepts that you've
practiced quite a bit by now. Hopefully this template and guide will get you off
to a good start with your Phase 3 Project.

Happy coding!

---

## Resources

- [Markdown Cheat Sheet](https://www.markdownguide.org/cheat-sheet/)
