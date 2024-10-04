
import random

# Definindo a estrutura de dados para os compartimentos de leite
def entrada_dados(num_caminhoes, num_compartimentos):
    dados_caminhoes = []
    
    for i in range(num_caminhoes):
        caminhão = {}
        caminhão['id'] = i + 1
        compartimentos = []
        
        for j in range(num_compartimentos):
            compartimento = {
                'compartimento_id': j + 1,
                'volume': round(random.uniform(500, 2000), 2),  # Volume de leite em litros (simulado entre 500L a 2000L)
                'temperatura': round(random.uniform(2, 8), 2),  # Temperatura do leite em °C (simulação entre 2°C a 8°C)
                'qualidade': random.choice(['Alta', 'Média', 'Baixa'])  # Qualidade do leite
            }
            compartimentos.append(compartimento)
        
        caminhão['compartimentos'] = compartimentos
        dados_caminhoes.append(caminhão)
    
    return dados_caminhoes

# Exemplo de uso
num_caminhoes = 3  # Número de caminhões
num_compartimentos = 4  # Número de compartimentos por caminhão

dados = entrada_dados(num_caminhoes, num_compartimentos)

# Exibindo os dados simulados
for caminhao in dados:
    print(f"Caminhão {caminhao['id']}:")
    for compartimento in caminhao['compartimentos']:
        print(f"  Compartimento {compartimento['compartimento_id']}:")
        print(f"    Volume: {compartimento['volume']}L")
        print(f"    Temperatura: {compartimento['temperatura']}°C")
        print(f"    Qualidade: {compartimento['qualidade']}")

        from datetime import datetime

# Simulando um banco de dados de motoristas (para fins de autenticação)
motoristas_autenticados = {
    "motorista1": "senha123",
    "motorista2": "senha456"
}

# Função para autenticar o motorista
def autenticar_motorista(usuario, senha):
    if usuario in motoristas_autenticados and motoristas_autenticados[usuario] == senha:
        print("Autenticação bem-sucedida.")
        return True
    else:
        print("Autenticação falhou. Verifique suas credenciais.")
        return False

# Função para registrar a chegada do caminhão
def registrar_chegada(usuario, id_caminhao, quantidade_leite):
    hora_chegada = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    registro = {
        'motorista': usuario,
        'id_caminhao': id_caminhao,
        'quantidade_leite': quantidade_leite,
        'hora_chegada': hora_chegada
    }
    
    print(f"Chegada registrada para o caminhão {id_caminhao} com {quantidade_leite}L de leite.")
    print(f"Hora de chegada: {hora_chegada}")
    
    # Retorna o registro para ser armazenado ou manipulado posteriormente
    return registro

# Exemplo de fluxo
def sistema_controle():
    # Autenticação
    usuario = input("Digite seu nome de usuário: ")
    senha = input("Digite sua senha: ")

    if autenticar_motorista(usuario, senha):
        # Registro de chegada
        id_caminhao = input("Digite o ID do caminhão: ")
        quantidade_leite = float(input("Digite a quantidade de leite (em litros): "))
        
        # Registrar e armazenar os dados
        registro = registrar_chegada(usuario, id_caminhao, quantidade_leite)
        
        # Aqui você pode armazenar os dados em um banco de dados ou arquivo, por exemplo.
        # Vamos apenas simular o armazenamento em uma lista por enquanto.
        armazenados = []
        armazenados.append(registro)
        
        print("Registro de chegada concluído com sucesso!")
    else:
        print("Autenticação falhou. Operação cancelada.")

# Chamar o sistema para simular o fluxo
sistema_controle()

