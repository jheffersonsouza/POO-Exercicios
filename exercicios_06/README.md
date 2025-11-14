# Sistema UFC (POO) — Campus e Cursos

Este exercício demonstra conceitos básicos de Programação Orientada a Objetos (POO) por meio de um pequeno sistema para gerenciar campi e cursos da UFC via terminal.

No menu interativo, é possível:
- Listar campus cadastrados e selecionar um para gerenciar.
- Cadastrar um novo campus.
- Dentro de um campus: adicionar, remover, atualizar e listar cursos.
- Listar todos os cursos disponíveis (agregados) em todos os campus.

---

## Estrutura de Arquivos

O módulo é composto por três arquivos principais:

### 1. `sistema_ufc.py`
Arquivo executável com o menu principal. Onde a lógica principal está contida.

### 2. `models/Campus.py`
Define a classe `Campus` com:
- Atributos: `nome`, `localizacao`, `cursos`.
- Métodos principais: `create_from_input()`, `criar_curso()`, `ver_cursos()`, `atualizar_curso()`, `remover_curso()`.

### 3. `models/Curso.py`
Define a classe `Curso` com atributos `nome`, `duracao`, `grau`, além de:
- `sumarizar_informacoes()`: imprime um resumo legível do curso.

---

## Como Executar

Recomendado executar como módulo (para que os imports de pacote funcionem corretamente):

1. Com o terminal aberto na raiz do repositório, rode:
   
   python -m exercicios_06.sistema_ufc

2. Siga as instruções do menu no terminal.

Observações:
- Se preferir executar diretamente o arquivo `sistema_ufc.py`, é necessário garantir que a raiz do projeto esteja no `PYTHONPATH` e que os imports de pacote sejam resolvidos. A forma via `-m` é a mais simples e portátil.
- Se estiver utiliza uma IDE de verdade o processo é até mais simples, no PyCharm é so clicar em um botão.