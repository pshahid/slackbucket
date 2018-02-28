from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DBConfig:
    engine = None
    base = None
    session = None

    def create(self, c):
        vendor = c['vendor']

        if vendor == 'postgres':
           connstr = 'postgres://'
        elif vendor == 'sqlite':
            connstr = 'sqlite://'
        elif vendor == 'mysql':
            connstr = 'mysql://'
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

        self.session = sessionmaker(bind=self.engine)
        self.base.metadata.create_all()

config = DBConfig()

