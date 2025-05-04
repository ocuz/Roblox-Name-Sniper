import requests
import time
from colorama import Fore, Style, init

init()

banner = r"""
  ______   ____  ____  _____  _____  ____  _____   ______  _____  _________  ________ 
.' ____ \ |_   ||   _||_   _||_   _||_   \|_   _|.' ___  ||_   _||  _   _  ||_   __  |
| (___ \_|  | |__| |    | |    | |    |   \ | | / .'   \_|  | |  |_/ | | \_|  | |_ \_|
 _.____`.   |  __  |    | '    ' |    | |\ \| | | |   ____  | |      | |      |  _| _ 
| \____) | _| |  | |_    \ \__/ /    _| |_\   |_\ `.___]  |_| |_    _| |_    _| |__/ |
 \______.'|____||____|    `.__.'    |_____|\____|`._____.'|_____|  |_____|  |________|
 
 Made by clemouche :)
"""

def check_username(username):
    url = f"https://auth.roblox.com/v1/usernames/validate?Username={username}&Birthday=2000-01-01"
    try:
        response = requests.get(url)
        response_data = response.json()

        code = response_data.get("code")
        if code == 0:
            print(Fore.GREEN + f"VALID: {username}" + Style.RESET_ALL)
            with open("valid.txt", "a") as valid_file:
                valid_file.write(username + "\n")
        elif code == 1:
            print(Fore.LIGHTBLACK_EX + f"TAKEN: {username}" + Style.RESET_ALL)
        elif code == 2:
            print(Fore.RED + f"CENSORED: {username}" + Style.RESET_ALL)
        else:
            print(Fore.YELLOW + f"bruh ({code}): {username}" + Style.RESET_ALL)

    except requests.exceptions.RequestException as e:
        print(Fore.YELLOW + f"glitch {username}: {e}" + Style.RESET_ALL)

def main():
    print(Fore.CYAN + banner + Style.RESET_ALL)
    input("Press Enter to continue...")

    with open("usernames.txt", "r") as file:
        usernames = file.read().splitlines()

    for username in usernames:
        check_username(username)
        time.sleep(0.05)

if __name__ == "__main__":
    main()
