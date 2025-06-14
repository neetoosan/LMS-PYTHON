# database/crud.py
from typing import Optional, List
from database.models import Member, Loan, Contribution
from sqlalchemy.orm import Session


# MEMBER CRUD
def get_member(db: Session, member_id: int) -> Optional[Member]:
    return db.query(Member).filter(Member.id == member_id).first()


def get_members(db: Session, skip: int = 0, limit: int = 100) -> List[Member]:
    return db.query(Member).offset(skip).limit(limit).all()


def create_member(db: Session, name: str, contact: str, address: str) -> Member:
    db_member = Member(name=name, contact=contact, address=address)
    db.add(db_member)
    db.commit()
    db.refresh(db_member)
    return db_member


def update_member(db: Session, member_id: int, name: str, contact: str, address: str):
    db_member = get_member(db, member_id)
    if db_member:
        db_member.name = name
        db_member.contact = contact
        db_member.address = address
        db.commit()
        db.refresh(db_member)
    return db_member


def delete_member(db: Session, member_id: int):
    db_member = get_member(db, member_id)
    if db_member:
        db.delete(db_member)
        db.commit()


# LOAN CRUD
def create_loan(db: Session, member_id: int, amount: float, rate: float = 5.0, term: int = 12):
    db_loan = Loan(member_id=member_id, amount=amount, rate=rate, term=term)
    db.add(db_loan)
    db.commit()
    db.refresh(db_loan)
    return db_loan


# CONTRIBUTION CRUD
def create_contribution(db: Session, member_id: int, amount: float, date: str, interest: float = 0.0):
    db_contribution = Contribution(
        member_id=member_id,
        amount=amount,
        date=date,
        interest=interest
    )
    db.add(db_contribution)
    db.commit()
    db.refresh(db_contribution)
    return db_contribution