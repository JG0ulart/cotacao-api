import requests

def cotacao():
    r = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

    dolar = r.json()['USDBRL']['bid'].replace('.', ',')
    euro = r.json()['EURBRL']['bid'].replace('.', ',')
    bitcoin = r.json()['BTCBRL']['bid']
    return f"""
        Preço do dolar hoje R$ 0{dolar}
        Preço do euro hoje R$ 0{euro}
        Preço do bitcoin hoje R$ {bitcoin},00
        """
        
        
print(cotacao())