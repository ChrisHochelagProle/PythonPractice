# def admissions(dict_etudiants):
#     dict_admis = {}
#     dict_non_admis = {}
#     for etudiant in dict_etudiants:
#         if dict_etudiants[etudiant] >= 10:
#             dict_admis[etudiant] = dict_etudiants[etudiant]
#         else:
#             dict_non_admis[etudiant] = dict_etudiants[etudiant]
#     return dict_admis, dict_non_admis

# def admissions_key_value(dict_etudiants):
#     dict_admis = {}
#     dict_non_admis = {}
#     for key, value in dict_etudiants.items():
#         if value >= 10:
#             dict_admis[key] = value
#         else:
#             dict_non_admis[key] = value
#     return dict_admis, dict_non_admis

def admissions_student_note(dict_etudiants):
    dict_admis = {}
    dict_non_admis = {}
    for etudiant, note in dict_etudiants.items():
        if note >= 10:
            dict_admis[etudiant] = note
        else:
            dict_non_admis[etudiant] = note
    return dict_admis, dict_non_admis

etudiants = {"etudiant_1": 13, "etudiant_2": 17, "etudiant_3": 2, "etudiant_4": 17, "etudiant_5": 13,
             "etudiant_6": 17, "etudiant_7": 5, "etudiant_8": 17, "etudiant_9": 8, "etudiant_10": 17,
             "etudiant_11": 9, "etudiant_12": 17}

tuple_of_dict_admissions = admissions_student_note(etudiants)

print("Les eleves admis:", tuple_of_dict_admissions[0], "\n")
print("Les eleces non admis:", tuple_of_dict_admissions[1])
