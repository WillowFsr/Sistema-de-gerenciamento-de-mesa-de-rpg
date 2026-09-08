from datetime import date
from Arqueiro import Arqueiro
from Guerreiro import Guerreiro
from Item import Item
from Jogador import Jogador
from Mago import Mago
from Mesa import Mesa
from Mestre import Mestre
from Participacao import Participacao


def main():
    espada = Item("Espada Longa", "Arma")
    pocao = Item("Poção de Cura", "Consumível")

    guerreiro = Guerreiro(forca=18, nome="Thorin", nivel=10, vida=100)
    mago = Mago(
        inteligencia=20, nome="Gandalf", nivel=2, vida=40, mentor=guerreiro
    )
    arqueiro = Arqueiro(precisao=95.5, nome="Legolas", nivel=5, vida=60)

    guerreiro.atacar()
    mago.atacar()
    arqueiro.atacar()

    arqueiro.definir_mentor(guerreiro)
    arqueiro.definir_mentor(arqueiro)

    guerreiro.adicionar_item(espada)
    guerreiro.adicionar_item(pocao)
    guerreiro.remover_item(espada.get_id())

    mago.receber_dano(25)
    mago.curar(10)
    mago.receber_dano(50)

    jogador = Jogador("Carlos")
    jogador.adicionar_personagem(guerreiro)
    jogador.adicionar_personagem(mago)
    jogador.buscar_personagem(guerreiro.get_id())

    mestre = Mestre("Eduardo")
    mestre.narrar("Bem-vindos à caverna!")

    mesa = Mesa("Campanha Principal")
    mesa.adicionar_jogador(jogador)

    participacao = Participacao(papel="Jogador", data_entrada=date.today())
    mesa.adicionar_participacao(participacao)
    mesa.criar_sessao(data=date.today(), descricao="Sessão 1")


if __name__ == "__main__":
    main()