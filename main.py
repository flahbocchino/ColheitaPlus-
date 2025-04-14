from utils import carregar_dados, salvar_dados

def menu():
    print("\n=== COLHEITA+ ===")
    print("1. Cadastrar Operador")
    print("2. Cadastrar Máquina")
    print("3. Registrar Colheita")
    print("4. Listar Colheitas")
    print("0. Sair")

def main():
    operadores = carregar_dados("operadores.json")
    maquinas = carregar_dados("maquinas.json")
    colheitas = carregar_dados("colheitas.json")

    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do operador: ")
            experiencia = input("Anos de experiência: ")
            tipo = input("Tipo de colheita (manual/mecanizada): ")
            operadores.append({
                "id": len(operadores) + 1,
                "nome": nome,
                "experiencia": experiencia,
                "tipo_colheita": tipo
            })
            print("Operador cadastrado com sucesso!")

        elif opcao == "2":
            modelo = input("Modelo da máquina: ")
            fabricante = input("Fabricante: ")
            ano = input("Ano: ")
            maquinas.append({
                "id": len(maquinas) + 1,
                "modelo": modelo,
                "fabricante": fabricante,
                "ano": ano
            })
            print("Máquina cadastrada com sucesso!")

        elif opcao == "3":
            id_operador = int(input("ID do operador: "))
            tipo = input("Tipo de colheita (manual/mecanizada): ")
            id_maquina = int(input("ID da máquina (0 se não tiver): "))
            data = input("Data (dd/mm/aaaa): ")
            area = float(input("Área colhida (ha): "))
            quantidade = float(input("Quantidade colhida (t): "))
            perda = float(input("Perda estimada (%): "))
            colheitas.append({
                "id": len(colheitas) + 1,
                "id_operador": id_operador,
                "id_maquina": id_maquina if id_maquina != 0 else None,
                "tipo_colheita": tipo,
                "data": data,
                "area_colhida": area,
                "quantidade_colhida": quantidade,
                "perda_estimada": perda
            })
            print("Colheita registrada com sucesso!")

        elif opcao == "4":
            print("\n=== COLHEITAS REGISTRADAS ===")
            for c in colheitas:
                print(f"ID: {c['id']} | Operador: {c['id_operador']} | Máquina: {c['id_maquina']} |

