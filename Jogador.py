from Personagem import Personagem

class Jogador:
  
  contador: int = 0
  
  def __init__(self, nome):
    Jogador.contador +=1
    self.__id = Jogador.contador
    self.__nome = nome
    self.__lista_de_personagens: list[Personagem] = []
  
  def adicionar_personagem(self, personagem:Personagem) -> None:
    self.__lista_de_personagens.append(personagem)
  
  def buscar_personagem(self,id_busca: int) -> Personagem:
    for personagem in self.__lista_de_personagens:
      if(personagem.get_id() == id_busca):
        return personagem
    print(f"personagem não foi encontrado")
  
  def listar_personagem (self) -> list[Personagem]:
    return self.__lista_de_personagens

  def remover_personagem (self,id_busca: int) -> bool:
    for personagem in self.__lista_de_personagens:
      if(personagem.get_id() == id_busca):
        self.__lista_de_personagens.remove(personagem)
        print(f"Personagem {personagem.get_nome()} foi removido")
        return True
    print(f"Personagem não encontrado")
    return False