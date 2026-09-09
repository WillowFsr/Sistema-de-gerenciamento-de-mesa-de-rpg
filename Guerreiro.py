from Personagem import Personagem

class Guerreiro( Personagem):
  def __init__(self, forca: int, nome:str, nivel: int, vida: int, mentor = None):
    self.__forca = forca
    super().__init__(nome, nivel, vida, mentor)

  def atacar(self):
    print(f"O guerreiro ataca e causa {self.__forca} de dano")
