 <h1>Web Scraping - Monitoramento de Preços de Tênis de Corrida Masculinos no Mercado Livre</h1>
  
  <h2>Descrição</h2>
  <p>Este projeto realiza a coleta de dados de tênis de corrida masculinos do site Mercado Livre, processa esses dados, e os salva em uma base de dados MySQL. Em seguida, um dashboard interativo é criado utilizando Streamlit para visualização dos principais indicadores de desempenho (KPIs).</p>
  
  <h2>Configuração</h2>
  <ol>
    <li>Clone este repositório:</li>
    <pre><code>git clone https://github.com/seu_usuario/webscraping-mercadolivre.git</code></pre>
    
    Instale as dependências necessárias:
    pip install -r requirements.txt
    
    Crie um arquivo .env na raiz do projeto com as seguintes variáveis:
    HOST=your_mysql_host
    USER=your_mysql_user
    PASSWORD=your_mysql_password
    DB_NAME_PROD=your_database_name</code></pre>
  </ol>
  <h2>Bibliotecas Utilizadas</h2>
  <ul>
    <li>Scrapy</li>
    <li>Pandas</li>
    <li>SQLAlchemy</li>
    <li>Streamlit</li>
    <li>dotenv</li>
  </ul>

  <h2>Arquivos Principais</h2>
  <ul>
    <li><code>mercadolivre_spider.py</code> - Script de web scraping utilizando Scrapy.</li>
    <li><code>data_processing.py</code> - Script de processamento e salvamento de dados.</li>
    <li><code>dashboard.py</code> - Script para criar o dashboard interativo com Streamlit.</li>
    <li><code>requirements.txt</code> - Lista de dependências necessárias para o projeto.</li>
  </ul>
  
  <h2>Execução</h2>
  <ol start="4">
    <li>Crie um banco de dados <code>mercado_livre</code> e a seguinte tabela:</li>
    <pre><code>USE mercado_livre;

CREATE TABLE items (
  Brand VARCHAR(25),
  Name VARCHAR(150),
  Reviews_rating_number FLOAT,
  Reviews_amount INT,
  Source VARCHAR(100),
  Data_coleta DATETIME,
  Old_price FLOAT,
  New_price FLOAT
);</code></pre>
    
    Para iniciar o processo de coleta de dados, execute o seguinte comando:
    scrapy crawl mercadolivre -o ../../data/data.jsonl
    
    Após a coleta de dados, processe e salve os dados no MySQL executando o script:
    python data_processing.py
    
    Para visualizar o dashboard interativo, execute o seguinte comando:
    streamlit run dashboard/dashboard.py
  </ol>
<h2>Utilização do Streamlit</h2>
<p>
    O Streamlit é utilizado para criar um dashboard interativo que mostra os dados de tênis vendidos no mercado livre e seus KPI's.
</p>

<h3>Execução do Streamlit</h3>
<ol>
    <li>Certifique-se de que o ambiente virtual está ativado.</li>
    <li>Execute o comando para iniciar o Streamlit:
        <pre>
streamlit run script.py
        </pre>
        <p>Substitua <code>script.py</code> pelo nome do arquivo Python que contém o código acima.</p>
    </li>
    <li>Abra o navegador e acesse <a href="http://localhost:8501">http://localhost:8501</a> para visualizar o dashboard.</li>
</ol>
<img src='https://github.com/ArthurCoutinho15/WebScraping-MercadoLivre/blob/main/img/Captura%20de%20tela%202024-07-16%20232921.png'/>

