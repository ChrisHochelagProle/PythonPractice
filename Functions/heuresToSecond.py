def heures_en_secondes(h, m, s):
    return h*3600 + m*60 + s


def secondes_en_heures(secondes):
    heures = secondes // 3600
    secondes_restantes = secondes - (heures*3600)
    minutes = secondes_restantes // 60
    secondes_restantes = secondes_restantes - (minutes*60)
    return heures, minutes, secondes_restantes


def seconde_heures_format(secondes):
    return f"{secondes // 3600}:{(secondes % 3600)//60}:{((secondes % 3600) % 60)}"


print("Que voulez-vous faire\n"
      "1) Convertir h:m:s en secondes\n"
      "2) Convertir secondes en h:m:s\n")

while True:
    choice = input("Quel est votre choix : ")
    if choice == "1":
        h = int(input("Heures: "))
        m = int(input("Minutes: "))
        s = int(input("Secondes: "))
        hms = input("Entrez selon h:m:s : ")
        print(hms.split(":"))
        hms = hms.split(":")
        print("La conversion demandee:", heures_en_secondes(h, m, s), "\n")
        print("La conversion demandee:", heures_en_secondes(int(hms[0]), int(hms[1]), int(hms[2])), "\n")
    elif choice == "2":
        secondes = int(input("Entrez un nombre x de secondes: "))
        secondesToHeures = secondes_en_heures(secondes)
        h = str(secondesToHeures[0])
        m = str(secondesToHeures[1])
        s = str(secondesToHeures[2])
        # print("La conversion demandee:", h+":"+m+":"+s, "\n")
        print("La conversion demandee:", seconde_heures_format(secondes), "\n")
    else:
        break
