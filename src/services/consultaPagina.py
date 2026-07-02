from services.baixarHtml import baixarHtml
from services.extrairDados import extrairDados


def consultaPagina(url):

    # Caso não tenha URL
    if not url:
        return

    html = baixarHtml(url)

    # Caso não tenha retornado html
    if not html:
        return

    dados = extrairDados(html)

    # Caso não tenha a pagina disponivel
    if not dados:
        return

    return dados
