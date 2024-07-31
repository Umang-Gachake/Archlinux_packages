import os

from termcolor import colored


def software(software):
    os.system("sudo pacman -S --noconfirm --needed " + software)


def main():
    print(colored("\n[*] This is python program to install software", "green"))
    print(colored("[*] Which type software do you want to install?", "green"))

    print(
        colored("--------------------------------------------------------", "magenta")
    )

    print(colored("[+] TEXT EDITOR", "cyan"))
    print(colored("[+] CODE EDITOR", "cyan"))
    print(colored("[+] OFFICE", "cyan"))
    print(colored("[+] GRAPHICS SOFTWARE", "cyan"))
    print(colored("[+] INTERNET", "cyan"))
    print(colored("[+] MULTIMEDIA", "cyan"))
    print(colored("[+] SYSTEM", "cyan"))
    print(colored("[+] EXIT", "cyan"))

    print(
        colored("--------------------------------------------------------", "magenta")
    )

    print(
        colored("[*] Enter first letter of your choice(eg.t for text editor).", "blue")
    )
    choice = str(input(colored("[?] ====> ", "blue")))

    print(
        colored("--------------------------------------------------------", "magenta")
    )

    if choice == "t" or choice == "T":
        software("kate ghostwriter")
    elif choice == "c" or choice == "C":
        software("pycharm-community-edition kdevelop vscodium zed")
    elif choice == "o" or choice == "O":
        software("wps-office libreoffice-fresh onlyoffice-bin freeoffice")
    elif choice == "g" or choice == "G":
        software("blender gimp inkscape upscayl-bin")
    elif choice == "i" or choice == "I":
        software(
            "chromium firefox torbrowser-launcher discord filezilla kdeconnect telegram-desktop qbittorrent anydesk-bin"
        )
    elif choice == "m" or choice == "M":
        software("vlc obs-studio")
    elif choice == "s" or choice == "S":
        software("virtualbox plasma-systemmonitor alacritty dolphin discover konsole")
    elif choice == "e" or choice == "E":
        os.system("exit")
        os.system("clear")
    else:
        main()


main()
