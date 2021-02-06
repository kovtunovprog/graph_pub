from utils.mysql_manager.manager import db_connection


def take_info_from_db():
    # FIXME: Используй общий класс mysql
    class_conn = db_connection()
    class_conn.connect()  # return conn and do connection
    conn = class_conn.take_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM db_upload_test")
    row = cursor.fetchone()
    list_information = []
    while row is not None:
        row = cursor.fetchone()
        list_information.append(row)
    columns_names = [i[0] for i in cursor.description]
    class_conn.disconnect()
    return list_information, columns_names


def graph_generator(list_rows, columns_names):
    # TODO: нужно передать график на страницу из views, папка templates - общая для всего проекта
    import pandas as pd
    df = pd.DataFrame(list(list_rows), columns=[columns_names])
    print(df)
    # fig, ax = plt.subplots()
    # props = {
    #     'title': 'Первый график matplotlib',
    #     'xlabel': 'Шаги x',
    #     'ylabel': 'Шаги y',
    # }
    # ax.set(**props)
    # ax.set_xticks([100, 250, 500, 750, 1000])
    # ax.set_yticks([100, 250, 500, 750, 1000])
    df.plot()
    import io
    buf = io.BytesIO()
    buf.seek(0)
    import matplotlib.pyplot as plt
    plt.show()
    import base64
    string = base64.b64encode(buf.read())
    import urllib
    uri = urllib.parse.quote(string)
    return uri


def call_graph_generator():
    list_information, column = take_info_from_db()
    graph_generator(list_information, column)


if __name__ == '__main__':
    list_info, columns = take_info_from_db()
    graph_generator(list_info, columns)
