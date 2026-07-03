from bs4 import BeautifulSoup


def extrairDados(html):

    # Caso não tenho o HTML
    if not html:
        return

    # Transforma o HTML de forma légivel
    htmlFormatado = BeautifulSoup(html, "html.parser")

    # Elemento quando a página está indisponivel
    cabecalho = htmlFormatado.find("h1", class_="no-camelcase")

    # Se o elemento estiver disponivel com o seguinte texto, então a pagina não está acessavel
    if ( cabecalho.text == "Conteúdo não foi encontrado ou já sofreu alteração de status e não pode ser alterado por esse meio."): return

    #Inicia as variaveis que serão utilizadas posteriormente
    dados_coleta = {}
    faltando = []

    #Elemento do remetente
    remetente = htmlFormatado.find(attrs={"js-hist-value": "FBPEDCOLETA_CDREMETENTE"})

    #Elemento do destinatario
    destinatario = htmlFormatado.find(
        attrs={"js-hist-value": "FBPEDCOLETA_CDDESTINATARIO"}
    )

    #Elemento do local de coleta
    localDeColeta = {
        "Rua": htmlFormatado.find(
            attrs={"js-hist-value": "FBPEDCOLETA_ENDERECOREM"}
        ),
        "Numero": htmlFormatado.find(
            attrs={"js-hist-value": "FBPEDCOLETA_NUMEROREM"}
        ),
        "Bairro": htmlFormatado.find(
            attrs={"js-hist-value": "FBPEDCOLETA_BAIRROREM"}
        ),
        "Cep": htmlFormatado.find(attrs={"js-hist-value": "FBPEDCOLETA_CEPREM"}),
        "Cidade": htmlFormatado.find(
            attrs={"js-hist-value": "FBPEDCOLETA_CDCIDREM"}
        ),
    }

    #Elemento do valor total
    valorTotal = (
        htmlFormatado.find("div", id="coletas-documentos")
        .find_all("div")[0]
        .find_all("span")[1]
    )

    #Elemento do peso
    peso = (
        htmlFormatado.find("div", id="coletas-documentos")
        .find_all("div")[1]
        .find_all("span")[1]
    )

    #Elemento do volume
    volume = (
        htmlFormatado.find("div", id="coletas-documentos")
        .find_all("div")[1]
        .find_all("span")[2]
    )

    #Caso não tenha remetente
    if not remetente:
        faltando.append("Rementente")
    else:
        dados_coleta["remetente"] = remetente.text.replace("Remetente:", "").split("-", 1)[0].strip()

    #Caso não tenha destinatario
    if not destinatario:
        faltando.append("Destinatário")
    else:
        dados_coleta["destinatario"] = destinatario.text.replace("Destinatário:", "").split("-", 1)[0].strip()

    #Caso não tenha valor total
    if not valorTotal:
        faltando.append("Valor Total")
    else:
        dados_coleta["valorTotal"] = valorTotal.text.replace("Valor Total:", "").replace("R$", "").strip()

    #Caso não tenha local de coleta
    if not localDeColeta:
        faltando.append("Local de Coleta")
    else:
        
        #Loop para passar em cada indice do dict
        for chave, valor in localDeColeta.items():

            #Caso não tenha o indice não tenha valor
            if not valor:
                faltando.append(chave)
            else:
                
                #Adiciona no dict de dados da coleta
                dados_coleta[chave] = (valor.text) 
        
    # Caso não tenha o valor de peso
    if not peso:
        faltando.append("Peso")
    else:
        dados_coleta["peso"] = peso.text.replace("Peso:", "").replace("Kg", "").strip()

    # Caso não tenha o valor de volume
    if not volume:
        faltando.append("Volume")
    else:
        dados_coleta["volume"] = volume.text.replace("Volume:", "").strip()
        
    return{
        "sucesso": len(faltando) == 0,
        "dados": dados_coleta,
        "faltando": faltando
    }
