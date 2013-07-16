# -*- coding: utf-8 -*-
"""
    photolog.database
    ~~~~~~~~~~~~~~~~~

    DB 연결 및 쿼리 사용을 위한 공통 모듈.

    :copyright: (c) 2013 by 4mba.
    :license: MIT LICENSE 2.0, see license for more details.
"""


from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


class DBManager:
    """데이터베이스 처리를 담당하는 공통 클래스"""
    
    _engine = None
    session = None

    @staticmethod
    def init(db_url, db_log_flag=True):
        DBManager._engine = create_engine(db_url, echo=db_log_flag, convert_unicode=True) 
        DBManager.session = scoped_session(sessionmaker(autocommit=False, 
                                                        autoflush=False, 
                                                        bind=DBManager._engine))
        global dao
        dao = DBManager.session
    
    @staticmethod
    def init_db():
        from photolog.model import Base
        Base.metadata.create_all(bind=DBManager._engine)

dao = None        
