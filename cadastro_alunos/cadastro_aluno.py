# Projeto Prático: Sistema de Cadastro de Alunos
# Descrição: Sistema que gerencia o cadastro de alunos utilizando uma classe Aluno
# Os Alunos serão armazenados em uma lista para manipulação, como adição, visualização e busca.

class Aluno:
    def __init__(self, nome, idade, matricula):
        self.nome = nome
        self.idade = idade
        self.matricula = matricula

    def __str__(self):
        return f"Matricula: {self.matricula}, Nome: {self.nome}, Idade: {self.idade}"

class SistemaCadastro():
    def __init__(self):
        self.alunos = []

    def cadastrar_alunos(self):
        nome = input("Digite o nome do aluno: ")
        idade = input("Digite a idade do aluno: ")
        matricula = input("Digite o numero da matricula do aluno: ")

        aluno = Aluno(nome, idade, matricula)

        self.alunos.append(aluno)

        print(f"Aluno {nome} adicionado com sucesso!")

    def listar_alunos(self):
        if not self.alunos:
            print("Nenhum aluno encontrado...")
        else:
            print("=== Lista de Alunos ===")
            for aluno in self.alunos:
                print(aluno)

    def buscar_aluno(self):
        matricula = input("Digite a matricula do Aluno que deseja encontrar: ")

        for aluno in self.alunos:
            if aluno.matricula == matricula:
                print("=== Aluno encontrado ===")
                print(aluno)
                return
        print("Aluno não encontrado!")

    def remover_aluno(self):
        matricula = input("Digite a matricula do Aluno que deseja remover: ")

        for aluno in self.alunos:
            if aluno.matricula == matricula:
                self.alunos.remove(aluno)
                print(f"Aluno {aluno.nome} removido com sucesso!")
                return
        print("Aluno não encontrado!")

    def menu(self):
        while True:
            print("=== Menu Sistema de Cadastro ===")
            print("1. Cadastrar Aluno")
            print("2. Exibir Alunos")
            print("3. Buscar Alunos")
            print("4. Remover Aluno")
            print("5. Sair ")

            opcao = input("Selecione uma opção: ")

            if opcao == "1":
                self.cadastrar_alunos()
            elif opcao == "2":
                self.listar_alunos()
            elif opcao == "3":
                self.buscar_aluno()
            elif opcao == "4":
                self.remover_aluno()
            elif opcao == "5":
                print("Saindo do Sistema...")
                break
            else:
                print("Opção inválida. Selecione de 1 a 4.")

if __name__ == "__main__":
    sistema = SistemaCadastro()

    sistema.menu()
