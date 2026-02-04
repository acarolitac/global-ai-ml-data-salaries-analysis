import streamlit as st
import pandas as pd
import plotly.express as px

# Configuração da página
st.set_page_config(
    page_title="Dashboard - Salários na Área de Dados",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Carregando os dados
@st.cache_data
def load_data():
    try:
        df = pd.read_csv('data/salaries_dashboard.csv')
        return df
    except FileNotFoundError:
        st.error("Arquivo 'data/salaries_dashboard.csv' não encontrado!")
        return pd.DataFrame()

df = load_data()

if df.empty:
    st.stop()

# CSS
st.markdown("""
<style>
    /* cor de fundo das tags*/
    span[data-baseweb="tag"] {
        background-color: #3B82F6 !important;
        color: white !important;
    }
    
    /* cor do X (ícone de fechar) */
    span[data-baseweb="tag"] svg {
        fill: white !important;
    }
    
    /* Efeito hover */
    span[data-baseweb="tag"]:hover {
        background-color: #1D4ED8 !important;
    }
    
    /* texto dentro da tag */
    span[data-baseweb="tag"] span {
        color: white !important;
    }
</style>
""", unsafe_allow_html=True)

# BARRA LATERAL - Filtros
with st.sidebar:
    st.title("🔍 Filtros")
    st.markdown("---")
    
    # Verificar se as colunas existem
    colunas_disponiveis = df.columns.tolist()
    
    # Filtro de Ano
    if 'work_year' in colunas_disponiveis:
        anos_disponiveis = sorted(df['work_year'].unique())
        anos_selecionados = st.multiselect(
            "**Ano**", 
            anos_disponiveis, 
            default=anos_disponiveis
        )
    else:
        anos_selecionados = []
        st.warning("Coluna 'work_year' não encontrada")
    
    # Filtro de Senioridade
    if 'experience_level_pt' in colunas_disponiveis:
        senioridades_disponiveis = sorted(df['experience_level_pt'].unique())
        senioridades_selecionadas = st.multiselect(
            "**Senioridade**", 
            senioridades_disponiveis, 
            default=senioridades_disponiveis
        )
    else:
        senioridades_selecionadas = []
    
    # Filtro por Tipo de Contrato
    if 'employment_type_pt' in colunas_disponiveis:
        contratos_disponiveis = sorted(df['employment_type_pt'].unique())
        contratos_selecionados = st.multiselect(
            "**Tipo de Contrato**", 
            contratos_disponiveis, 
            default=contratos_disponiveis
        )
    else:
        contratos_selecionados = []
    
    # Filtro por Tamanho da Empresa
    if 'company_size_pt' in colunas_disponiveis:
        tamanhos_disponiveis = sorted(df['company_size_pt'].unique())
        tamanhos_selecionados = st.multiselect(
            "**Tamanho da Empresa**", 
            tamanhos_disponiveis, 
            default=tamanhos_disponiveis
        )
    else:
        tamanhos_selecionados = []
    
# APLICAR FILTROS
df_filtrado = df.copy()

# Aplicar filtros apenas se as colunas existirem
filtros = []

if 'work_year' in df.columns and anos_selecionados:
    filtros.append(df_filtrado['work_year'].isin(anos_selecionados))

if 'experience_level_pt' in df.columns and senioridades_selecionadas:
    filtros.append(df_filtrado['experience_level_pt'].isin(senioridades_selecionadas))

if 'employment_type_pt' in df.columns and contratos_selecionados:
    filtros.append(df_filtrado['employment_type_pt'].isin(contratos_selecionados))

if 'company_size_pt' in df.columns and tamanhos_selecionados:
    filtros.append(df_filtrado['company_size_pt'].isin(tamanhos_selecionados))

# Combinar todos os filtros
if filtros:
    for filtro in filtros:
        df_filtrado = df_filtrado[filtro]

# CONTEÚDO PRINCIPAL
st.title("Salários na Área de Dados - Panorama Global")
st.markdown("Explore os dados salariais na área de dados nos últimos anos. Utilize os filtros à esquerda para refinar sua análise.")

# MÉTRICAS PRINCIPAIS (KPIs) 
st.subheader("📈 Métricas gerais (Salário anual em USD)")

if not df_filtrado.empty:
    salario_medio = df_filtrado['salary_in_usd'].mean()
    salario_maximo = df_filtrado['salary_in_usd'].max()
    total_registros = df_filtrado.shape[0]
    cargo_mais_frequente = df_filtrado["job_title"].mode()[0] if not df_filtrado["job_title"].mode().empty else "N/A"
else:
    salario_medio, salario_maximo, total_registros, cargo_mais_frequente = 0, 0, 0, "N/A"

# Layout de 4 colunas
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Salário médio", f"${salario_medio:,.0f}")

with col2:
    st.metric("Salário máximo", f"${salario_maximo:,.0f}")

with col3:
    st.metric("Total de registros", f"{total_registros:,}")

with col4:
    st.metric("Cargo mais frequente", cargo_mais_frequente)

st.markdown("---")

# GRÁFICOS 
st.subheader("📊 Análise Visual dos Dados")

# LINHA 1: Gráfico 1 e Gráfico 2
col_graf1, col_graf2 = st.columns(2)

# GRÁFICO 1: Top 10 cargos por salário médio
with col_graf1:
    if not df_filtrado.empty and 'job_title' in df_filtrado.columns and 'salary_usd_k' in df_filtrado.columns:
        top_cargos = df_filtrado.groupby('job_title')['salary_usd_k'].mean().nlargest(10).sort_values(ascending=True).reset_index()
        
        grafico_cargos = px.bar(
            top_cargos,
            x='salary_usd_k',
            y='job_title',
            orientation='h',
            title="Top 10 Cargos por Salário Médio",
            labels={'salary_usd_k': 'Média Salarial Anual (mil USD)', 'job_title': ''},
            color_discrete_sequence=["#1f77b4"]  
        )
        grafico_cargos.update_traces(
            texttemplate='$%{x:.1f}K',
            textposition='outside'
        )
        grafico_cargos.update_layout(
            height=400,
            yaxis={'categoryorder':'total ascending'}
        )
        st.plotly_chart(grafico_cargos, use_container_width=True)
    else:
        st.info("⚠️ Dados insuficientes para o gráfico de cargos")

# GRÁFICO 2: Distribuição de salários anuais
with col_graf2:
    if not df_filtrado.empty and 'salary_usd_k' in df_filtrado.columns:
        grafico_hist = px.histogram(
            df_filtrado,
            x='salary_usd_k',
            nbins=30,
            title="Distribuição de Salários Anuais",
            labels={'salary_usd_k': 'Faixa Salarial (mil USD)', 'quantidade': 'Frequência'},
            color_discrete_sequence=["#1f77b4"] 
        )
        grafico_hist.update_layout(height=400)
        st.plotly_chart(grafico_hist, use_container_width=True)
    else:
        st.info("⚠️ Dados insuficientes para o histograma")

# LINHA 2: Gráfico 3 e Gráfico 4
col_graf3, col_graf4 = st.columns(2)

# GRÁFICO 3: Proporção por tipo de trabalho
with col_graf3:
    if not df_filtrado.empty and 'remote_ratio_pt' in df_filtrado.columns:
        contagem_remoto = df_filtrado['remote_ratio_pt'].value_counts().reset_index()
        contagem_remoto.columns = ['tipo_trabalho', 'quantidade']
        cores_pizza = ["#1f77b4", "#00163F", "#c7edff", "#087685"]
        
        fig_pizza = px.pie(
            contagem_remoto,
            names='tipo_trabalho',
            values='quantidade',
            title='Proporção por Tipo de Trabalho',
            color_discrete_sequence=cores_pizza,
            hole=0.5 
        )
        
        fig_pizza.update_traces(
            textposition='inside',
            textinfo='percent+label',
            textfont_size=14,
            pull=[0.02, 0.02, 0.02]
        )
        
        fig_pizza.update_layout(height=450, showlegend=True)
        st.plotly_chart(fig_pizza, use_container_width=True)
    else:
        st.info("⚠️ Dados de tipo de trabalho não disponíveis")

# GRÁFICO 4: Média Salarial por Nível de Experiência
with col_graf4:
    if not df_filtrado.empty and 'experience_level_pt' in df_filtrado.columns and 'salary_usd_k' in df_filtrado.columns:
        media_salario_experiencia = df_filtrado.groupby('experience_level_pt')['salary_usd_k'].mean().round(2)
        media_salario_experiencia = media_salario_experiencia.sort_values(ascending=False).reset_index()

        fig_experiencia = px.bar(
            media_salario_experiencia,
            x='experience_level_pt',
            y='salary_usd_k',
            title="Média Salarial por Nível de Experiência",
            labels={"experience_level_pt": "Nível de Experiência", "salary_usd_k": "Salário Médio Anual (mil USD)"},
            color='salary_usd_k',
            color_discrete_sequence=["#1f77b4"], 
            text='salary_usd_k'
        )

        fig_experiencia.update_traces(
            texttemplate='$%{text:.1f}K',
            textposition='outside'
        )

        fig_experiencia.update_layout(height=450)
        st.plotly_chart(fig_experiencia, use_container_width=True)
    else:
        st.info("⚠️ Dados de experiência não disponíveis")

# LINHA 3: Gráfico 5 e Gráfico 6
col_graf5, col_graf6 = st.columns(2)

# GRÁFICO 5: Mapa de salários por país
with col_graf5:
    if not df_filtrado.empty and 'residence_iso3' in df_filtrado.columns and 'job_title' in df_filtrado.columns:
        # Filtro para Data Scientists
        df_data_scientist = df_filtrado[df_filtrado['job_title'] == 'Data Scientist']
        
        if not df_data_scientist.empty:
            media_data_scientist_pais = df_data_scientist.groupby('residence_iso3')['salary_usd_k'].mean().reset_index()
            media_data_scientist_pais = media_data_scientist_pais.dropna(subset=['residence_iso3'])
            
            if not media_data_scientist_pais.empty:
                grafico_paises = px.choropleth(
                    media_data_scientist_pais,
                    locations='residence_iso3',
                    color='salary_usd_k',
                    color_continuous_scale=[
                        "#caf0f8", 
                        "#90dbf4",
                        "#00b4d8",
                        "#023e8a"
                    ],
                    title='🌍 Salário Médio de Data Scientists por País',
                    labels={'salary_usd_k': 'Salário Médio (mil USD)', 'residence_iso3': 'País'},
                    hover_data={'salary_usd_k': ':.2f'}
                )
                
                grafico_paises.update_traces(
                    hovertemplate="<b>%{location}</b><br>Salário: $%{z:,.1f}K<extra></extra>"
                )
                
                grafico_paises.update_layout(
                    geo=dict(
                        showframe=False,
                        showcoastlines=True,
                        projection_type='natural earth'
                    ),
                    height=450
                )
                
                st.plotly_chart(grafico_paises, use_container_width=True)
            else:
                st.info("🌍 Nenhum código de país válido para Data Scientists")
        else:
            st.info("🌍 Nenhum Data Scientist encontrado nos dados filtrados")
    else:
        st.info("🌍 Dados de localização não disponíveis")

# GRÁFICO 6: Média Salarial por Tamanho da Empresa 
with col_graf6:
    if not df_filtrado.empty and 'company_size_pt' in df_filtrado.columns and 'salary_usd_k' in df_filtrado.columns:
        media_salario_tamanho = df_filtrado.groupby('company_size_pt')['salary_usd_k'].mean().reset_index()
        
        fig_tamanho = px.bar(
            media_salario_tamanho,
            x='company_size_pt',
            y='salary_usd_k',
            title="🏢 Média Salarial por Tamanho da Empresa",
            labels={'company_size_pt': 'Tamanho da Empresa', 'salary_usd_k': 'Salário Médio (mil USD)'},
            color='salary_usd_k',
            color_continuous_scale='Blues',
            text='salary_usd_k'
        )
        
        fig_tamanho.update_traces(
            texttemplate='$%{text:.1f}K',
            textposition='outside'
        )
        
        fig_tamanho.update_layout(height=450)
        st.plotly_chart(fig_tamanho, use_container_width=True)
    else:
        st.info("🏢 Dados de tamanho da empresa não disponíveis")

# TABELA DE DADOS DETALHADOS
st.markdown("---")
st.subheader("📋 Dados Detalhados")

if not df_filtrado.empty:
    colunas_para_mostrar = [
        'work_year', 'experience_level_pt', 'employment_type_pt',
        'job_title', 'salary_usd_k', 'company_size_pt', 'remote_ratio_pt'
    ]
    
    # Filtrar apenas colunas que existem
    colunas_existentes = [col for col in colunas_para_mostrar if col in df_filtrado.columns]

    st.dataframe(
        df_filtrado[colunas_existentes].head(100),
        use_container_width=True,
        hide_index=True
    )
    
    st.caption(f"📄 Mostrando 100 de {len(df_filtrado)} registros disponíveis")
else:
    st.info("ℹ️ Nenhum dado disponível com os filtros selecionados")

# INFORMAÇÕES ADICIONAIS
st.markdown("---")

# Expander com informações
with st.expander("ℹ️ Sobre este dashboard"):
    st.markdown("""
    ### 📊 Sobre os Dados
    - **Fonte**: Global Salaries in AI, ML, Data Science
    - **Conteúdo**: Salários anuais em USD, cargos, experiência, localização
    - **Objetivo**: Análise de mercado para profissionais de dados
    
    ### 🎯 Como Usar
    1. Use os filtros na barra lateral para refinar a análise
    2. Explore os 6 gráficos interativos
    3. Verifique a tabela para dados detalhados
    
    ### 📈 Métricas Calculadas
    - Panorama geral dos salários na área de Dados          
    - Cargos mais bem remunerados
    - Cargo mais comum na área de dados (de acordo com o DataFrame)
    - Experiência e salários
    - Distruibuição dos tipos de trabalhos
    - Média salarial por tamanho da empresa
    """)

# Rodapé
st.markdown("---")
st.caption("📊 Dashboard criado com Streamlit • Dados: Global Salaries in AI, ML, Data Science • Desenvolvido para Análise de Mercado")
st.caption("Autora: Ana Carolina Itacarambi")