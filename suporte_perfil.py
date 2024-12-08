from datetime import datetime

# Classes e estruturas do sistema
class ConfiguracaoPrivacidade:
    def __init__(self, exibir_data_nascimento=True, exibir_foto=True):
        self.exibir_data_nascimento = exibir_data_nascimento
        self.exibir_foto = exibir_foto


class Usuario:
    def __init__(self, id, nome, data_nascimento, email, cpf, idioma_preferido, foto_perfil):
        self.id = id
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.email = email
        self.cpf = cpf
        self.idioma_preferido = idioma_preferido
        self.foto_perfil = foto_perfil
        self.idade = self.calcular_idade()
        self.config_privacidade = ConfiguracaoPrivacidade()

    def calcular_idade(self):
        data_nasc = datetime.strptime(self.data_nascimento, "%d/%m/%Y")
        hoje = datetime.now()
        idade = hoje.year - data_nasc.year
        if (hoje.month, hoje.day) < (data_nasc.month, data_nasc.day):
            idade -= 1
        return idade

    def editar_perfil(self):
        print("\n--- Editar Perfil ---")
        self.nome = input("Digite o novo nome: ")
        self.email = input("Digite o novo e-mail: ")
        self.foto_perfil = input("Digite o novo caminho da foto do perfil: ")

    def validar_idade(self):
        if self.idade < 18:
            print("Conteúdo restrito: O usuário não tem idade suficiente.")
        else:
            print("Conteúdo liberado.")

    def exibir_informacao(self):
        print("\n--- Informações do Usuário ---")
        print(f"Nome: {self.nome}")
        print(f"Email: {self.email}")
        print(f"Idade: {self.idade}")

    def configurar_privacidade(self):
        print("\n--- Configurar Privacidade ---")
        exibir_data = input("Deseja exibir a data de nascimento? (S/N): ").strip().lower() == "s"
        exibir_foto = input("Deseja exibir a foto do perfil? (S/N): ").strip().lower() == "s"
        self.config_privacidade.exibir_data_nascimento = exibir_data
        self.config_privacidade.exibir_foto = exibir_foto


class Conteudo:
    def __init__(self, titulo, descricao, faixa_etaria_minima):
        self.titulo = titulo
        self.descricao = descricao
        self.faixa_etaria_minima = faixa_etaria_minima

    def exibir(self, usuario):
        print("\n--- Exibir Conteúdo ---")
        if usuario.idade >= self.faixa_etaria_minima:
            print(f"Conteúdo: {self.titulo}")
            print(f"Descrição: {self.descricao}")
        else:
            print("Este conteúdo não está disponível para sua faixa etária.")


class Notificacao:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    def enviar(self):
        print(f"Enviando notificação para {self.nome}: {self.email}")


class Tutorial:
    def __init__(self, nome, descricao):
        self.nome = nome
        self.descricao = descricao

    def iniciar(self):
        print(f"\nIniciando tutorial: {self.nome}")
        print(f"Descrição: {self.descricao}")


class IA_AssistenteVirtual:
    def __init__(self, nome):
        self.nome = nome

    def oferecer_ajuda(self):
        print(f"Assistente Virtual ({self.nome}) oferecendo ajuda...")


# Função principal com interação
def main():
    print("Bem-vindo à plataforma!")
    nome = input("Digite seu nome completo: ")
    data_nascimento = input("Digite sua data de nascimento (DD/MM/AAAA): ")
    email = input("Digite seu e-mail: ")
    cpf = input("Digite seu CPF: ")
    idioma = input("Digite seu idioma preferido: ")
    foto_perfil = input("Digite o caminho da sua foto de perfil: ")

    usuario = Usuario(
        id="001",
        nome=nome,
        data_nascimento=data_nascimento,
        email=email,
        cpf=cpf,
        idioma_preferido=idioma,
        foto_perfil=foto_perfil
    )

    while True:
        print("\n--- Menu Principal ---")
        print("1. Exibir Informações do Usuário")
        print("2. Editar Perfil")
        print("3. Configurar Privacidade")
        print("4. Verificar Idade para Conteúdo")
        print("5. Exibir Conteúdo")
        print("6. Enviar Notificação")
        print("7. Iniciar Tutorial")
        print("8. Usar Assistente Virtual")
        print("9. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            usuario.exibir_informacao()
        elif opcao == "2":
            usuario.editar_perfil()
        elif opcao == "3":
            usuario.configurar_privacidade()
        elif opcao == "4":
            usuario.validar_idade()
        elif opcao == "5":
            conteudo = Conteudo(
                titulo="Curso de Matemática",
                descricao="Curso completo de Matemática para iniciantes",
                faixa_etaria_minima=18
            )
            conteudo.exibir(usuario)
        elif opcao == "6":
            notificacao = Notificacao(nome, email)
            notificacao.enviar()
        elif opcao == "7":
            tutorial = Tutorial(
                nome="Tutorial de Boas-vindas",
                descricao="Aprenda como usar a plataforma de forma eficiente"
            )
            tutorial.iniciar()
        elif opcao == "8":
            assistente = IA_AssistenteVirtual("Assistente Virtual")
            assistente.oferecer_ajuda()
        elif opcao == "9":
            print("Saindo do sistema. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()



