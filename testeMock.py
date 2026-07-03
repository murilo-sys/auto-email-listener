from src.services.extrairDados import extrairDados


def testar_mock_html():
    # 1. Abre o arquivo HTML local que você já salvou no projeto
    with open("pagina.html", "r", encoding="utf-8") as arquivo:
        html_mock = arquivo.read()

    # 2. Chama a sua função original passando o mock
    print("Iniciando teste de extração...")
    dados_extraidos = extrairDados(html_mock)

    # 3. Exibe o resultado final
    print("\n--- Resultado da Extração ---")
    if not dados_extraidos['sucesso']:
        print(f'Não foi possível encontrar os seguintes dados: {dados_extraidos}')
        return
        
    print(dados_extraidos['dados'])


if __name__ == "__main__":
    testar_mock_html()
