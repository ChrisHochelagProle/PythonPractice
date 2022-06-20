def force_faiblesse(personnage):
    forces = ()
    faiblesses = ()
    for skill in personnage:
        active_skill_score = skill[-1]
        if int(active_skill_score) < 15:
            faiblesses += skill
        else:
            forces += skill

    return forces, faiblesses


gundrick = (("Force", 11), ("Dexterite", 13), ("Constitution", 14),
            ("Intelligence", 16), ("Sagesse", 11), ("Charisme", 11))

print("Les forces:", force_faiblesse(gundrick)[-2], "\nLes faiblesses:", force_faiblesse(gundrick)[-1])
