# TODO: Create a letter using starting_letter.txt
with open("./Input/Letters/starting_letter.txt") as letter:
    letter_greeting=letter.readline()
    letter_full=letter.read()

with open("./Input/Names/invited_names.txt") as name:
    lines = [line.rstrip() for line in name]
    for recipient_name in lines:
        x=letter_greeting.replace("[name]", recipient_name)
        ready_mail=f"{x}{letter_full}"
        with open(f"./Output/ReadyToSend/Mail_for_{recipient_name}.txt",mode='w') as mail:
            mail.write(ready_mail)






