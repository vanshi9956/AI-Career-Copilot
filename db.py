from sqlalchemy import create_engine  ## here create_engine makes a connect between database and python
from sqlalchemy.orm import declarative_base , sessionmaker

DATABASE_URL ="mysql+pymysql://2ur9vNd287kZhK9.root:mdfwC1fhVI71Nthd@gateway01.ap-southeast-1.prod.aws.tidbcloud.com:4000/test?ssl_ca=D:\Downloads\isrgrootx1.pem&ssl_verify_cert=true&ssl_verify_identity=true"
engine=create_engine(
    DATABASE_URL , 
    pool_pre_ping=True, ## checking connection if it is done or not
    connect_args={
        "ssl":{
            "ssl": True ## secure connection bnane ko bolre hai
        }
    }

)

SessionLocal= sessionmaker(bind=engine) ## when we need to update delete data from database then we need this
Base=declarative_base()
