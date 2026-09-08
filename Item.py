class Item:
  contador = 0
  
  def __init__(self, nome:str,tipo:str):
    Item.contador += 1
    self.__id = Item.contador
    self.__nome = nome
    self.__tipo = tipo

  def get_id(self) -> int:
    return self.__id

  def get_nome(self) -> str:
    return self.__nome