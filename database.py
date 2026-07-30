from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base 
# DATABASE_URL = "mysql+pymysql://root:Lokesh%40123@localhost:3306/ecommerce"
# DATABASE_URL ="mysql+pymysql://CLICK_TO:REVEAL_PASSWORD@mysql-bd40758-lokeshmachetti9347-22f6.d.aivencloud.com:11771/defaultdb"
DATABASE_URL = "mysql+pymysql://avnadmin:AVNS_zbCupRnEDksbVXiw9un@mysql-bd40758-lokeshmachetti9347-22f6.d.aivencloud.com:11771/defaultdb"
engine = create_engine(DATABASE_URL) 
SessionLocal = sessionmaker( 
    autocommit=False, 
    autoflush=False, 
    bind=engine 
    ) 
Base = declarative_base()
