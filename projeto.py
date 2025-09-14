# Projeto: Central de Notícias - Futebol Feminino
# Integrantes: Julia Schiavi, Leonardo Grosskof, Thayna Lopes, Sofia Bomeny

# dicionário para guardar todas as notícias
noticias = {}   
# contador de ID para cada notícia cadastrada
id_atual = 1    

# cadastrar uma notícia nova
def cadastrar():
    global id_atual
    titulo = input("Título: ")  
    resumo = input("Resumo: ") 
    categoria = input("Categoria (clube/campeonato/jogadora): ")
    # salva a notícia no dicionário com o ID atual
    noticias[id_atual] = {
        "titulo": titulo,
        "resumo": resumo,
        "categoria": categoria
    }
    print(f"✅ Notícia cadastrada com ID {id_atual}!\n")
    id_atual += 1  # aumenta o ID pro próximo cadastro

#  listar todas as notícias
def listar():
    if not noticias:
        print("⚠ Nenhuma notícia cadastrada.\n")
    else:
        print("\n=== Todas as Notícias ===")
        for id_, dados in noticias.items():
            print(f"ID: {id_} | {dados['categoria'].upper()}")
            print(f"Título: {dados['titulo']}")
            print(f"Resumo: {dados['resumo']}\n")

# filtrar notícias por categoria
def filtrar():
    cat = input("Digite a categoria (clube/campeonato/jogadora): ")
    achou = False
    print(f"\n=== Notícias da categoria {cat.upper()} ===")
    for id_, dados in noticias.items():
        if dados["categoria"].lower() == cat.lower():  # compara ignorando maiúsculas
            print(f"ID: {id_} | {dados['categoria'].upper()}")
            print(f"Título: {dados['titulo']}")
            print(f"Resumo: {dados['resumo']}\n")
            achou = True
    if not achou:
        print("⚠ Nenhuma notícia encontrada nessa categoria.\n")

# buscar notícias por uma palavra no título ou resumo
def buscar():
    termo = input("Digite uma palavra para buscar: ").lower()
    achou = False
    print(f"\n=== Resultados da busca por: {termo} ===")
    for id_, dados in noticias.items():
        if termo in dados["titulo"].lower() or termo in dados["resumo"].lower():
            print(f"ID: {id_} | {dados['categoria'].upper()}")
            print(f"Título: {dados['titulo']}")
            print(f"Resumo: {dados['resumo']}\n")
            achou = True
    if not achou:
        print("⚠ Nenhuma notícia encontrada.\n")

# remover uma notícia pelo ID
def remover():
    try:
        id_remove = int(input("Digite o ID da notícia que deseja remover: "))
        if id_remove in noticias:
            del noticias[id_remove]
            print("🗑 Notícia removida!\n")
        else:
            print("⚠ ID não encontrado.\n")
    except ValueError:
        print("⚠ Digite um número válido.\n")

#  menu principal
def mostrar_menu():
    print("\n" + "=" * 45)
    print(" 📢 Central de Notícias - Futebol Feminino ")
    print("=" * 45)
    print("1️⃣  Cadastrar notícia")
    print("2️⃣  Listar todas as notícias")
    print("3️⃣  Filtrar por categoria")
    print("4️⃣  Buscar por palavra")
    print("5️⃣  Remover notícia")
    print("0️⃣  Sair")
    print("=" * 45)

# principal função que controla o menu e as opções
def menu():
    while True:
        mostrar_menu()
        opc = input("👉 Escolha uma opção: ")

        if not opc.isdigit():  # apenas números sejam digitados
            print("⚠ Digite apenas números!\n")
            continue

        opc = int(opc)

        if opc == 1:
            cadastrar()
        elif opc == 2:
            listar()
        elif opc == 3:
            filtrar()
        elif opc == 4:
            buscar()
        elif opc == 5:
            remover()
        elif opc == 0:
            print("👋 Saindo... até a próxima!")
            break
        else:
            print("⚠ Opção inválida. Escolha entre 0 e 5.\n")

# executa o menu só se o arquivo for rodado diretamente
if __name__ == "__main__":
    menu()
