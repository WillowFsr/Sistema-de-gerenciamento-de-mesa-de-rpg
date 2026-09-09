class Mestre:
  contador = 0
  
  def __init__(self,nome: str):
    Mestre.contador +=1
    self.__id = Mestre.contador
    self.__nome = nome
  
  def narrar(self,mensagem:str)-> str:
    print(f"{mensagem}")

  

