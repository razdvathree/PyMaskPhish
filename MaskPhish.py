""""

Made by Tochkaheart=)

"""


import gdshortener
from colorama import *
import os

def mp(): print(Back.GREEN+"MaskPhish"+Style.RESET_ALL)
os.system("clear")
def short_link():
    mp()
    link = str(input("Link: "))
    os.system("clear")
    mp()
    print("build short link...")
    s = gdshortener.ISGDShortener()
    pp_link = s.shorten(link)
    p_link = pp_link[0].split("//")
    
    os.system("clear")
    mp()
    print("Enter words related to the topic of the link, separated by a hyphen. Example: word-word")
    words = str(input(">> "))
    os.system("clear")
    mp()
    link_phish = f"https://google.com-{words}@{p_link[1]}"
    print(f"Your link: {link_phish}")
    
    
    
    
    
    


def menu():
    
    
    print(Back.GREEN+"MaskPhish\n"+Style.            RESET_ALL,"Menu:")
    print("1.Short link\n2.Exit")
    answer = str(input(">> "))
    if "1" in answer:
        os.system("clear")
        short_link()
    elif "2" in answer:
        os.system("clear")
        os._exit(200)
    else: os.system("clear").os._exit(200)


if __name__ == "__main__":
    menu()
