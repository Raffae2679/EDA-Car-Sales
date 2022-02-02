import pandas as pd

def pegando_df():
    link = 'https://raw.githubusercontent.com/Raffae2679/EDA-Car-Sales/main/Dataset/Car_sales.csv'
    df = pd.read_csv(link)

    return df 


def importando_df():
    df = pegando_df()

    df_tratado = tratando_df(df)


    return df_tratado


def tratando_df(df):

    # Corrigimos o tipo do dado que se encontrava na coluna "Latest_launch", para o formato datetime
    df.Latest_Launch = pd.to_datetime(df.Latest_Launch) 

    # Para lidar com os valores nulos da coluna "year_resale_value", resolvemos substituir pela média dos valores dessa coluna
    df['__year_resale_value'] = df['__year_resale_value'].fillna(df['__year_resale_value'].mean())

    # Já os valores nulos restantes, apenas demos um drop nessas linhas

    df.dropna(inplace=True)

    return df 


if __name__ == "__main__":
    df = importando_df()
    print(df)