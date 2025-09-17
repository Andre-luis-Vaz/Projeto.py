import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Avaliação de Fluência", layout="wide")

st.title("📖 Sistema de Avaliação de Fluência em Leitura")

# Upload de arquivo
file = st.file_uploader("Envie um arquivo CSV ou Excel com os dados dos alunos", type=["csv", "xlsx"])

if file:
    if file.name.endswith(".csv"):
        df = pd.read_csv(file)
    else:
        df = pd.read_excel(file)

    # Classificação de fluência
    def classificar_fluencia(pontos):
        if pontos < 50:
            return "Baixo"
        elif pontos < 70:
            return "Médio"
        else:
            return "Alto"

    df["Nível"] = df["Pontuacao"].apply(classificar_fluencia)

    st.subheader("📊 Dados carregados")
    st.dataframe(df)

    # Gráfico 1: Distribuição de fluência
    st.subheader("Distribuição de Fluência em Leitura")
    fig1, ax1 = plt.subplots()
    df["Nível"].value_counts().plot(kind="bar", color=["red", "orange", "green"], ax=ax1)
    ax1.set_xlabel("Nível de Fluência")
    ax1.set_ylabel("Quantidade de Alunos")
    st.pyplot(fig1)

    # Gráfico 2: Média por turma
    st.subheader("Média de Pontuação por Turma")
    fig2, ax2 = plt.subplots()
    df.groupby("Turma")["Pontuacao"].mean().plot(kind="bar", color="skyblue", ax=ax2)
    ax2.set_xlabel("Turma")
    ax2.set_ylabel("Média da Pontuação")
    st.pyplot(fig2)

    # Download dos dados analisados
    st.download_button(
        "📥 Baixar dados analisados (CSV)",
        df.to_csv(index=False).encode("utf-8"),
        "resultado_fluencia.csv",
        "text/csv"
    )

else:
    st.info("Envie um arquivo de dados para iniciar a análise.")
