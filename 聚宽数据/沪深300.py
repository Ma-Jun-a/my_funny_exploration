from jqdatasdk import *
from sqlalchemy import create_engine

auth('13821503367', '503367')
q=query(finance.FUND_NET_VALUE).filter(finance.FUND_NET_VALUE.code=='000176').limit(1)
df=finance.run_query(q)
# engine = create_engine('mysql+pymysql://user:password@localhost/stonetest?charset=utf8')
# df = pd.read_sql('emp_master', engine)
# # make sure emp_master_backup table has been created
# # so the table schema is what we want
# df.to_sql('emp_backup', engine, index=False, if_exists='append')
print(df)