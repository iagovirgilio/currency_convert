
def format_value_br(valor, decimais=2):
    retorno = f"{valor:,.{decimais}f}"
    retorno = retorno.replace(',', '_').replace('.', ',').replace('_', '.')
    return retorno
