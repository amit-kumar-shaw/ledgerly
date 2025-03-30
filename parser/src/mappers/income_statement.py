from pydantic import BaseModel
from enum import Enum

class Company(Enum):
    IN_1 = "IN_1"
    DE_1 = "DE_1"
    DE_2 = "DE_2"

class TableLocation(BaseModel):
    table: int
    row: int
    column: int
    convert: bool

class TextLocation(BaseModel):
    text: int
    words: list
    spaces: bool
    convert: bool

earnings_mapper = {
    "IN_1": {},
    "DE_1": {},
    "DE_2": {
        "gross": TableLocation(table=3, row=0, column=1, convert=True),
        "description":  TextLocation(text=0, words=[2, 3], spaces= True, convert=False),
        "monthlyBaseSalary": TableLocation(table=2, row=0, column=9, convert=True),
        # "nonCashBenefits": TableLocation(table=3, row=0, column=1, convert=True),
        # "voluntaryEmployerContributions": TableLocation(table=3, row=0, column=1, convert=True),
        # "oneTimeBonus": TableLocation(table=3, row=0, column=1, convert=True),
        # "holidayPay": TableLocation(table=3, row=0, column=1, convert=True),
        "taxDeduction": TableLocation(table=3, row=0, column=14, convert=True),
        # "taxFreeBenefit": TableLocation(table=3, row=0, column=1, convert=True),
        "taxableAmount": TableLocation(table=3, row=1, column=1, convert=True),
        "net": TableLocation(table=3, row=4, column=14, convert=True),
        "paid": TableLocation(table=5, row=1, column=2, convert=True)
    }
}

taxes_mapper = {
    "IN_1": {},
    "DE_1": {},
    "DE_2": {
        "income": TableLocation(table=3, row=2, column=1, convert=True),
        "church":  TableLocation(table=3, row=4, column=1, convert=True),
        "solidarity": TableLocation(table=3, row=3, column=1, convert=True)
    }
}

social_contributions_mapper = {
    "IN_1": {},
    "DE_1": {},
    "DE_2": {
        "health": TableLocation(table=3, row=1, column=8, convert=True),
        "longTermCare":  TableLocation(table=3, row=4, column=8, convert=True),
        "pension": TableLocation(table=3, row=2, column=8, convert=True),
        "unemployment": TableLocation(table=3, row=3, column=8, convert=True),
        "healthByEmployer": TableLocation(table=3, row=1, column=10, convert=True),
        "longTermCareByEmployer":  TableLocation(table=3, row=4, column=10, convert=True),
        "pensionByEmployer": TableLocation(table=3, row=2, column=10, convert=True),
        "unemploymentByEmployer": TableLocation(table=3, row=3, column=10, convert=True),
        "total": TableLocation(table=3, row=1, column=14, convert=True)
    }
}