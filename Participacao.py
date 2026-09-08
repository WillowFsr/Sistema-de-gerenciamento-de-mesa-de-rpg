from datetime import date

class Participacao:
  def __init__(self, papel:str, data_entrada: date):
    self.__papel = papel
    self.__data_entrada = data_entrada
  
  def get_papel(self) -> str:
    return self.__papel
  
  def get_data_entrada(self)-> date:
    return self.__data_entrada