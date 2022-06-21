def java_mastery(etudiants):
    java = 0
    for student in etudiants:
        for information in student:
            if information == "java":
                java += 1
    return java


# Dont like this code a little bit... but it works
# def language_mastery(etudiants):
#     java = ["Java", 0]
#     c_sharp = ["C#", 0]
#     python = ["Python", 0]
#     for student in etudiants:
#         for information in student:
#             if information == "java":
#                 java[1] += 1
#             elif information == "python":
#                 python[1] += 1
#             elif information == "C#":
#                 c_sharp[1] += 1
#     if java[1] >= c_sharp[1] and java[1] >= python[1]:
#         return java
#     elif c_sharp[1] >= java[1] and c_sharp[1] >= python[1]:
#         return c_sharp
#     else:
#         return python


# def best_mastery(etudiants):
#     skill_list = list()
#     for student in etudiants:
#         for element in student[1:]:
#             skill_list.append(element)
#     java = skill_list.count("java")
#     python = skill_list.count("python")
#     c_sharp = skill_list.count("C#")
#     if java > c_sharp and java > python:
#         return "Java"
#     elif c_sharp > java and c_sharp > python:
#         return "C#"
#     else:
#         return "Python"


def best_mastery_2(etudiants):
    dico_prog = {"python": 0, "java": 0, "C#": 0}
    for student in etudiants:
        for element in student:
            if element == "java":
                dico_prog["java"] += 1
            elif element == "python":
                dico_prog["python"] += 1
            elif element == "C#":
                dico_prog["C#"] += 1
    return max(dico_prog, key=dico_prog.get)


e1 = ("Edouard", "C#", "java", "python")
e2 = ("Salima", "python", "java", "java")
e3 = ("Marco", "python", "C#", "java")
etudiants = e1, e2, e3

print("Nombre d'etudiant maitrisant java:", java_mastery(etudiants))
# most_mastered = language_mastery(etudiants)
# best_mastered = best_mastery(etudiants)
best_mastered = best_mastery_2(etudiants)
print("Le language le mieux maitriser est:", best_mastered)
