from datetime import date

class Sessao:
  contador = 0

  def __init__(self,data: date, descricao:str ):
    Sessao.contador += 1
    self.__id = Sessao.contador
    self.__data = data
    self.__descricao = descricao