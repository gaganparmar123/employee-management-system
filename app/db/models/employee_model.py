from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    Date,
    ForeignKey,
    Numeric
)

from sqlalchemy.orm import relationship

from app.db.base import Base


class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(255), nullable=False)

    email = Column(String(255), unique=True, nullable=False)

    phone = Column(String(20), nullable=True)

    department_id = Column(
        Integer,
        ForeignKey("departments.id"),
        nullable=False
    )

    designation = Column(String(255), nullable=False)

    salary = Column(Numeric(10, 2), nullable=False)

    joining_date = Column(Date, nullable=False)

    created_by = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    is_active = Column(Boolean, default=True)

    department = relationship("Department")

    creator = relationship("User")