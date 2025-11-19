from exercicios_06.models.curso import Curso


class Campus:
    def __init__(self, nome: str, localizacao: str):
        self.nome = nome
        self.localizacao = localizacao
        self.cursos = []
    
    @classmethod
    def create_from_input(cls):
        while True:
            nome = input("Nome do campus: ").strip()
            if not nome:
                print("Nome não pode ser vazio!")
                continue
            localizacao = input("Localização do campus: ").strip()
            if not localizacao:
                print("Localização não pode ser vazia!")
                continue
            return cls(nome, localizacao)

    def criar_curso(self):
        novo_curso = Curso.create_from_input()
        self.cursos.append(novo_curso)

    def ver_cursos(self):
        if not self.cursos:
            print("Nenhum curso cadastrado.")
            return
        for curso in self.cursos:
            curso.sumarizar_informacoes()
        print('-'*30)

    def atualizar_curso(self):
        if not self.cursos:
            print("Nenhum curso cadastrado.")
            return

        print("Cursos disponíveis:")
        for i, curso in enumerate(self.cursos, 1):
            print(f"{i}. {curso.nome}")

        while True:
            try:
                opt = int(input("Qual curso você deseja atualizar? ")) - 1
                if 0 <= opt < len(self.cursos):
                    print("O que deseja atualizar?")
                    print("1. Nome")
                    print("2. Duração")
                    print("3. Grau")
                    opcao = input("Escolha uma opção: ").strip()

                    if opcao == "1":
                        novo_nome = input("Novo nome: ").strip()
                        if not novo_nome:
                            print("Nome não pode ser vazio.")
                            continue
                        self.cursos[opt].nome = novo_nome
                        print("Nome atualizado com sucesso!")
                    elif opcao == "2":
                        try:
                            nova_duracao = int(input("Nova duração (em anos): ").strip())
                            if nova_duracao <= 0:
                                print("Duração deve ser um número positivo.")
                                continue
                            self.cursos[opt].duracao = nova_duracao
                            print("Duração atualizada com sucesso!")
                        except ValueError:
                            print("Por favor, insira um número válido para a duração.")
                            continue
                    elif opcao == "3":
                        print("""Qual o grau do curso?
                        1. Bacharel
                        2. Licenciatura
                        3. Tecnólogo""")
                        while True:
                            escolha = input("Digite o número da opção: ").strip()
                            if escolha == "1":
                                novo_grau = "Bacharel"
                                break
                            elif escolha == "2":
                                novo_grau = "Licenciatura"
                                break
                            elif escolha == "3":
                                novo_grau = "Tecnologo"
                                break
                            else:
                                print("Opção inválida. Tente novamente.")
                        self.cursos[opt].grau = novo_grau
                        print("Grau atualizado com sucesso!")
                    else:
                        print("Opção inválida!")
                        continue
                    break
                else:
                    print("Índice de curso inválido!")
            except ValueError:
                print("Por favor, insira um número válido!")

    def remover_curso(self):
        if not self.cursos:
            print("Nenhum curso cadastrado.")
            return
        print("Cursos do campus:")
        for i, curso in enumerate(self.cursos, 1):
            print(f"{i}. {curso.nome}")
        while True:
            try:
                opt = int(input("Qual curso você deseja remover? ").strip()) - 1
            except ValueError:
                print("Por favor, insira um número válido!")
                continue
            if 0 <= opt < len(self.cursos):
                print(f"O Curso '{self.cursos.pop(opt).nome}' foi removido com sucesso!")
                break
            else:
                print("Curso inválido, tente novamente!")
