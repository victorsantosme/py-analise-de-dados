import pandas as pd
from twilio.rest import Client
from dotenv import load_dotenv
load_dotenv()
import os

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = (os.environ['account_sid'])
auth_token = (os.environ['auth_token'])
client = Client(account_sid, auth_token)

# Abrir os seis arquivos em excel
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    print(mes)
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'No mês {mes} alguém bateu a meta. Vendedor: {vendedor}. Vendas R${vendas}.')
        message = client.messages \
            .create(
            body=f'No mês {mes} alguém bateu a meta. Vendedor: {vendedor}. Vendas R${vendas}.',
            #from_='telefone a definir',
            #to='telefone a definir'
        )
        print(message.sid)


# pandas / openpyxl / twilio