# Projeto: Central de Notícias - Futebol Feminino
# Integrantes: Julia Schiavi, Leonardo Grosskopf, Thayna Lopes, Sofia Bomeny

import json
import os

#CRIANDO ARQUIVO JSON
ARQUIVO = "noticias.json"


def salvar_dados(dados):
    #SALVAR OS DADOS NO ARQUIVO JSON
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)

def carregar_dados():
    #CARREGA OS DADOS DO ARQUIVO JSON
    if os.path.exists(ARQUIVO):
        try:
            with open(ARQUIVO, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            print("⚠ Erro ao carregar os dados. Um novo arquivo será criado.")
    
    # Se o arquivo não existir ou estiver corrompido, cria um novo
    dados_iniciais = {"noticias": {}, "id_atual": 1}
    salvar_dados(dados_iniciais)  
    return dados_iniciais

# inicio CRUD

def cadastrar():
    #cadastro de noticias
    dados = carregar_dados()
    try:
        titulo = input("Título: ").strip()
        resumo = input("Resumo: ").strip()
        categoria = input("Categoria (clube/campeonato/jogadora): ").strip().lower()

        if not titulo or not resumo or categoria not in ["clube", "campeonato", "jogadora"]:
            print("⚠ Dados inválidos! Verifique as entradas.\n")
            return

        noticia = {"titulo": titulo, "resumo": resumo, "categoria": categoria}
        dados["noticias"][str(dados["id_atual"])] = noticia
        print(f"✅ Notícia cadastrada com ID {dados['id_atual']}!\n")
        dados["id_atual"] += 1
        salvar_dados(dados)
    except Exception as e:
        print(f"⚠ Erro ao cadastrar notícia: {e}")

def mostrar_noticias(lista_noticias):
    #exibe as noticias formatadas
    if not lista_noticias:
        print("⚠ Nenhuma notícia encontrada.\n")
        return
    for id_, dados in lista_noticias.items():
        print(f"ID: {id_} | {dados['categoria'].upper()}")
        print(f"Título: {dados['titulo']}")
        print(f"Resumo: {dados['resumo']}\n")

def listar():
   #listas as noticias
    dados = carregar_dados()
    print("\n=== Todas as Notícias ===")
    mostrar_noticias(dados["noticias"])

def filtrar():
    #filtrar noticias por categoria
    dados = carregar_dados()
    cat = input("Digite a categoria (clube/campeonato/jogadora): ").lower()
    filtradas = {id_: d for id_, d in dados["noticias"].items() if d["categoria"] == cat}
    print(f"\n=== Notícias da categoria {cat.upper()} ===")
    mostrar_noticias(filtradas)

def buscar():
    #buscar noticias por palavra no titulo ou resumo
    dados = carregar_dados()
    termo = input("Digite uma palavra para buscar: ").lower()
    encontradas = {id_: d for id_, d in dados["noticias"].items() 
                   if termo in d["titulo"].lower() or termo in d["resumo"].lower()}
    print(f"\n=== Resultados da busca por: {termo} ===")
    mostrar_noticias(encontradas)

def remover():
    #remover uma noticia pelo id
    dados = carregar_dados()
    try:
        id_remove = input("Digite o ID da notícia que deseja remover: ").strip()
        if id_remove in dados["noticias"]:
            dados["noticias"].pop(id_remove)
            salvar_dados(dados)
            print("🗑 Notícia removida!\n")
        else:
            print("⚠ ID não encontrado.\n")
    except Exception as e:
        print(f"⚠ Erro ao remover: {e}")

def atualizar():
    #atualizar noticia pelo id
    dados = carregar_dados()
    try:
        id_update = input("Digite o ID da notícia que deseja atualizar: ").strip()
        if id_update not in dados["noticias"]:
            print("⚠ ID não encontrado.\n")
            return
        titulo = input("Novo título (deixe vazio para manter): ").strip()
        resumo = input("Novo resumo (deixe vazio para manter): ").strip()
        categoria = input("Nova categoria (clube/campeonato/jogadora ou deixe vazio): ").strip().lower()

        if titulo: dados["noticias"][id_update]["titulo"] = titulo
        if resumo: dados["noticias"][id_update]["resumo"] = resumo
        if categoria in ["clube", "campeonato", "jogadora"]:
            dados["noticias"][id_update]["categoria"] = categoria

        salvar_dados(dados)
        print("👍 Notícia atualizada com sucesso!\n")
    except Exception as e:
        print(f"⚠ Erro ao atualizar: {e}")



def mostrar_menu():
    """Menu principal."""
    print("\n" + "=" * 45)
    print(" 📢 Central de Notícias - Futebol Feminino ")
    print("=" * 45)
    print("1️⃣  Cadastrar notícia")
    print("2️⃣  Listar todas as notícias")
    print("3️⃣  Filtrar por categoria")
    print("4️⃣  Buscar por palavra")
    print("5️⃣  Remover notícia")
    print("6️⃣  Atualizar notícia")
    print("0️⃣  Sair")
    print("=" * 45)

def menu():
    #loop principal
    carregar_dados()  # Garante que o arquivo exista
    while True:
        mostrar_menu()
        opc = input("👉 Escolha uma opção: ")
        if not opc.isdigit():
            print("⚠ Digite apenas números!\n")
            continue
        opc = int(opc)

        match opc:
            case 1: cadastrar()
            case 2: listar()
            case 3: filtrar()
            case 4: buscar()
            case 5: remover()
            case 6: atualizar()
            case 0: 
                print("👋 Saindo... até a próxima!")
                break
            case _: print("⚠ Opção inválida. Escolha entre 0 e 6.\n")

if __name__ == "__main__":
    menu()
