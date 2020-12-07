import pymysql
import datetime

def init_from_db(type):
    conn = pymysql.connect(host='localhost', port=3306, user='PM', passwd='888888', db='wiki_data_temp')
    cursor = conn.cursor()
    print('\ndbConnected. \nfrom init_from_db()')
    if type == 'date':
        sql = "SELECT date,SUM(access_times) AS sum_access FROM record GROUP BY date"
        cursor.execute(sql)
        data = cursor.fetchall()
        datadict = {}
        for row in data:
            rec = list(row)
            datadict[str(rec[0])]=int(rec[1])
            # listdata.append([str(rec[0]),int(rec[1])])
    elif type == 'keywd':
        sql = "SELECT t.keywd,t.sum_access FROM (SELECT keywd,SUM(access_times) AS sum_access FROM record GROUP BY keywd) as t ORDER BY sum_access DESC"
        cursor.execute(sql)
        data = cursor.fetchall()
        datadict = {}
        for row in data:
            rec = list(row)
            datadict[str(rec[0])]=int(rec[1])
    conn.commit()
    conn.close()
    return datadict

def get_date(date):
    conn = pymysql.connect(host='localhost', port=3306, user='PM', passwd='888888', db='wiki_data_temp')
    cursor = conn.cursor()
    print('\ndbConnected.\nfrom get_data()')
    sql = "SELECT keywd,access_times from record where date = \'" + date +"\' ORDER BY access_times DESC"
    cursor.execute(sql)
    data = cursor.fetchall()
    datadict = {}
    for row in data:
        rec = list(row)
        datadict[str(rec[0])] = int(rec[1])
    conn.commit()
    conn.close()
    return datadict

def get_word(word):
    conn = pymysql.connect(host='localhost', port=3306, user='PM', passwd='888888', db='wiki_data_temp')
    cursor = conn.cursor()
    print('\ndbConnected.\nfrom get_data()')
    sql = "SELECT date,SUM(access_times) AS sum_access FROM record where keywd=\'"+word+"\' GROUP BY date"
    cursor.execute(sql)
    data = cursor.fetchall()
    datadict = {}
    for row in data:
        rec = list(row)
        datadict[str(rec[0])] = int(rec[1])
    conn.commit()
    conn.close()
    return datadict