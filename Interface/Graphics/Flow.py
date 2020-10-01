from ETL.SqlConnection import sql_conn
import pandas as pd

class flow_axes(object):
    def __init__(self):
        self.df = pd.read_sql(sql='select * from grafico_vazao order by dt_processamento desc limit 30', con=sql_conn())

    def x(self):
        return list(reversed(list(pd.to_datetime(self.df.dt_processamento).dt.strftime("%H:%M:%S"))))

    def y(self):
        return list(reversed(list(self.df.sen_vazao.array)))
