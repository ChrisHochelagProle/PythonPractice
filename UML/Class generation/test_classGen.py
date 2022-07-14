from ClassMethod import *
from ClassAttribut import *
from ClassGenUtils import *

uml = f'| ************** |\n' \
      f'| Ville          |\n' \
      f'| ************** |\n' \
      f'| - nom: str     |\n' \
      f'| - pays: Pays   |\n' \
      f'| - pop: int     |\n' \
      f'| ************** |\n' \
      f'| + infos(): str |\n' \
      f'| + afficher()   |\n' \
      f'| ************** |\n'

generator = ClassGenerator(uml)
print(generator.generateClass())
