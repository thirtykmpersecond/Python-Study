from pandas import DataFrame
from pandas import Series
from sqlalchemy import create_engine
#import pymysql
#启动引擎
#此处一定写为mysql+pymysql
engine = create_engine("mysql+pymysql://xzw:Hasmanafuture?@127.0.0.1:3306/mytest?charset=utf8")
#
df = DataFrame({'app_name':Series(['QQ 音乐','京东 APP']),
                'url':Series(['http://music.qq.com','http://jd.com']),
                'country':Series(['CN','CN'])})

#存放入MySQL
df.to_sql(name='apps',
          con=engine,
          if_exists='append',
          index=False,
          index_label=False)