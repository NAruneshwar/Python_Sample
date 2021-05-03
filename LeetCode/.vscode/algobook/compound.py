import psycopg2
import pandas as pd
import numpy as np
from collections import defaultdict 

class compound_return():
    def __init__(self):
        self.df = self.connect()

    def connect(self):
        conn = psycopg2.connect(
        host="35.188.222.122",
        database="postgres",
        user="big_lebowski",
        password="XZg28!#L",
        port="5432")
        cur =conn.cursor()
        cur.execute('Select s.proper_name,s.ticker_region,d.isin_code,d.p_date,d.currency,d.one_day_pct from security_reference s inner join daily_returns d on s.isin_code = d.isin_code order by d.isin_code, d.p_date')
        security_reference_rows = cur.fetchall()
        df = pd.DataFrame(security_reference_rows)
        df.columns = ['proper_name','ticker_region','isin_code','p_date','currency','one_day_pct']
        df['p_date'] = pd.to_datetime(df['p_date'])
        df['year'] = df['p_date'].dt.year
        cur.close()
        return df

    def compound_total_return(self):
        df = self.df
        df1 = df.pivot_table(index=['p_date'], columns='ticker_region', values=['one_day_pct'])
        df1['one_day_pct'] = df1['one_day_pct'].fillna(1)
        df1.columns = [col[1] for col in df1.columns.values]
        cum_return = ((df1.iloc[-1] - df1.iloc[0])/df1.iloc[0])
        return cum_return

    def compound_annual_growth_rate(self):
        df = self.df
        df['year'] = df['p_date'].dt.year
        df1 = df.pivot_table(index=['p_date'], columns='ticker_region', values=['one_day_pct'])
        df1['one_day_pct'] = df1['one_day_pct'].fillna(1)
        df1.columns = [col[1] for col in df1.columns.values]
        CAGR= ((abs(df1.iloc[-1]/df1.iloc[0]))**(1/5)) - 1
        return CAGR

    def sharpie(self):
        df = self.df
        df1 = df.pivot_table(index=['p_date'], columns='ticker_region', values=['one_day_pct'])
        df1['one_day_pct'] = df1['one_day_pct'].fillna(0)
        df1.columns = [col[1] for col in df1.columns.values]
        sharpie = df1.mean() / df1.std()
        return (sharpie * (252**0.5))


if __name__=='__main__':
    a = compound_return()
    print(a.compound_annual_growth_rate)
    print(a.compound_total_return)
    print(a.sharpie)
    # print(compound_total_return(a))
    # print(compound_annual_growth_rate(a))
    # print(sharpie(a))
    