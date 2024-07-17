<h1>Web Scraping - Monitoramento de Preços de Tênis de Corrida Masculinos no Mercado Livre</h1>
  
  <h2>Descrição</h2>
  <p>Este projeto realiza a coleta de dados de tênis de corrida masculinos do site Mercado Livre, processa esses dados, e os salva em uma base de dados MySQL. Em seguida, um dashboard interativo é criado utilizando Streamlit para visualização dos principais indicadores de desempenho (KPIs).</p>
  
  <h2>Configuração</h2>
  <ol>
    <li>Clone este repositório:</li>
    <pre><code>git clone https://github.com/seu_usuario/webscraping-mercadolivre.git</code></pre>
    
    Instale as dependências necessárias:
    
    Crie um arquivo <code>.env</code> na raiz do projeto com as seguintes variáveis:
    HOST=your_mysql_host
    USER=your_mysql_user
    PASSWORD=your_mysql_password
    DB_NAME_PROD=your_database_name
  </ol>
  
  <h2>Execução</h2>
  <ol>
    <li>Para iniciar o processo de coleta de dados, execute o seguinte comando:</li>
    <pre><code>scrapy crawl mercadolivre</code></pre>
    
    <li>Após a coleta de dados, processe e salve os dados no MySQL executando o script:</li>
    <pre><code>python data_processing.py</code></pre>
    
    <li>Para visualizar o dashboard interativo, execute o seguinte comando:</li>
    <pre><code>streamlit run dashboard.py</code></pre>
  </ol>
  
  <h2>Arquivos Principais</h2>
  <ul>
    <li><code>mercadolivre_spider.py</code> - Script de web scraping utilizando Scrapy.</li>
    <li><code>data_processing.py</code> - Script de processamento e salvamento de dados.</li>
    <li><code>dashboard.py</code> - Script para criar o dashboard interativo com Streamlit.</li>
    <li><code>requirements.txt</code> - Lista de dependências necessárias para o projeto.</li>
  </ul>
  
  <h2>Bibliotecas Utilizadas</h2>
  <ul>
    <li>Scrapy</li>
    <li>Pandas</li>
    <li>SQLAlchemy</li>
    <li>Streamlit</li>
    <li>dotenv</li>
  </ul>
  
scrapy crawl mercadolivre -o ../../data/data.jsonl
streamlit run dashboard/dashboard.py
