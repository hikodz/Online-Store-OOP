from pprint import pprint



from  inquirer import prompt, List  # noqa

questions = prompt([
    List(
        "size",
        message="What size do you need?",
        choices=["Jumbo", "Large", "Standard", "Medium", "Small", "Micro"],
    ),
])

print(questions["size"])