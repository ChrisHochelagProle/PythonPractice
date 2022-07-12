class ClassGenerator:
    def __init__(self, uml: str):
        self.uml_diagram = uml

    def generateClass(self):
        nom_de_classe = ""
        list_attributs = []
        list_methodes = []
        lines_in_uml = self.uml_diagram.split("\n")
        compteur_separations = 0
        for line in lines_in_uml:
            if "*" in line:
                compteur_separations += 1
                continue
            if compteur_separations == 1:
                line.strip(' ')
                line.strip('|')
                nom_de_classe = line
            elif compteur_separations == 2:
                line.strip('|')
                new_string = line[1:]
                isnotspace = lambda char: char != " "
                for char in new_string[-1:-len(line)]:
                    if isnotspace(char):
                        break
                    else:
                        new_string = new_string[0:len(new_string) - 2]
                list_attributs.append(new_string)
            elif compteur_separations == 3:
                line.strip('|')
                new_string = line[1:]
                isnotspace = lambda char: char != " "
                for char in new_string[-1:-len(line)]:
                    if isnotspace(char):
                        break
                    else:
                        new_string = new_string[0:len(new_string)-2]
                list_methodes.append(new_string)
            else:
                break
        infos = f'Nom: {nom_de_classe}\n' \
                f'Attributs: {list_attributs}\n' \
                f'Methodes: {list_attributs}'
        return infos


uml = f'| ************** |\n' \
      f'| Ville          |\n' \
      f'| ************** |\n' \
      f'| - nom: str     |\n' \
      f'| - pays: Pays   |\n' \
      f'| - pop: int     |\n' \
      f'| ************** |\n' \
      f'| + infos(): str |\n' \
      f'| ************** |\n'

# generator = ClassGenerator(uml)
# print(generator.generateClass())

# lines_in_uml = uml.split("\n")
# print(lines_in_uml)
# lines_without_bars = []
# for line in lines_in_uml:
#     lines_without_bars.append(line.strip("|"))
# print(lines_without_bars)
# for line in lines_without_bars:
#     for char in range(len(line)):