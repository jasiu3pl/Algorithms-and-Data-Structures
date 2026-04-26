import time
import random

class Element:
    def __init__(self, dane, priorytet):
        self.__dane = dane
        self.__priorytet = priorytet
        
    def __lt__(self, other):
        return self.__priorytet < other.__priorytet
    
    def __gt__(self, other):
        return self.__priorytet > other.__priorytet
    
    def __repr__(self):
        return f"{self.__priorytet} : {self.__dane}"


def insertion_sort(tab):
    for i in range(1, len(tab)):
        j = i
        while j > 0 and tab[j] < tab[j-1]:
            tab[j-1], tab[j] = tab[j], tab[j-1]
            j -= 1
            
    return tab

def shell_sort_classic(tab):
    n = len(tab)
    h = n // 2
    
    while h > 0:
        for i in range(h, n):
            j = i
            while j >= h and tab[j] < tab[j-h]:
                tab[j-h], tab[j] = tab[j], tab[j-h]
                j -= h
     
        h = h // 2
    
    return tab

def shell_sort_modified(tab):
    n = len(tab)
    h = 1
    while (3 * h + 1) < (n // 3):
        h = 3 * h + 1
    
    while h > 0:
        for i in range(h, n):
            j = i
            while j >= h and tab[j] < tab[j-h]:
                tab[j-h], tab[j] = tab[j], tab[j-h]
                j -= h
     
        h = h // 3
    
    return tab

def main():
    pass
    
    
if __name__ == "__main__":
    main()