from Personagem import Personagem

class Mago(Personagem):
  def __init__(self,inteligencia: int, nome:str, nivel: int, vida: int,mentor:"Personagem" |  None= None):
    self.__inteligencia = inteligencia
    super().__init__(nome, nivel, vida, mentor) 

  def atacar(self):
    print(f"O mago ataca com {self.__inteligencia} de inteligencia")