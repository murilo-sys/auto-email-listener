def extrairTexto(elemento, textoExtrair=""):
    if not elemento:
        return None
    
    
    if not isinstance(textoExtrair, list):
        return elemento.text.replace(textoExtrair, "").strip()
    
    textoFormatado = elemento.text
    
    for texto in textoExtrair:
        print(texto)
        textoFormatado = textoFormatado.replace(texto, "").strip()
        
    return textoFormatado
    