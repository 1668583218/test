import pandas

xiaoshuaib = pandas.read_csv('xiaoshuaib.csv', encoding='gbk')
# print(xiaoshuaib)
with True:
    xiaoshuaib.to_sql('xsb', conn, if_exists='replace')
