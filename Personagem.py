from Item import Item
from Atacante import Atacante

class Personagem( Atacante):
  contador = 0
  
  def __init__(self, nome:str, nivel: int, vida: int,mentor = None):
    Personagem.contador += 1
    self.__id = Personagem.contador
    self.__nome = nome
    self.__nivel = nivel
    self.__vida = vida  
    self.__inventario_de_itens:list[Item] = []
    self.__mentor = mentor
  
  def receber_dano(self, dano_recebido:int):
    if(self.__vida >0):
      self.__vida = max(0,self.__vida - dano_recebido)
      if(self.__vida >0):
        print(f"Voce recebeu {dano_recebido} de dano e possui atualmente {self.__vida} de vida")
      else:
        print(f"O dano foi fatal")

    else:
      print(f"Esse personagem já está morto")
  
  def curar(self, cura_recebida):
    self.__vida += cura_recebida
    print(f"O personagem possui atualmente: {self.__vida} e curou {cura_recebida}")

  def adicionar_item(self, item:Item):
    self.__inventario_de_itens.append(item)
  
  def remover_item(self, id_item: int) -> bool:
    for item in self.__inventario_de_itens:
      if(item.get_id() == id_item):
        self.__inventario_de_itens.remove(item)
        print(f"O item {item.get_nome()} foi removido do inventário")
        return True
    print(f"O item não foi encontrado no inventário")
    return False


  def listar_itens(self)-> list[Item]:
    return self.__inventario_de_itens

  def get_Mentor(self):
    return self.__Mentor

  def definir_mentor(self, mentor:Personagem):
    if(mentor == self):
      print(f"Um personagem não pode ser mentor dele mesmo")
    else:
      self.__Mentor = mentor

  def atacar(self):
    print(f"O persongem {self.__nome} ataca")

  def get_id(self) -> int:
    return self.__id

  def get_nome(self) -> str:
    return self.__nome