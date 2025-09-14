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


