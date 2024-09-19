class Residuo:
    def __init__(self, tipo, quantidade):
        self.tipo = tipo  # Tipo de resíduo (orgânico, reciclável, não reciclável)
        self.quantidade = quantidade  # Quantidade em quilos

class GestaoResiduos:
    def __init__(self):
        self.residuos = []  # Lista para armazenar os resíduos coletados

    def adicionar_residuo(self, tipo, quantidade):
        residuo = Residuo(tipo, quantidade)
        self.residuos.append(residuo)
        print(f"{quantidade}kg de {tipo} adicionado.")

    def calcular_totais(self):
        totais = {
            'orgânico': 0,
            'reciclável': 0,
            'não reciclável': 0
        }
        for residuo in self.residuos:
            if residuo.tipo in totais:
                totais[residuo.tipo] += residuo.quantidade
        return totais

    def gerar_relatorio(self):
        totais = self.calcular_totais()
        print("\n--- Relatório de Resíduos ---")
        for tipo, quantidade in totais.items():
            print(f"Total de resíduos {tipo}: {quantidade}kg")
        print(f"Total geral de resíduos: {sum(totais.values())}kg")

    def mostrar_status(self):
        print("\n--- Status Atual da Gestão de Resíduos ---")
        if not self.residuos:
            print("Nenhum resíduo registrado ainda.")
        else:
            for i, residuo in enumerate(self.residuos, 1):
                print(f"{i}. Tipo: {residuo.tipo.capitalize()}, Quantidade: {residuo.quantidade}kg")
        self.gerar_relatorio()

def main():
    sistema = GestaoResiduos()
    
    while True:
        print("\nEscolha uma opção:")
        print("1. Adicionar resíduo")
        print("2. Mostrar status atual")
        print("3. Gerar relatório")
        print("4. Sair")
        
        escolha = input("Digite o número da opção desejada: ")
        
        if escolha == '1':
            tipo = input("Digite o tipo de resíduo (orgânico, reciclável, não reciclável): ").strip().lower()
            if tipo not in ['orgânico', 'reciclável', 'não reciclável']:
                print("Tipo de resíduo inválido. Tente novamente.")
                continue
            quantidade = float(input("Digite a quantidade em quilos: "))
            sistema.adicionar_residuo(tipo, quantidade)
        elif escolha == '2':
            sistema.mostrar_status()
        elif escolha == '3':
            sistema.gerar_relatorio()
        elif escolha == '4':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
