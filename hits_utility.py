import pandas as pd
import numpy as np

df = pd.read_csv('dataset.csv',sep = ";" )

df_2 = df.drop(['name', 'team','nationality','position','potential','overall'],1)

df_origin = df_2.head(10)

df ={'player_id':['169134','31912','190871', '203376','200389', '192985', '192985','188545', '183277', '212831']
        , 'age':['29','45', '29','31','40','34','35','36','24','29' ]
        , 'hits':['150','289', '269','137','50','120','90','70','40','100']
    }

df_anonym = pd.DataFrame(df)



def main(df_origin, df_anonym ):

    df_origin = df_origin.copy()
    df_anonym = df_anonym.copy()

    df_origin = df_origin.astype({'age': 'int64', 'hits': 'int64'})
    df_anonym = df_anonym.astype({'age': 'int64', 'hits': 'int64'})

    df_origin['average'] = df_origin['hits'].rolling(2).mean()
    df_origin.at[0,'average'] = df_origin.at[0,'hits']

    df_origin['score'] = abs(df_origin['average'] - df_anonym['hits'])/df_anonym['hits']
    print(df_origin)
    print(df_anonym)
    print(df_origin['score'].mean())
    

if __name__ == "__main__":
    main(df_origin,df_anonym)




