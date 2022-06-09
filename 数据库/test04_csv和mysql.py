import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv('../csv文件/xsb.csv')

# 当engine连接的时候我们就插入数据
engine = create_engine('mysql://root:ccbbyy..2030@localhost/xsb?charset=utf8')
with engine.connect() as conn, conn.begin():
    df.to_sql('xsb', conn, if_exists='replace')
