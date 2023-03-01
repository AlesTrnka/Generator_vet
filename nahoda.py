import os
import random as r
from data import jaky, kdo, jak, co_delal, kde

class Nahoda:
    """ Třída s funkcemi pro tvorbu náhodných vět a průvodcem prgramem"""
    
    def __init__(self):
        pass
        
    def vypis_vetu(self, pocet):    # Vypíše množství náhodných vět dle zadaného počtu.
        for i in range(pocet):
            print(f"{r.choice(jaky).capitalize()} {r.choice(kdo)} {r.choice(jak)} {r.choice(co_delal)} {r.choice(kde)}.")
    
    def spustit_program(self):      # Průvodce programem. Zjistí požadovaný počet náhodných vět
        while True:
            os.system("cls")
            print("GENERÁTOR NÁHODNÝCH VĚT")
            print("ˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇ\n")
            try:                    # Ošetření vstupu od uživatele
                pocet = int(input("Kolik náhodných vět chcete vytvořit? (limit 15 vět)\n"))
                if pocet in range(1, 16):
                    os.system("cls")
                    print(f"Zde je {pocet} náhodných vět:\n ")
                    self.vypis_vetu(pocet)
                    pokracovat = input("\nPokračovat? Pro ukončení zadejte 'ne':\n")
                    if pokracovat == "ne":
                        return False
                else:
                    os.system("cls")
                    print(f"Je možné zadat pouze celé číslo v rozmezí 1-15.")
                    input("\nPokračujte stiskem klávesy Enter . . .")
            except ValueError:      # vyjímka, pokud uživatel nezadá celé číslo
                os.system("cls")
                print(f"Je možné zadat pouze celé číslo v rozmezí 1-15.")
                input("\nPokračujte stiskem klávesy Enter . . .")