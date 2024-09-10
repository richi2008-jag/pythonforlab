import random

char_name = input("Enter your character name here:")
clan = input("what is your clan name(e.g., uchiha, uzumaki, hyuga): ")
main_jutsu = input("what is your main jutsu(e.g., rasengan, chidori, shadow clone jutsu): ")
team = input("what is your team number:")
rank= input("what is your rank shinobi(e.g., genin, chunin,jonin, anbu, kage):")
Ninja_war=input("Do you :")

print("-------------------Naruto Bio----------------------")
print(f"Name: {char_name}")
print(f"Clan: {clan}")
print(f"Main_jutsu:{main_jutsu}")
print(f"Team:{team}")
print(f"Rank:{rank}")

print("Your character name is " + char_name + " and your clan is "  + clan )
if clan == "uchiha":
  print("You have a sharagian ") 
if clan =="uzumaki":
  print("you have a enhanced charka pool")
if clan == "hyuga":
  print("you have a byakugan.")

clans = ["uchiha", "uzumaki", "hyuga"]
clan =random.choice(clans)
print(clan)

main_jutsus =[ "rasengan","chidori", "shawdow clone jutsu"]
main_jutsu =random.choice(main_jutsus)
print(main_jutsu)

ranks =["genin","chunin","jonin","anbu","kage",]
rank=random.choice(ranks)
print(rank)
if rank.lower() == "kage":
  print(f"{char_name} Welcome Hokage") 
Ninjas_wars=["yes","No",]
Ninja_war=random.choice(Ninjas_wars)
print(Ninja_war) 
goat="king"
print(goat)