def province_commence_n(dict_codes):
    list_provinces_n = []
    for key in dict_codes.keys():
        if key[0] == "N":
            list_provinces_n.append(dict_codes[key][0])
    return list_provinces_n

def province_atlantique(dict_codes):
    list_provinces_atlantique = []
    for pro_region in dict_codes.values():
        if pro_region[-1] == "Atlantique":
            list_provinces_atlantique.append(pro_region[0])
    return list_provinces_atlantique


codes_canada = {"NL": ("Terre-Neuve-et-Labrador", "Atlantique"),
                "PE": ("Île-du-Prince-Édouard", "Atlantique"),
                "NS": ("Nouvelle-Écosse", "Atlantique"),
                "NB": ("Nouveau-Brunswick", "Atlantique"),
                "QC": ("Québec", "Québec"),
                "ON": ("Ontario", "Ontario"),
                "MB": ("Manitoba", "Prairies"),
                "SK": ("Saskatchewan", "Prairies"),
                "AB": ("Alberta", "Prairies"),
                "BC": ("Colombie-Britannique", "Colombie-Britannique"),
                "YT": ("Yukon", "Territoires"),
                "NT": ("TerritoiresduNord-Ouest", "Territoires"),
                "NU": ("Nunavut", "Territoires")
                }

print("Provinces donc le code commence par N:", province_commence_n(codes_canada))
print("\nProvinces atlantiques:", province_atlantique(codes_canada))