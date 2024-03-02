def format_brazilian_currency(value, decimals=2):
    formatted_value = f"{value:,.{decimals}f}"
    formatted_value = formatted_value.replace(',', '_').replace('.', ',').replace('_', '.')
    return formatted_value
