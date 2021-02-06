import os
import pandas as pd
from sqlalchemy import create_engine
from loader import db_connection


class DbUpload(object):
    def __init__(self, pd_df, files_list):
        self.df = pd_df
        self.files = files_list

    def upload_df(self):
        """
        :return:
        """
        try:
            # FIXME: Используй mysql,который в loader
            conn = db_connection()
            conn.connect()
            conn.take_alchemy()
            engine = create_engine(conn.take_alchemy(), echo=False)
            con = conn.take_conn()
            cursor = con.cursor()
            cursor.execute("USE graph_generate")
            cursor.execute("SHOW TABLES")
            tables = cursor.fetchall()
            for file in files:  # Check cloning in DB
                file = file[:-4]
                iterator = 0
                if file in str(tables):
                    print('С таким именем есть уже таблица. Заменить? (Y)')
                    interactive = input()
                    if interactive == "Y" or interactive == "y" or interactive == "Д" or interactive == "д":
                        self.df[iterator].to_sql(name=file, con=engine, if_exists='replace', index=False)
                        print("Updated")
                    else:
                        print("It does not update")
                    iterator += 1

                else:
                    try:
                        df_sql = self.df[iterator].to_sql(name=file, con=engine, if_exists='fail', index=False)
                    except Exception as err:
                        print(err)
                    iterator += 1
            cursor.close()
            con.close()

        except Exception as err:
            print(err)
            # TODO: тут нужно настроить логгирование

    @staticmethod
    def file_read(files_directory):
        files_in_directory = os.listdir(path=files_directory)
        df_list = []
        for file in files_in_directory:
            try:
                df_file = open(files_directory + file)
            except IOError as e:
                print(u'Не удалось открыть файл или он не валидный')
            else:
                with df_file as opened_file:
                    dataframe = pd.read_csv(df_file)
                    csv_columns = dataframe  # Get all columns from CSV
                    csv_columns.columns = dataframe.columns.str.replace(r" ", "_")
                    df_list.append(csv_columns)
        return df_list, files_in_directory


if __name__ == '__main__':
    directory = "./data_frame_files/"
    df, files = DbUpload.file_read(directory)
    db_upload = DbUpload(pd_df=df, files_list=files)
    db_upload.upload_df()
