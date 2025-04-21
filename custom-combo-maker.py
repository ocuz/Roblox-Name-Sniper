cons = "abcdefghijklmnopqrstuvwxyz0123456789"

combos = [f"{first}{second}{third}" for first in cons for second in cons for third in cons]

with open("usernames.txt", "w") as file:
    for combo in combos:
        file.write(combo + "\n")

print("Combos generated to usernames.txt")
