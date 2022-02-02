from dados_car_sales import importando_df
import streamlit as st
import pandas as pd 
import numpy as np 
import plotly.express as px
import matplotlib.pyplot as plt 
import seaborn as sns

# Importando dataframe
df = importando_df()

option = st.sidebar.selectbox( 'Para qual página você deseja ir?',
('Inicio', 'Analises', 'Dados'))

if option == "Inicio":
    st.title("EDA Car Sales")
    st.write("O Dataset escolhido para esse trabalho é o 'Car_sales.csv', que consiste em dados de vendas de carros, com seus valores, modelos, preços, eficiência, potência etc. O motivo para a escolha desse conjunto de dados, é a alta abrangência de abordagens e a diversificação de informações. Podendo também ser usado em uma abordagem com Machine Learning, para predição do valor de venda.")
    st.dataframe(df)

elif option == "Analises":
    st.title("Analises dos dados de vendas de carro")
    st.write("O nosso dataset conta com um total de 30 montadoras, sendo essas representadas no gráfico abaixo, junto aos números de vendas.")

    df_vendas = df.groupby("Manufacturer")["Sales_in_thousands"].sum()
    df_vendas = pd.DataFrame(df_vendas,columns=['Manufacturer','Sales_in_thousands'])
    df_vendas['Manufacturer'] = df_vendas.index
    df_vendas.reset_index(drop=True, inplace=True)

    
    fig = px.pie(df_vendas, values="Sales_in_thousands", names='Manufacturer', title='Total de Venda das Fabricantes de Carros')

    st.plotly_chart(fig)


    # Gráfico de barra
    st.write("No gráfico abaixo, temos exposto em um gráfico de barras as 5 montadoras com maior quantidade de modelos. Assim como nas vendas, temos a ford em primeiro, com um total de 11 modelos.")
    manufacture_values = df['Manufacturer'].value_counts()[:5]
    df_m = pd.DataFrame(manufacture_values,columns=['Manufacturer','count'])
    df_m['count'] = df_m['Manufacturer']
    df_m['Manufacturer'] = df_m.index
    df_m.reset_index(drop=True, inplace=True)

    
    manufacture_values = df['Manufacturer'].value_counts()[:5]
    fig2 = px.bar(df_m, x="Manufacturer", y="count", color="Manufacturer" , barmode="group", title='Top 5 quantidade de modelos por montadoras')
    st.plotly_chart(fig2)

    # Gráfico de histograma
    st.write("Com um histograma é possivel ver a distribuição de vendas em milhares do nosso database. Na parte debaixo temos representado a quatidade de vendas, concetradas nos valores do dataset. Já na parte de cima temos o modelo correspondente a esse valor.")
    fig3 = px.histogram(df, x="Sales_in_thousands", color="Manufacturer", marginal="rug", hover_data=df.columns, title='Histograma de vendas em milhares')
    st.plotly_chart(fig3)

    # Gráfico de histograma 2
    st.write("Com um histograma é possivel ver a distribuição de preço em milhares do nosso database. Na parte debaixo temos representado a quatidade de carros com mesma faixa de preço, concetradas nos valores do dataset. Já na parte de cima temos o modelo correspondente a esse valor.")
    fig4 = px.histogram(df, x="Price_in_thousands", color="Model", marginal="rug", hover_data=df.columns, title='Histograma de preço em milhares')
    st.plotly_chart(fig4)

    # HeatMap
    st.write("No gráfico de calor abaixo, é possivel perceber as correlações entre as variaveis do nosso dataframe.")
    fig5 = px.imshow(df.corr())
    st.write(fig5)

    # MONTADORAS #

    st.markdown("## Ford")
    st.write("Analise dos valores da montadora Ford.")
    #Data frame com apenas Carros da ford  
    df_ford = df.loc[df['Manufacturer']=='Ford',:].iloc[:,[1,2,3,4,5,6,7,8,11,12,13,14,15]].copy()
    df_ford = df_ford.sort_values(['Sales_in_thousands'],ascending=False)
    df_ford['Mêdia_valor'] = df_ford['Price_in_thousands'].mean()
    st.dataframe(df_ford.head(5)) 

    #Heatmap ford
    fig6 = px.imshow(df_ford.corr())
    st.write(fig6)

    st.write("Podemos dizer que clientes da ford tem uma maior consciência de compra tendo em vista que muitos fatores têm uma influência forte na compra.")

    st.markdown("## Dodge")
    st.write("Analise dos valores da montadora Dodge.")

    #Data frame com apenas Carros da Dodge
    df_Dodge = df.loc[df['Manufacturer']=='Dodge',:].iloc[:,[1,2,3,4,5,6,7,8,11,12,13,14,15]].copy()
    df_Dodge= df_Dodge.sort_values(['Sales_in_thousands'],ascending=False)
    df_Dodge['Mêdia_valor'] = df_Dodge['Price_in_thousands'].mean()
    st.dataframe(df_Dodge.head(5)) 

    #Heatmap dodge
    fig7 = px.imshow(df_Dodge.corr())
    st.write(fig7)

    st.write("Já o público da Dodge seria mais sensorial pelo fato de que a compra é muito influenciada por uma visualização de robustez do veículo por aparentar ser grande e pesada.")


    st.markdown("## Toyota")                
    st.write("Analise dos valores da montadora Toyota.")

    #Data frame com apenas Carros da Toyota
    df_Toyota = df.loc[df['Manufacturer']=='Toyota',:].iloc[:,[1,2,3,4,5,6,7,8,11,12,13,14,15]].copy()
    df_Toyota= df_Toyota.sort_values(['Sales_in_thousands'],ascending=False)
    df_Toyota['Mêdia_valor'] = df_Toyota['Price_in_thousands'].mean()
    st.dataframe(df_Toyota.head(5))

    #Heatmap toyota
    fig8 = px.imshow(df_Toyota.corr())
    st.write(fig8)

    st.markdown("### Resultados Observados na Analise")
    st.markdown("- As montadoras que mais vendem são ford, dodge e toyota respectivamente.")
    st.markdown("- Um dado curioso é que os veículos mais vendidos de cada montadora tem uma faixa de valor bem similar porém uma análise curiosa que pode ser observada pelo mapa de calor é que o público que compra um Toyota dificilmente compraria um Dodge tendo em vista que o indivíduo prefere ter uma melhor autonomia do veículo.")
    st.markdown("- Porém observamos que entre Ford e Dodge relação mais similar pois o público alvo das montadoras não se importam muito com a eficiência do motor e sim com a potência e com o tamanho do carro.")
    st.markdown("- Sendo assim, podemos concluir que dificilmente Toyota e Dodge vão disputar clientes pelo fato do público da Dodge procurar robustez e o da Toyota economia e carros mais compactos.")