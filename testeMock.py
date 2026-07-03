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
    if isinstance(dados_extraidos, list):
        print(f'Não foi possível encontrar os seguintes dados: {dados_extraidos}')
        return
        
    print(dados_extraidos)


if __name__ == "__main__":
    testar_mock_html()
