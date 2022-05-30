# Définissez votre fonction ici

def formatCourriel(string):
    liste_courriel = string.split(',')
    return liste_courriel[1].lower() + "." + liste_courriel[0].lower() + "@" + liste_courriel[2].lower()


# Ne modifiez pas cette partie!

s1 = "BEN-SAAD,Asma,cmaisonneuve.qc.ca"

s2 = "TAOUFIKI,Manal,hotmail.com"

s3 = "TARDIF,Olivier,gmail.com"

c1 = formatCourriel(s1)

c2 = formatCourriel(s2)

c3 = formatCourriel(s3)

print(c1)

print(c2)

print(c3)