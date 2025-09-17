# 📖 Sistema de Avaliação de Fluência em Leitura

Protótipo funcional desenvolvido como parte da **Atividade Extensionista II – Tecnologia Aplicada à Inclusão Digital (Uninter)**.  
O sistema permite importar dados de alunos, classificar automaticamente o nível de fluência em leitura, gerar gráficos e exportar os resultados.

---

## 🚀 Funcionalidades
- Upload de arquivo **CSV ou Excel** com os dados dos alunos (`Aluno`, `Turma`, `Pontuacao`).
- Classificação automática dos alunos em **Baixo**, **Médio** ou **Alto** nível de fluência.
- Geração de **gráficos interativos** (distribuição geral e média por turma).
- Exportação dos resultados tratados em **CSV**.
- Pode ser rodado **localmente** ou publicado online via **Streamlit Cloud**.

---

## 🖥️ Como rodar localmente
1. Clone o repositório:
   ```bash
   git clone https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git
   cd SEU_REPOSITORIO
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Rode o sistema:
   ```bash
   streamlit run app.py
   ```

4. Acesse no navegador:
   ```
   http://localhost:8501
   ```

---

## 🌐 Como publicar online (Streamlit Cloud)
1. Suba este repositório no seu GitHub.  
2. Acesse [Streamlit Cloud](https://streamlit.io/cloud).  
3. Conecte sua conta do GitHub e escolha o repositório.  
4. Implante o app → você terá um **link público** para compartilhar no seu trabalho final.  

---

## 📂 Estrutura do repositório
```
📦 fluencia-leitura
 ┣ 📜 app.py              # Código principal do sistema
 ┣ 📜 requirements.txt    # Dependências do projeto
 ┣ 📜 alunos_exemplo.csv  # Planilha de exemplo para teste
 ┗ 📜 README.md           # Este arquivo
```

---

## 📊 Exemplo de dados (alunos_exemplo.csv)
```csv
Aluno,Turma,Pontuacao
Ana,1º Ano,45
Bruno,1º Ano,60
Carlos,1º Ano,30
Daniela,1º Ano,70
Eduardo,2º Ano,80
Fernanda,2º Ano,55
Gabriel,2º Ano,40
Helena,2º Ano,75
Igor,2º Ano,65
Joana,2º Ano,50
```

---

## ✨ Autor
- **Nome:** André Luis de Oliveira Vaz  
- **RU:** 1295815  
- **Curso:** CST em Ciência de Dados – Uninter  
