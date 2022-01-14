#Szöveg alapú játék 
import time
import random

number_of_life = 3

def show_number_of_life():
    print("♡" * number_of_life)

def reverse_word(word): 
    word=word[::-1]
    return word

def game_over():
    if number_of_life < 1:
        print("Vesztettél!")
        exit()

print('A "játék" lényege az, hogy a megfelelő válasz megadásával tovább haladj.')
print("Három élettel rendelkezel, minden rossz választásnál 1 élet levonódik.")
print("Ha az életeid száma eléri a 0-át, vesztettél!")
time.sleep(3)

player_name = input('Add meg a neved! ')

print(player_name,'éppen a boltba indult, mikor látta, hogy lemerült a kocsiban az aksi, ezért gyalog kell mennie.')
time.sleep(2)

time.sleep(3)

print(player_name, "után egy férfi kiált egy asztal mögül. Meghívja egy kör gyufázásra. Hogy tovább haladj, találd meg melyik pohár alatt van a kupak!")
time.sleep(2)
cups = ["x", "x"]

print(cups)

vendor = input("Válaszd ki, melyik alatt van a golyó! (1/2) ")

while vendor is not "2":
    print("Sajnos nem ez alatt volt! Vesztettél egy életet!")
    number_of_life -= 1
    show_number_of_life()
    game_over()
    vendor = input("Válaszd ki, melyik alatt van a golyó! (1/2) ")
    
if vendor is "2":
    print("Sikeresen megtaláltad a golyót! Tovább haladhatsz!")

print(player_name, "egy hatalmas pocsolya előtt áll, hogy kikerülje, meg kell oldanod a matematikai feladatot.")
time.sleep(3)
help_list = []
fake_number1 = random.randint(1,100)
fake_number2 = random.randint(1,100)
help_list.append(fake_number1)
help_list.append(fake_number2)
random_number1 = random.randint(1,100)
random_number2 = random.randint(1,100)
print(random_number1, "*", random_number2)
math_puzzle = random_number1 * random_number2
help_list.append(math_puzzle)
print("Válaszd ki belőle a jó számot!:", help_list)
solution = int(input("Add meg a feladat megoldását! ")) 

while math_puzzle != solution:
    print("Rossz válasz!")
    number_of_life -= 1
    show_number_of_life()
    game_over()
    int(input("Add meg a feladat megoldását! "))

if math_puzzle == solution:
    print("Eltaláltad! Mehetsz tovább!")
    time.sleep(3)
    print(player_name, "egy zárt kapu előtt találja magát! Hogy ki tudja nyitni a kaput, be kell írnod helyesen a szavakat! ")
    reversed_word = "bejelentkeztethettelek"
    reversed_word_final = print(reverse_word(reversed_word))
    reversed_word_guess = input("Írd be ezt a szót helyesen! ")

while reversed_word != reversed_word_guess:
    print("Ez helytelen! Próbáld újra!")
    number_of_life -= 1
    show_number_of_life()
    game_over()
    reversed_word_guess = input("Írd be ezt a szót helyesen! ")

if reversed_word == reversed_word_guess: 
    print("Gratulálok! Sikeresen teljesítetted a feladatokat!")
    print("Sikeresen elértél a boltba!")
    time.sleep(2)
    print(player_name,"benyúl a zsebébe...")
    time.sleep(3)
    print("Otthon maradt a tárcája...")