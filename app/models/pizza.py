from __future__ import annotations
from typing import (
    List,
    Optional,
)
from sqlalchemy import (
    ForeignKey,
    String,
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)
from . import Base

class Pizza(Base):
	__tablename__ = "pizza"

	id: Mapped[int] = mapped_column(primary_key=True)
	name: Mapped[Optional[str]]
	ingridients: Mapped[str] = mapped_column(String(100))
	price: Mapped[int] = mapped_column()
