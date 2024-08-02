import subprocess
import os
import distro
from termcolor import colored

type = distro.like()


def update():  # this function update the operating system
    name = distro.name()  # os variable holds the name of distros
    y = str(
        input(
            colored(
                "[?] Do you want to update your "
                + name
                + "\n[!] Enter your choice(y/n) ====> ",
                "yellow",
            )
        )
    )
    if y == "y" or y == "Y":
        print(colored("[!] Updating your " + name + " ...", "red"))
        os.system("sleep 2")
        if type == "arch":
            os.system(
                "sudo pacman -Syu"
            )  # linux command to update arch linux or arch based distros
        else:
            os.system(
                "sudo apt-get update && sudo apt-get upgrade"  # linux command to update debian linux or debian based distros
            )
        is_flatpak_installed()
    else:
        is_flatpak_installed()


def is_flatpak_installed():  # this function check wheather flatpak is installed or not
    print(colored("[!] checking if flatpak is installed or not ...", "yellow"))
    os.system("sleep 2")
    try:
        subprocess.check_output(["flatpak", "--version"])
        print(colored("[*] Flatpak is installed.", "green"))
        print(colored("[!] Continuing Installation ...", "yellow"))
        os.system("sleep 2")
        main()

    except FileNotFoundError:
        print(colored("[!] Flatpak is not installed.", "red"))
        print(colored("[!] Installing flatpak ...", "yellow"))
        os.system("sleep 2")
        if type == "arch":
            software.arch("flatpak")
        else:
            software.debian("flatpak")
        print(
            colored(
                "[*] Installation of flatpak in complete , Continuing to package installion ...",
                "green",
            )
        )
        os.system("sleep 1")
        main()


class software:  # this class is made to use arch/debian/flatpak command repeatedly
    def arch(software):
        os.system("sudo pacman -S --noconfirm --needed " + software)

    def debian(software):
        os.system("sudo apt-get install " + software)

    def flatpak(software):
        os.system("flatpak install flathub " + software)


def main():
    print(
        colored("--------------------------------------------------------", "magenta")
    )
    print(colored("[*] This is python program to install software", "green"))
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
    choice = str(
        input(colored("[?] ====> ", "blue"))  # takes the input from user as a string
    )

    print(
        colored("--------------------------------------------------------", "magenta")
    )
    if choice == "t" or choice == "T":
        software.flatpak("io.atom.Atom  org.kde.ghostwriter")
        if type == "arch":
            software.arch("kate")
        else:
            software.debian("kate")
    elif choice == "c" or choice == "C":
        software.flatpak(
            "com.jetbrains.PyCharm-Community org.kde.kdevelop com.vscodium.codium dev.zed.Zed"
        )
    elif choice == "o" or choice == "O":
        software.flatpak(
            "com.wps.Office org.libreoffice.LibreOffice org.onlyoffice.desktopeditors "
        )
    elif choice == "g" or choice == "G":
        software.flatpak(
            "org.upscayl.Upscayl org.inkscape.Inkscape org.gimp.GIMP org.blender.Blender"
        )
    elif choice == "i" or choice == "I":
        software.flatpak(
            "com.google.Chrome org.mozilla.firefox org.torproject.torbrowser-launcher com.discordapp.Discord org.filezillaproject.Filezilla com.github.bajoja.indicator-kdeconnect org.telegram.desktop org.qbittorrent.qBittorrent com.anydesk.Anydesk"
        )
    elif choice == "m" or choice == "M":
        software.flatpak("org.videolan.VLC org.obsstudio.Studio")
    elif choice == "s" or choice == "S":
        software.flatpak("org.kde.konsole org.kde.dolphin ")
        if type == "arch":
            software.arch("virtualbox plasma-systemmonitor alacritty discover")
        else:
            software.debian(
                "ksysguard gnome-system-monitor virtualbox plasma-discover alacritty"
            )
    elif choice == "e" or choice == "E":
        os.system("exit")
        os.system("clear")
    else:
        main()


update()
