import streamlist as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Minha Primeira Aplicação WEB PYTHON")
df = pd.DataFrame({"Conteudo GC": [56, 45, 55, 35, 44]},
                  index=['especie 1', 'especie 2'.'especie 3',
                         'especie 4', 'especie 5'])

st.markdown("Meu primeiro ***dataframe:**")
st.dataframe(df)


selecao = st.selectbox("Mostrar gráfico?", ["Não", "Sim"])


if selecao == "Sim":
    fig, ax = plt.subplot(figsize=(6, 3))
    ax = plt.bar(df.index, df["Conteudo GC"])
    st.pyplot(fig)


"""
Vamos analisar passo a passo o código acima: 

Linhas 1 a 3: importei as bibliotecas que irei utilizar. 

Linha 5: criei o título da minha aplicação, com o st.title() 

Linha 7: criei um dataframe hipotético com os valores do Conteúdo GC de 5 espécies. 

Linha 11: coloquei em markdown uma descrição para o dataframe, o qual será gerado com o st.dataframe() 

Linha 14: adicionei uma caixa de seleção para que o usuário possa interagir, escolhendo visualizar ou não o gráfico gerado a partir do dataframe. Por padrão, o elemento que está no índice zero (nesse caso, o “Não”) é o escolhido.

Linha 16: coloquei uma condição: caso o usuário selecione “Sim”, o gráfico será gerado.

Salve seu arquivo (salvei como meu-app.py). 
Para rodar a aplicação no navegador, usei o próprio terminal do Visual Studio Code. 
Naveguei até a pasta onde o arquivo foi salvo e rodei o comando: 
streamlit run meu-app.py
"""
