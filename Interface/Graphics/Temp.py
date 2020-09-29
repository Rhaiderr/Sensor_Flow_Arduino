from ETL.SqlConnection import sql_conn
import pandas as pd

class temp_axes(object):
    def __init__(self):
        self.df = pd.read_sql(sql='select * from grafico_temperatura order by dt_processamento desc limit 10', con=sql_conn())

    def x(self):
        return list(self.df.dt_processamento)

    def y(self):
        return list(self.df.sen_temp.array)
