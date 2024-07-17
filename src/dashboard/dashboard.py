import pandas as pd
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os
import streamlit as st

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

def get_data(engine):
    query = f""" SELECT * FROM mercado_livre.items; """
    df = pd.read_sql(query, engine)
    return df 

def kpi(df):
    st.subheader("Principais KPI's do sistema")
    col1, col2, col3 = st.columns(3)
    
    
    total_items = df.shape[0]
    col1.metric(label="Número Total de Itens", value=total_items)
    
    unique_brands = df['brand'].nunique()
    col2.metric(label="Número de marcas únicas", value=unique_brands)
    
    
    average_new_price = df['new_price'].mean()
    col3.metric(label="Média de preços", value=f'{average_new_price:.2f}')
    
    
    st.subheader("Marcas mais encontradas nas 10 primeiras páginas")
    col1, col2 = st.columns([4,2])
    
    top_10 = df['brand'].value_counts().sort_values(ascending=False)
    col1.bar_chart(top_10)
    col2.write(top_10)
    
    #Preço médio por marca
    st.subheader("Preço médio por marca")
    col1, col2 = st.columns([4,2])
    df_zero_prices = df[df['new_price'] > 0]
    average_price_by_brand = df_zero_prices.groupby('brand')['new_price'].mean().sort_values(ascending=False)
    col1.bar_chart(average_price_by_brand)
    col2.write(average_price_by_brand)
    
    #Satisfação por marca
    st.subheader("Satisfação por marca")
    col1, col2 = st.columns([4,2])
    df_zero_reviews = df[df['reviews_rating_number'] > 0]
    satisfaction_by_brand = df_zero_reviews.groupby('brand')['reviews_rating_number'].mean().sort_values(ascending=False)
    col1.bar_chart(satisfaction_by_brand)
    col2.write(satisfaction_by_brand)

def page_config():
    st.set_page_config(page_title='Dashboard do diretor', layout='wide')

def titulo():
    st.title('Vendas')

def descricao():
    st.write("""
        Pesquisa de mercado -  Os tênis mais vendidos do mercado livre.
    """)
    

def dashboard(df):
    st.dataframe(df)
    
if __name__ == '__main__':
    
    HOST_NAME = os.getenv('HOST')
    USER = os.getenv('USER')
    PASSWORD = os.getenv('PASSWORD')
    DATABASE = os.getenv('DB_NAME_PROD')
    
    engine = connect_mysql(HOST_NAME, USER, PASSWORD, DATABASE)
    
    df = get_data(engine)
    page_config()
    titulo()
    descricao()
    kpi(df)