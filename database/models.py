# database/models.py
from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from database.session import Base

class Member(Base):
    __tablename__ = 'members'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    contact = Column(String(20))
    address = Column(String(255))

    loans = relationship("Loan", back_populates="member")
    contributions = relationship("Contribution", back_populates="member")


class Loan(Base):
    __tablename__ = 'loans'

    is_member = Column(Boolean, default=True)
    id = Column(Integer, primary_key=True)
    form_number = Column(String(20), unique=True)
    name = Column(String(100), nullable=False)
    contact = Column(String(20))
    guarantor = Column(String(100))
    guarantor_phone = Column(String(20))
    cheque_number = Column(String(50))      # <-- Added
    batch_number = Column(String(50))       # <-- Added
    approval_date = Column(Date)            # <-- Added
    member_id = Column(String(20), ForeignKey('members.id'), nullable=False)
    amount = Column(Float, nullable=False)
    rate = Column(Float, default=5.0)
    term = Column(Integer, default=12)
    status = Column(String(20), default='Pending')
    due_date = Column(Date)

    member = relationship("Member", back_populates="loans")


class Contribution(Base):
    __tablename__ = 'contributions'

    id = Column(Integer, primary_key=True)
    member_id = Column(Integer, ForeignKey('members.id'), nullable=False)
    amount = Column(Float, nullable=False)
    date = Column(Date, nullable=False)
    interest = Column(Float, default=0.0)

    member = relationship("Member", back_populates="contributions")