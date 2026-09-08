# 🎲 Sistema de Gerenciamento de Mesa de RPG

Sistema em Python desenvolvido utilizando os princípios de **Programação Orientada a Objetos (POO)** e boas práticas de modelagem UML. O projeto simula a gestão completa de uma mesa de RPG, abrangendo criação de personagens, controle de inventário, combate e sessões de jogo.

---

## 🚀 Funcionalidades

- **Gerenciamento de Personagens:** Suporte às classes `Guerreiro`, `Mago` e `Arqueiro` herdeiras de `Personagem`.
- **Mecanismos de Combate:** Sistema de dano, cura e ataques polimórficos via interface `Atacante`.
- **Inventário:** Adição e remoção de itens equipáveis (`Item`).
- **Gestão de Sessões & Mesa:** Criação de mesas (`Mesa`), registro de partidas (`Sessao`) e controle de papéis (`Participacao`).
- **Narrativa:** Classe `Mestre` para condução e envio de mensagens durante o jogo.

---

## 🛠️ Arquitetura e Padrões de Projeto

- **Encapsulamento:** Uso estrito de atributos privados (`__atributo`).
- **Abstração e Herança:** Classe abstrata `Personagem` herdando da interface `Atacante` via módulo `abc`.
- **Polimorfismo:** Sobrescrita dos métodos de ataque específicos para cada subclasse.
- **Associação e Agregação:** Vínculos entre `Jogador`, `Personagem`, `Mesa` e `Participacao`.

---

## 📂 Estrutura do Projeto

```text
.
├── Arqueiro.py      # Subclasse de Personagem
├── Atacante.py     # Interface abstrata para ações de ataque
├── Guerreiro.py    # Subclasse de Personagem
├── Item.py         # Representação de itens do jogo
├── Jogador.py      # Gestão de jogadores e seus personagens
├── Mago.py         # Subclasse de Personagem
├── Mesa.py         # Gerenciamento global das sessões e jogadores
├── Mestre.py       # Controle da narrativa do jogo
├── Participacao.py # Classe de associação entre Jogador e Mesa
├── Personagem.py   # Classe base abstrata para os heróis
├── Sessao.py       # Registro de sessões de jogo
└── main.py         # Script principal de testes da aplicação
