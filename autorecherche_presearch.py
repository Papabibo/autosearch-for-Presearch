import pyautogui
import time
import random

#print(pyautogui.size()) #donne la taille de l'écran
print(pyautogui.position()) #donne la position de la souris

for i in range(40): #repète 40fois la tache suivante:
    time.sleep(1) #pause de 1s
    pyautogui.click(765, 639, duration = 1) #clic sur la zone de recherche
    with open("dico.txt", "r") as file: # ouvre le fichier txt
        allText = file.read()  # lit le fichier txt
        words = list(map(str, allText.split())) #sépare tous les mots du fichier txt
    pyautogui.typewrite(random.choice(words)) #écrit un des mots du fichier au hazard
    pyautogui.press('enter') #appui sur entrée
    time.sleep(4) #pause de 4s
    pyautogui.hotkey('alt', 'left') #appui sur retour arrière
