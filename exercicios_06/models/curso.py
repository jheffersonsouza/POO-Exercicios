class Curso:
    def __init__(self, nome, duracao, grau):
        self.nome = nome
        self.duracao = duracao
        self.grau = grau

    @classmethod
    def create_from_input(cls):
        while True:
            nome = input("Digite o nome do curso: ").strip()
            if nome:
                break
            print("Nome inválido. Tente novamente.")
        while True:
            print("""Qual o grau do curso?
            1. Bacharel
            2. Licenciatura
            3. Tecnólogo""")
            opt = input("Digite o número da opção: ").strip()
            if opt == "1":
                grau = "Bacharel"
                duracao = 4
                break
            elif opt == "2":
                grau = "Licenciatura"
                duracao = 4
                break
            elif opt == "3":
                grau = "Tecnologo"
                duracao = 3
                break
            else:
                print("Opção inválida. Tente novamente.")

        return cls(nome, duracao, grau)

    def sumarizar_informacoes(self):
        print('-'*30)
        print(f"Nome: {self.nome}")
        print(f"Duração: {self.duracao}")
        print(f"Grau: {self.grau}")
