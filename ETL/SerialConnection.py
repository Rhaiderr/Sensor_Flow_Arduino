"""
Perocesso de ETL que realiza a leitura constante dos dados recebidos via porta serial, trasnforma e salva os dados no banco 
"""


class ETL(object):

    def __init__(self, connection, serial):
        self.connection = connection
        self.serial = serial

    def serial_read(self):
        """ Realiza leitura da porta serial e grava informação no banco de dados"""

        # Leitura da linha
        rl = ReadLine(self.serial)

        # Grava informação de temperatura
        pd.DataFrame(
            {
                'dt_processamento': [datetime.now()],
                'sen_temp': [rl.readline().decode().replace("\r\n", "")]
            }
        ) \
            .to_sql('grafico_temperatura',
                    if_exists='append',
                    con=self.connection,
                    index=False)

        # Grava informação de fluxo
        pd.DataFrame(
            {
                'dt_processamento': [datetime.now()],
                'sen_vazao': [rl.readline().decode().replace("\r\n", "")]
            }
        ) \
            .to_sql('grafico_vazao',
                    if_exists='append',
                    con=self.connection,
                    index=False)

        # Retorna ao fluxo inicials
        self.main()

    def main(self):
        """ Realiza leitura da linha """
        self.serial_read()


if __name__ == "__main__":
    # abspath = os.path.abspath("__file__")
    # dname = os.path.dirname(abspath)
    # os.chdir(dname)

    from serial import Serial
    import pandas as pd
    from datetime import datetime
    from Serial_Read.ReadLine import ReadLine
    from ETL.SqlConnection import *


    # Classe de gravação no banco de dados
    read = ETL(connection=sql_conn(), serial=Serial('COM6', 9600))

    # inicia loop
    read.main()
