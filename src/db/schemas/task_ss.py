import datetime

from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, DateTime

from sqlalchemy.dialects.postgresql import JSONB

Base = declarative_base()


class TaskSS(Base):
    __tablename__ = 'task_ss'

    task_ss_pk = Column(Integer, primary_key=True)
    client = Column(Integer)

    taskId = Column(String)
    result = Column(JSONB)

    status = Column(Integer, default=0)  # 0 - created, 1 - started, 2 - failed, 3 - finished

    load_dttm = Column(DateTime, default=datetime.datetime.now())
