import os
from colorama import Fore, Style, init
from banner import banner
from tools import TOOLS

init()

def clear():
    os.system("clear")

def show_menu():
    clear()
    banner()
    print(Fore.GREEN + "\n=== SASA HACK TOOLS CATEGORIES ===\n")

    for category in TOOLS:
        print(Fore.YELLOW + f"[{category}]")

    print(Fore.CYAN + "\nType category name (OSINT, NETWORK, WEB, DEV)")
    print("Type exit to quit\n")

def show_tools(category):
    clear()
    banner()
    print(Fore.BLUE + f"\n--- {category} TOOLS ---\n")

    for key, tool in TOOLS[category].items():
        print(Fore.GREEN + f"[{key}] {tool[0]}")

    print("\nType tool number or back")

def install_tool(choice, category):
    name, repo = TOOLS[category][choice]
    print(Fore.RED + f"\nInstalling {name}...\n")
    os.system(f"git clone {repo}")

while True:
    show_menu()
    cat = input(Fore.WHITE + "Category > ").upper()

    if cat == "EXIT":
        break

    if cat in TOOLS:
        while True:
            show_tools(cat)
            ch = input(Fore.WHITE + "Select Tool > ")

            if ch == "back":
                break

            if ch in TOOLS[cat]:
                install_tool(ch, cat)
                input("\nPress Enter to continue...")
