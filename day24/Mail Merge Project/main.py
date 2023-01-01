with open("Input/Names/invited_names.txt") as names:
    name_list = names.readlines()
    for name in name_list:
        name = name.strip("\n")
        with open("Input/Letters/starting_letter.txt") as letter:
            l = letter.read()
            new_l = l.replace("[name]", name)
            with open(f"Output/ReadyToSend/{name}.txt", mode="w") as letter_to_send:
                letter_to_send.write(new_l)



