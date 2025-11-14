from exercicios_06.models.Campus import Campus
from exercicios_06.models.Curso import Curso

if __name__ == '__main__':
    todos_campus = []

    campus_itapaje = Campus(nome="UFC Itapajé", localizacao="Itapajé, CE")
    campus_itapaje.cursos.extend([
        Curso("Ciência de Dados", 3, "Tecnologo"),
        Curso("Analise e Desenvolvimento de Sistemas", 3, "Tecnologo"),
        Curso("Segurança da Informação", 3, "Tecnologo"),
    ])
    todos_campus.append(campus_itapaje)

    campus_quixada = Campus(nome="UFC Quixadá", localizacao="Quixadá, CE")
    campus_quixada.cursos.extend([
        Curso("Ciência da Computação", 4, "Bacharel"),
        Curso("Engenharia de Software", 4, "Bacharel"),
        Curso("Sistemas de Informação", 4, "Bacharel"),
        Curso("Design Digital", 4, "Bacharel"),
    ])
    todos_campus.append(campus_quixada)
    

    while True:
        print("""
Sistema UFC
1. Ver todos os campus
2. Ver todos os cursos
0. Sair""")
        opt = input("Escolha uma opção: ").strip()
        if opt == "1":
            if not todos_campus:
                print("Nenhum campus cadastrado.")
                todos_campus = todos_campus
            while True:
                print("Campus cadastrados:")
                for i, campus in enumerate(todos_campus, start=1):
                    print(f"{i}. {campus.nome} - {campus.localizacao}")
                print(f"{len(todos_campus) + 1}. Cadastrar novo campus")
                print("0. Voltar")


                escolha = input("Escolha um campus pelo número, ou cadastre um novo (0 para voltar): ").strip()
                try:
                    idx = int(escolha)
                except ValueError:
                    print("Por favor, digite um número válido.")
                    continue

                if idx == 0:
                    break
                if 1 <= idx <= len(todos_campus):
                    campus_sel = todos_campus[idx - 1]
                    while True:
                        print(f"""
Gerenciar {campus_sel.nome}
1. Adicionar curso
2. Remover curso
3. Atualizar curso
4. Listar cursos
0. Voltar
                """)
                        sub = input("Escolha uma opção: ").strip()
                        if sub == "1":
                            campus_sel.criar_curso()
                        elif sub == "2":
                            campus_sel.remover_curso()
                        elif sub == "3":
                            campus_sel.atualizar_curso()
                        elif sub == "4":
                            campus_sel.ver_cursos()
                        elif sub == "0":
                            break
                        else:
                            print("Opção inválida.")
                    continue
                elif idx == len(todos_campus) + 1:
                    try:
                        novo_campus = Campus.create_from_input()
                        todos_campus.append(novo_campus)
                        print(f"Campus '{novo_campus.nome}' cadastrado com sucesso!")
                    except Exception as e:
                        print(f"Falha ao cadastrar campus: {e}")
                    continue
                else:
                    print("Opção inválida. Tente novamente.")
        elif opt == "2":
            nomes = set()
            for campus in todos_campus:
                for curso in campus.cursos:
                    if curso and getattr(curso, "nome", None):
                        nomes.add(curso.nome)
            if not nomes:
                print("Nenhum curso disponível.")
            else:
                print("Cursos disponíveis em todos os campus:")
                for nome in sorted(nomes):
                    print(f"- {nome}")
        elif opt == "0":
            break
        else:
            print('Opção inválida.')
