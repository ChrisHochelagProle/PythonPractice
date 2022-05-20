'''''
Nom de l'algorithme : fiche_paye_employe
Constantes : impot_federal = 0.15 (réel), impot_provincial = 0.20 (réel), assurance_emploi = 0.025 (réel
             regime_rentes = 0.002 (réel)
Entrées : nb_heures_travaillees (réel), taux_horaire (réel)
Sortie : salaire_net (réel)

afficher "Entrez votre taux horaire et vos heures travaillees: "
lire taux_horaire, nb_heures_travaillees
salaire_brut <-- taux_horaire * nb_heures_travaillees
retenu_impot_federal <-- impot_federal * salaire_brut
retenu_impot_provincial <-- impot_provincial * salaire_brut
retenu_assurance_emploi <-- assurance_emploi * salaire_brut
retenu_regime_rentes <-- regime_rentes * salaire_brut

salaire_net <-- salaire_brut - retenu_regime_rentes - retenu_assurance_emploi - retenu_impot_provincial - retenu_impot_federal
afficher "Votre salaire net est de: ", salaire_net, "$"
afficher "Déduction d'impot provincial: ", retenu_impot_provincial, "$"
afficher "Déduction d'impot fédéral: ", retenu_impot_provincial, "$"
afficher "Déduction d'assurance emploi: ", retenu_assurance_emploi, "$"
afficher "Déduction du régime des rentes: ", retenu_regime_rentes, "$"

'''''

impot_federal = 0.15
impot_provincial = 0.20
assurance_emploi = 0.025
regime_rentes = 0.02

taux_horaire = float(input("Entrez votre taux horaire: "))
nb_heures_travaillees = float(input("Entrez vos heures travaillees: "))
salaire_brut = taux_horaire * nb_heures_travaillees
retenu_impot_federal = impot_federal * salaire_brut
retenu_impot_provincial = impot_provincial * salaire_brut
retenu_assurance_emploi = assurance_emploi * salaire_brut
retenu_regime_rentes = regime_rentes * salaire_brut

salaire_net = round((salaire_brut - retenu_regime_rentes - retenu_assurance_emploi - retenu_impot_provincial - retenu_impot_federal), 2)
print("Votre salaire brut est de: " + str(salaire_brut) + "$")
print("Votre salaire net est de: " + str(salaire_net) + "$")
print("Déduction d'impot provincial: " + str(retenu_impot_provincial) + "$")
print("Déduction d'impot fédéral: " + str(retenu_impot_federal) + "$")
print("Déduction d'assurance emploi: " + str(retenu_assurance_emploi) + "$")
print("Déduction du régime des rentes: " + str(retenu_regime_rentes) + "$")