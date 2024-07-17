import pandas as pd
from datetime import datetime
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

load_dotenv()

def connect_mysql(host, user, password, database):
    try:
        connection_url = f'mysql+pymysql://{user}:{password}@{host}/{database}'
        engine = create_engine(connection_url)
        print("Successfully connected to MySQL")
        return engine
    except Exception as err:
        print(f"Error: {err}")
        return None
    
def leitura(path):
    df = pd.read_json('C:\\Users\\Arthur Coutinho\\Desktop\\Arthur Coutinho\\Python\\WebScraping-MonitoramentoPrecos\\data\\data.jsonl', lines=True)
    return df

def cria_colunas(df):
    df['source'] = "https://lista.mercadolivre.com.br/tenis-corrida-masculino"
    df['data_coleta'] = datetime.now()
    return df

def tratamento_tipos(df):
    df['old_price_reais'] = df['old_price_reais'].fillna(0).astype(float)
    df['old_price_cents'] = df['old_price_cents'].fillna(0).astype(float)
    df['new_price_reais'] = df['new_price_reais'].fillna(0).astype(float)
    df['new_price_cents'] = df['new_price_cents'].fillna(0).astype(float)
    df['reviews_rating_number'] = df['reviews_rating_number'].fillna(0).astype(float)
    return df

def tratamento_reviews(df):
    df['reviews_amount'] = df['reviews_amount'].str.replace(r'[\(\)]', '', regex=True)
    df['reviews_amount'] = df['reviews_amount'].fillna(0).astype(int)
    
    return df

def coluna_preco(df):
    df['old_price'] = df['old_price_reais'] + df['old_price_cents'] / 100
    df['new_price'] = df['new_price_reais'] + df['new_price_cents'] / 100
    return df

def remove_colunas(df):
    df = df.drop(columns=['old_price_reais', 'old_price_cents', 'new_price_reais', 'new_price_cents'])
    return df
    
def salvar_no_mysql(df, engine, table_name='items'):
    df.to_sql(name=table_name, con=engine, if_exists='replace', index=True, index_label='Date')
    print(f"Dados salvos na tabela '{table_name}' no MySQL")
    

if __name__ == '__main__':
    HOST_NAME = os.getenv('HOST')
    USER = os.getenv('USER')
    PASSWORD = os.getenv('PASSWORD')
    DATABASE = os.getenv('DB_NAME_PROD')
    
    path = 'C:\\Users\\Arthur Coutinho\\Desktop\\Arthur Coutinho\\Python\\WebScraping-MonitoramentoPrecos\\data'
    engine = connect_mysql(HOST_NAME, USER, PASSWORD, DATABASE)
    
    df = leitura(path)
    df = cria_colunas(df)
    df = tratamento_tipos(df)
    df = tratamento_reviews(df)
    df = coluna_preco(df)
    df = remove_colunas(df)
    salvar_no_mysql(df, engine)
    
    