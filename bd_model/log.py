from typing import List
from typing import Optional
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import Integer, String, ForeignKey, create_engine, DateTime

from .Base import *

class log(Base):
    __tablename__ = "logs"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
   
    ip: Mapped[str] = mapped_column(String(255))
    data = mapped_column(DateTime(timezone=True))
    status: Mapped[int] = mapped_column(Integer)
    query: Mapped[str] = mapped_column(String(255))
    user_agent: Mapped[str] = mapped_column(String(255))

    def __repr__(self) -> str:
        return f"Log(id={self.id!r}, ip={self.ip!r}, data={self.data!r}, status={self.status!r}, query={self.query!r}, user_agent={self.user_agent!r})"

# 91.132.20.33 
# [11/May/2024:21:21:08 +0000] 
# 200 
# "http://185.104.114.7/rest/products/search'||(SELECT/**/0x72695944/**/FROM/**/DUAL/**/WHERE/**/2270=2270/**/OR/**/ROW(2060,5762)>(SELECT/**/COUNT(*),CONCAT(0x716a706b71,(SELECT/**/(ELT(2060=2060,1))),0x716b707171,FLOOR(RAND(0)*2))x/**/FROM/**/(SELECT/**/1247/**/UNION/**/SELECT/**/8186/**/UNION/**/SELECT/**/4742/**/UNION/**/SELECT/**/4825)a/**/GROUP/**/BY/**/x))||'" 
# "Mozilla/5.0 (X11; U; Linux i686; en-GB; rv:1.8.0.5) Gecko/20060731 Ubuntu/dapper-security Firefox/1.5.0.5"