from datetime import date
from Jogador import Jogador
from Participacao import Participacao
from Sessao import Sessao

class Mesa:
    contador: int = 0

    def __init__(self, nome: str):
        Mesa.contador += 1
        self.__id = Mesa.contador
        self.__nome = nome
        self.__jogadores: list[Jogador] = []
        self.__participacoes: list[Participacao] = []
        self.__sessoes: list[Sessao] = []

    def adicionar_jogador(self, jogador: Jogador) -> None:
        self.__jogadores.append(jogador)

    def listar_jogadores(self) -> list[Jogador]:
        return self.__jogadores

    def adicionar_participacao(self, participacao: Participacao) -> None:
        self.__participacoes.append(participacao)

    def listar_participacoes(self) -> list[Participacao]:
        return self.__participacoes

    def criar_sessao(self, data: date, descricao: str) -> Sessao:
        nova_sessao = Sessao(data, descricao)
        self.__sessoes.append(nova_sessao)
        return nova_sessao

    def listar_sessoes(self) -> list[Sessao]:
        return self.__sessoes

    def get_id(self) -> int:
        return self.__id

    def get_nome(self) -> str:
        return self.__nome