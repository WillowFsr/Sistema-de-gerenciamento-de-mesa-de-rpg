from Personagem import Personagem

class Arqueiro( Personagem):
  def __init__(self,precisao: float, nome:str, nivel: int, vida: int,mentor:"Personagem" |  None= None):
    self.__precisao = precisao
    super().__init__(nome, nivel, vida, mentor)

  def atacar(self):
     print(f"O arqueiro ataca com {self.__precisao} de precisao")