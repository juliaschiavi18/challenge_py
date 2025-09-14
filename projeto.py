# Projeto: Central de Notícias - Futebol Feminino
# Integrantes: Julia Schiavi, Leonardo Grosskopf, Thayna Lopes, Sofia Bomeny

# dicionário que guarda as notícias e contador de ID
noticias = {}
id_atual = 1

# função para cadastrar notícia
def cadastrar():
    global id_atual
    noticia = {
        "titulo": input("Título: "),
        "resumo": input("Resumo: "),
        "categoria": input("Categoria (clube/campeonato/jogadora): ")
    }
    noticias[id_atual] = noticia
    print(f"✅ Notícia cadastrada com ID {id_atual}!\n")
    id_atual += 1

# função  pra mostrar notícias de um dicionário filtrado
def mostrar_noticias(lista_noticias):
    if not lista_noticias:
        print("⚠ Nenhuma notícia encontrada.\n")
        return
    for id_, dados in lista_noticias.items():
        print(f"ID: {id_} | {dados['categoria'].upper()}")
        print(f"Título: {dados['titulo']}")
        print(f"Resumo: {dados['resumo']}\n")

# listar todas as notícias
def listar():
    print("\n=== Todas as Notícias ===")
    mostrar_noticias(noticias)

# filtrar notícias por categoria
def filtrar():
    cat = input("Digite a categoria (clube/campeonato/jogadora): ").lower()
    filtradas = {id_: d for id_, d in noticias.items() if d["categoria"].lower() == cat}
    print(f"\n=== Notícias da categoria {cat.upper()} ===")
    mostrar_noticias(filtradas)

# buscar notícias por palavra no título ou resumo
def buscar():
    termo = input("Digite uma palavra para buscar: ").lower()
    encontradas = {id_: d for id_, d in noticias.items() 
                   if termo in d["titulo"].lower() or termo in d["resumo"].lower()}
    print(f"\n=== Resultados da busca por: {termo} ===")
    mostrar_noticias(encontradas)

# remover notícia por ID
def remover():
    try:
        id_remove = int(input("Digite o ID da notícia que deseja remover: "))
        if noticias.pop(id_remove, None):
            print("🗑 Notícia removida!\n")
        else:
            print("⚠ ID não encontrado.\n")
    except ValueError:
        print("⚠ Digite um número válido.\n")

# mostra o menu principal
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

# loop principal do menu
def menu():
    while True:
        mostrar_menu()
        opc = input("👉 Escolha uma opção: ")
        if not opc.isdigit():
            print("⚠ Digite apenas números!\n")
            continue
        opc = int(opc)

#utilizando match case para as opções, para melhor organização em vez de varios if-elif-else
        match opc:
            case 1: cadastrar()
            case 2: listar()
            case 3: filtrar()
            case 4: buscar()
            case 5: remover()
            case 0: 
                print("👋 Saindo... até a próxima!")
                break
            case _: print("⚠ Opção inválida. Escolha entre 0 e 5.\n")

if __name__ == "__main__":
    menu()
