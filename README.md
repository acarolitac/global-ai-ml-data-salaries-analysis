# 🌍 Global AI, ML & Data Salaries Analysis

Projeto de **Análise de Dados** desenvolvido a partir do **Global AI, ML & Data Science Salaries Dataset** (Kaggle), com o objetivo de analisar padrões salariais na área de Dados considerando **nível de experiência, cargo, tipo de trabalho e localização**.

O projeto contempla **ETL, Análise Exploratória (EDA)** e a construção de um **Dashboard Interativo com Streamlit**, simulando um pipeline completo de análise de dados aplicado a um cenário real.

O foco principal foi:
- Consolidar conhecimentos em **análise de dados end-to-end**
- Criar visualizações interativas para **apoio à tomada de decisão**
- Aplicar boas práticas de organização, código e documentação

---

## 🛠️ Tecnologias Utilizadas
![Python](https://img.shields.io/badge/Python-blue)
![Pandas](https://img.shields.io/badge/Pandas-150458)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B)
![Plotly](https://img.shields.io/badge/Plotly-lightgrey)

- **Python**
- **Pandas** – manipulação e limpeza de dados  
- **Plotly** – visualizações interativas  
- **Streamlit** – dashboard web  
- **Matplotlib** – visualizações auxiliares  

---

## 🚀 Processos

### ETL
- **Extração:** carregamento do dataset público do Kaggle
- **Transformação:** limpeza dos dados, padronização de categorias e criação de variáveis derivadas
- **Carga:** estruturação e salvamento dos dados tratados para uso em análises e no dashboard interativo

### Análise Exploratória (EDA)
- Estatísticas descritivas
- Identificação de padrões, tendências e distribuições
- Análise por cargo, senioridade, tipo de contrato e localização
- Avaliação de dispersão salarial e identificação de outliers

### Dashboard Interativo
- Visualizações interativas desenvolvidas com Plotly
- Filtros dinâmicos para exploração dos dados pelo usuário
- Layout customizado no Streamlit
- Inclusão de novos gráficos além do escopo do projeto original
- Interface responsiva e intuitiva

---

## 📁 Estrutura do Projeto
```
global-data-salaries-analysis/
│
├── data/
│ ├── salaries.csv
│ ├── salaries_clean.csv
│ └── salaries_dashboard.csv
│
├── notebooks
│ ├── 01_etl_cleaning.ipynb
│ └── 02_eda.ipynb
│
├── app.py
│
├── requirements.txt
```
---

## 📊 Principais Insights

- A maioria dos profissionais da amostra atua em nível **Sênior**
- O **contrato em tempo integral** é o mais frequente
- **Data Scientist** é o cargo mais comum
- **Estados Unidos** concentram a maior parte dos profissionais e empresas
- O **regime presencial** ainda predomina, embora remoto e híbrido sejam relevantes
- Empresas de **médio porte** representam a maior parcela da amostra

### Análise Salarial
- Os salários variam entre **USD 15.000 e USD 800.000 anuais**, indicando alta dispersão
- A média salarial (~USD 159.000) é maior que a mediana, sugerindo **assimetria**
- Cargos de **liderança e executivos** apresentam as maiores médias salariais
- Profissionais com maior experiência tendem a receber salários mais elevados

### Porte da Empresa
- Empresas de **médio porte** apresentam a maior média salarial na base analisada
- Não há evidência de relação direta entre maior porte e maior remuneração
- Resultados podem ser influenciados pela representatividade de cada grupo

---

## 📚 Aprendizados
Este projeto permitiu consolidar conhecimentos em:
- Construção de pipelines **ETL**
- **Análise Exploratória de Dados** com Python
- Criação de **dashboards interativos**
- Visualização de dados para tomada de decisão
- Organização de projetos e boas práticas de documentação

---

## 💚 Créditos
- Projeto base: **Imersão Python com Dados – Alura**
- Dataset: Kaggle – Global AI, ML & Data Science Salaries
- Customizações, análises e melhorias: **Ana Carolina Itacarambi**

---

## Autora
**Ana Carolina Itacarambi**  
Tecnóloga em Sistemas para Internet em transição para a área de Dados, com foco em **Análise de Dados**.

<p align="left">
    <a href="https://www.linkedin.com/in/ana-carolina-itacarambi-araujo/" target="_blank">
      <img 
        src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" 
        alt="LinkedIn"
      />
    </a>
</p>

---

⭐ Se você gostou deste projeto, considere deixar uma estrela no repositório!
