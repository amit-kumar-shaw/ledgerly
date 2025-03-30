from pydantic import BaseModel
from typing import Dict, Any

class Earning(BaseModel):
    gross: float = 0.0
    description: str = ""
    monthlyBaseSalary: float = 0.0
    nonCashBenefits: float = 0.0
    voluntaryEmployerContributions: float = 0.0
    oneTimeBonus: float = 0.0
    holidayPay: float = 0.0
    taxDeduction: float = 0.0
    taxFreeBenefit: float = 0.0
    taxableAmount: float = 0.0
    net: float = 0.0
    paid: float = 0.0
    additional: Dict[str, Any] = {}

class Tax(BaseModel):
    income: float = 0.0
    church: float = 0.0
    solidarity: float = 0.0

class SocialSecurityContribution(BaseModel):
    health: float = 0.0
    longTermCare: float = 0.0
    pension: float = 0.0
    unemployment: float = 0.0
    healthByEmployer: float = 0.0
    longTermCareByEmployer: float = 0.0
    pensionByEmployer: float = 0.0
    unemploymentByEmployer: float = 0.0
    total: float = 0.0
    additional: Dict[str, Any] = {}

class Deduction(BaseModel):
    tax: Tax = Tax()
    socialSecurityContribution: SocialSecurityContribution = SocialSecurityContribution()
    additional: Dict[str, Any] = {}

class Details(BaseModel):
    month: str = ""
    year: int = 0
    gross: float = 0.0
    deduction: float = 0.0
    paid: float = 0.0
