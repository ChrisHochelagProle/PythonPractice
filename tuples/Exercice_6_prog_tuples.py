def java_mastery(etudiants):
    java = 0
    for student in etudiants:
        for information in student:
            if information == "java":
                java += 1
    return java


def language_mastery(etudiants):
    java = ["Java", 0]
    c_sharp = ["C#", 0]
    python = ["Python", 0]
    for student in etudiants:
        for information in student:
            if information == "java":
                java[1] += 1
            elif information == "python":
                python[1] += 1
            elif information == "C#":
                c_sharp[1] += 1
    if java[1] >= c_sharp[1] and java[1] >= python[1]:
        return java
    elif c_sharp[1] >= java[1] and c_sharp[1] >= python[1]:
        return c_sharp
    else:
        return python


e1 = ("Edouard", "C#", "java", "python")
e2 = ("Salima", "python", "java")
e3 = ("Marco", "python", "C#")
etudiants = e1, e2, e3

print("Nombre d'etudiant maitrisant java:", java_mastery(etudiants))
most_mastered = language_mastery(etudiants)
print("Le language le mieux maitriser est:", most_mastered[0])
