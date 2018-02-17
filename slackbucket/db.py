from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine


class DBConfig:
    engine = None
    base = None

    def create(self, c):
        driver = c['vendor']

        if driver == 'postgres':
            connstr = 'postgres://'
        elif driver == 'sqlite':
            connstr = 'sqlite://'
        else:
            raise ValueError(f"Database driver {driver} not supported.")

        if c.get('password'):
            connstr += f"{c['password']}@"

        if 'host' not in c and 'port' not in c:
            connstr += ':memory:'
        else:
            if c.get('host'):
                connstr += c['host']

            if c.get('port'):
                connstr += f":{c['port']}"


        self.engine = create_engine(connstr)
        self.base = declarative_base()

config = DBConfig()

