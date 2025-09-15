import pandas as pd
import matplotlib.pyplot as plt
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet
import os

# ---------- 1. Carregar dados ----------
# alunos.csv

arquivo = input("Digite o nome do arquivo CSV ou Excel com os dados (ex: alunos.csv): ")

if not os.path.exists(arquivo):
    print("Arquivo não encontrado! Usando dados fictícios.")
    data = {
        "Aluno": ["Ana", "Bruno", "Carlos", "Daniela", "Eduardo", "Fernanda", "Gabriel", "Helena", "Igor", "Joana"],
        "Turma": ["1º Ano", "1º Ano", "1º Ano", "1º Ano", "2º Ano", "2º Ano", "2º Ano", "2º Ano", "2º Ano", "2º Ano"],
        "Pontuacao": [45, 60, 30, 70, 80, 55, 40, 75, 65, 50]
    }
    df = pd.DataFrame(data)
else:
    if arquivo.endswith(".csv"):
        df = pd.read_csv(arquivo)
    elif arquivo.endswith(".xlsx"):
        df = pd.read_excel(arquivo)
    else:
        raise ValueError("Formato de arquivo não suportado. Use CSV ou XLSX.")

# ---------- 2. Classificar alunos por nível de fluência ----------
def classificar_fluencia(pontos):
    if pontos < 50:
        return "Baixo"
    elif pontos < 70:
        return "Médio"
    else:
        return "Alto"

df["Nível"] = df["Pontuacao"].apply(classificar_fluencia)

# ---------- 3. Criar gráficos ----------
# Gráfico 1: Distribuição geral de fluência
dist_fluencia = df["Nível"].value_counts()
plt.figure(figsize=(6,4))
dist_fluencia.plot(kind="bar", color=["red","orange","green"])
plt.title("Distribuição de Fluência em Leitura")
plt.xlabel("Nível de Fluência")
plt.ylabel("Quantidade de Alunos")
plt.tight_layout()
plt.savefig("grafico_fluencia.png")
plt.close()

# Gráfico 2: Média por turma
media_turma = df.groupby("Turma")["Pontuacao"].mean()
plt.figure(figsize=(6,4))
media_turma.plot(kind="bar", color="skyblue")
plt.title("Média de Fluência por Turma")
plt.xlabel("Turma")
plt.ylabel("Média de Pontuação")
plt.tight_layout()
plt.savefig("grafico_media_turma.png")
plt.close()

# ---------- 4. Gerar relatório em PDF ----------
pdf_path = "Relatorio_Fluencia.pdf"
doc = SimpleDocTemplate(pdf_path, pagesize=A4)
styles = getSampleStyleSheet()
story = [Paragraph("<b>Relatório de Avaliação de Fluência em Leitura</b>", styles["Title"]), Spacer(1, 20)]

# Título

# Introdução
intro = "Este relatório apresenta os resultados da avaliação de fluência em leitura aplicada aos alunos do 1º e 2º ano do Ensino Fundamental."
story.append(Paragraph(intro, styles["Normal"]))
story.append(Spacer(1, 15))

# Texto com análise
analise_texto = f"No total foram avaliados <b>{len(df)}</b> alunos.<br/>" \
                f"- Baixo: {dist_fluencia.get('Baixo', 0)} alunos<br/>" \
                f"- Médio: {dist_fluencia.get('Médio', 0)} alunos<br/>" \
                f"- Alto: {dist_fluencia.get('Alto', 0)} alunos<br/>"
story.append(Paragraph(analise_texto, styles["Normal"]))
story.append(Spacer(1, 15))

# Inserir gráficos
story.append(Paragraph("<b>Distribuição de Fluência em Leitura</b>", styles["Heading2"]))
story.append(Image("grafico_fluencia.png", width=400, height=250))
story.append(Spacer(1, 20))

story.append(Paragraph("<b>Média de Fluência por Turma</b>", styles["Heading2"]))
story.append(Image("grafico_media_turma.png", width=400, height=250))
story.append(Spacer(1, 20))

# Conclusão
conclusao = "A análise de fluência permite identificar padrões de desempenho e apoiar professores e gestores na definição de estratégias pedagógicas."
story.append(Paragraph(conclusao, styles["Normal"]))

doc.build(story)

print("Relatório gerado com sucesso: Relatorio_Fluencia.pdf")
