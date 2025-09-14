# Projeto: Central de Notícias - Futebol Feminino
# Integrantes: Julia Schiavi, Leonardo Grosskof, Thayna Lopes, Sofia Bomeny


noticias = []  
id_atual = 1   


def cadastrar():
    global id_atual
    titulo = input("Título: ")
    resumo = input("Resumo: ")
    categoria = input("Categoria (clube/campeonato/jogadora): ")
    noticia = {
        "id": id_atual,
        "titulo": titulo,
        "resumo": resumo,
        "categoria": categoria
    }
    noticias.append(noticia)
    id_atual += 1
    print("✅ Notícia cadastrada!\n")


def listar():
    if not noticias:
        print("⚠ Nenhuma notícia cadastrada.\n")
    else:
        print("\n=== Todas as Notícias ===")
        for n in noticias:
            print(f"ID: {n['id']} | {n['categoria'].upper()}")
            print(f"Título: {n['titulo']}")
            print(f"Resumo: {n['resumo']}\n")


def filtrar():
    cat = input("Digite a categoria (clube/campeonato/jogadora): ")
    achou = False
    print(f"\n=== Notícias da categoria {cat.upper()} ===")
    for n in noticias:
        if n["categoria"].lower() == cat.lower():
            print(f"ID: {n['id']} | {n['categoria'].upper()}")
            print(f"Título: {n['titulo']}")
            print(f"Resumo: {n['resumo']}\n")
            achou = True
    if not achou:
        print("⚠ Nenhuma notícia encontrada nessa categoria.\n")


def buscar():
    termo = input("Digite uma palavra para buscar: ").lower()
    achou = False
    print(f"\n=== Resultados da busca por: {termo} ===")
    for n in noticias:
        if termo in n["titulo"].lower() or termo in n["resumo"].lower():
            print(f"ID: {n['id']} | {n['categoria'].upper()}")
            print(f"Título: {n['titulo']}")
            print(f"Resumo: {n['resumo']}\n")
            achou = True
    if not achou:
        print("⚠ Nenhuma notícia encontrada.\n")


def remover():
    try:
        id_remove = int(input("Digite o ID da notícia que deseja remover: "))
        for n in noticias:
            if n["id"] == id_remove:
                noticias.remove(n)
                print("🗑 Notícia removida!\n")
                return
        print("⚠ ID não encontrado.\n")
    except ValueError:
        print("⚠ Digite um número válido.\n")


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


def menu():
    while True:
        mostrar_menu()
        opc = input("👉 Escolha uma opção: ")

        if not opc.isdigit():  # só aceita números
            print("⚠ Digite apenas números!\n")
            continue

        opc = int(opc)  # converte para inteiro

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


if __name__ == "__main__":
    menu()
