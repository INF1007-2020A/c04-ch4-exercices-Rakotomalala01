#!/usr/bin/env python
# -*- coding: utf-8 -*-
https://teams.microsoft.com/l/channel/19%3ac99a11edf1344df3be675b2052998498%40thread.tacv2/Cours%2520C04?groupId=0f3c8839-4918-45bf-b83d-a9b2128eb0c7&tenantId=d2ee49eb-e94b-49d7-a34a-2fb97a949bfc



def is_even_len(string: str) -> bool:
    if len(string) % 2 == 0
        return True
    else :
        return False

def remove_third_char(string: str) -> str:
    pass
    return string[0:2]+string[3:]


def replace_char(string: str, old_char: str, new_char: str):
    for i in range (len(string)):
        if string[i]==old_char
    return string[i]+ new char+ string[i+1]

def get_number_of_char(string: str, char: str) -> int:
    pass
for i in range (len string):
    a=0
    if string[i]==char
    a+=1
    return a


def get_number_of_words(sentence: str, word: str) -> int:
    pass
    for current 

def main()-> None:
    chaine = "Bonjour!"
    if is_even_len(chaine):
        print(f"Le nombre de caractère dans la chaine {chaine} est pair")
    else:
        print(f"Le nombre de caractère dans la chaine {chaine} est impair")

    chaine = "salut monde!"
    print(f"On supprime le 3e caratère dans la chaine: {chaine}. Résultat : {remove_third_char(chaine)}")

    chaine = "hello world!"
    print(f"On remplace le caratère w par le caractère z dans la chaine: {chaine}. Résultat : {replace_char(chaine, 'w', 'z')}")

    print(f"Le nombre d'occurrence de l dans hello est : {get_number_of_char(chaine, 'l')}")
    
    chaine = "Baby shark doo doo doo doo doo doo"
    print(f"L'occurence du mot doo dans la chaine {chaine} est: {get_number_of_words(chaine, 'doo')}")


if __name__ == '__main__':
    main()

