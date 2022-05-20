string = "Hello world"

print(len(string))

print("Bonjour"+" toi.")

extract = string[0:5]

print(extract)

msg = "Bienvenu au cours {}"
msg = msg.format("Intro a la programmation")
print(msg)

prenom = "chris"
cours = "Intro a la programmation"
msg = f"Bienvenu {prenom} dans le cours {cours}!"
print(msg)
print(msg.count(prenom))
print(msg.upper())
print(msg.lower())
print(msg.replace(prenom, "JP"))
print(msg.find(prenom))
print(msg[9:])
