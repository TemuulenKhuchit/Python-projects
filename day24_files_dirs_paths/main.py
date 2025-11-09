# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

STARTING_LETTERS_LOCATION = "./Input/Letters/starting_letter.txt"
INVITED_NAMES_LOCATION = "./Input/Names/invited_names.txt"
READY_TO_SEND_LOCATION = "./Output/ReadyToSend/"

with open(STARTING_LETTERS_LOCATION) as template_file:
    contents = template_file.read()

with open(INVITED_NAMES_LOCATION) as names_file:
    names = names_file.readlines()

for name_raw in names:
    name = name_raw.replace("\n", "")
    with open(f"{READY_TO_SEND_LOCATION}letter_for_{name}.txt", mode="w") as new_file:
        new_contents = contents.replace("[name]", name)
        new_file.write(new_contents)
