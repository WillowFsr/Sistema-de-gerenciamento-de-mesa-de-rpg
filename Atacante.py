from abc import ABC, abstractclassmethod

class Atacante(ABC):
  
  @abstractclassmethod 
  def atacar(self):
    print(f"Isso ataca")