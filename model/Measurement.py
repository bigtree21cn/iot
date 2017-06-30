from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class Serializer(object):
    __public__ = None
    "Must be implemented by implementors"

    def to_serializable_dict(self):
        dict = {}
        for public_key in self.__public__:
            value = getattr(self, public_key)
            if value:
                dict[public_key] = value
        return dict


class Measurement(Base, Serializer):
    __public__ = ['start_time', 'device_id', 'mea_id', 'c1', 'c2', 'c3']
    __tablename__ = 'measurements'

    msg_id = Column(Integer, primary_key=True)
    start_time = Column(DateTime, nullable=True)
    device_id = Column(Integer, nullable=False, index=False)
    mea_id = Column(Integer, nullable=False)
    c1 = Column(Float, nullable=False, index=False)
    c2 = Column(Float, nullable=False, index=False)
    c3 = Column(Float, nullable=False, index=False)

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self.msg_id)


'''
mea1 = Measurement()
mea1.msg_id = 2
mea1.start_time = datetime.datetime.now()
mea1.device_id = 100
mea1.c1 = 11
mea1.c2 = 22
mea1.c3 = 33

session = DBSession()
#session.add(mea1)
#session.commit()


for mea in session.query(Measurement).all():
    print (mea.to_serializable_dict())



from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
DB_CONNECTION_STRING='mysql+pymysql://root:123456@10.140.1.17/iot?charset=utf8'
engine = create_engine(DB_CONNECTION_STRING, echo=True)
DBSession = sessionmaker(bind=engine)
session = DBSession()
query = session.query(Measurement).filter(Measurement.msg_id == 1)
print (query)
obj = query.first()
print (obj.to_serializable_dict())
'''
