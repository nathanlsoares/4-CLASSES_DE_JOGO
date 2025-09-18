class Heroi:
    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo.lower()  # deixa o tipo em minúsculo para facilitar comparações

    def atacar(self):
        # Define os ataques conforme o tipo
        ataques = {
            "mago": "magia",
            "guerreiro": "espada",
            "monge": "artes marciais",
            "ninja": "shuriken"
        }

        # Verifica se o tipo está na tabela de ataques
        if self.tipo in ataques:
            ataque = ataques[self.tipo]
            print(f"O {self.tipo} atacou usando {ataque}")
        else:
            print(f"O {self.tipo} atacou, mas não sabemos qual arma foi usada.")


# Testando a classe:
heroi1 = Heroi("Merlin", 150, "Mago")
heroi2 = Heroi("Arthur", 30, "Guerreiro")
heroi3 = Heroi("Liu Kang", 40, "Monge")
heroi4 = Heroi("Hanzo", 28, "Ninja")

heroi1.atacar()  # O mago atacou usando magia
heroi2.atacar()  # O guerreiro atacou usando espada
heroi3.atacar()  # O monge atacou usando artes marciais
heroi4.atacar()  # O ninja atacou usando shuriken