import psycopg2
import sys

conn_string = "host='localhost' port='5433' dbname='rocktribe' user='rocktribe' password='rocktribe'"
conn = psycopg2.connect(conn_string)
cursor = conn.cursor()


class DbInit():

    def __init__(self):
        cursor.execute("DROP TABLE IF EXISTS pictures")
        cursor.execute("CREATE TABLE pictures(id INT PRIMARY KEY, title TEXT, url TEXT, description TEXT)")
        cursor.execute("INSERT INTO pictures VALUES(1,'Nick at New River Gorge National River'"
                       ",'https://fbcdn-sphotos-g-a.akamaihd.net/hphotos-ak-xfp1/t1.0-9/10303368_319268634903365""_8162484403308547357_n.jpg',"
                       "'Photo credit Mac Wood')")
        conn.commit()


class Query(object):

    def querypictures(self):
        cursor.execute("SELECT * FROM pictures")
        pictures = cursor.fetchall()
        print pictures[0][2]
        return pictures