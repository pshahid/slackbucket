from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine


class DBConfig:
    engine = None

    def create(self, config):
        driver = config['vendor']

        if driver == 'postgres':
            connstr = 'postgres://'
        elif driver == 'sqlite':
            connstr = 'sqlite://'
        else:
            raise ValueError(f"Database driver {driver} not supported.")

        if config['password']:
            connstr += f"{config['password']}@"
        connstr += f"{host}:{port}"

        self.engine = create_engine(connstr)

config = DBConfig()

Base = declarative_base()
