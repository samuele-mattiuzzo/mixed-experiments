import datetime
from dataclasses import dataclass

MAPPING = {
    # Product fields
    "PR_ID": 3,
    "PR_PARENT": 4,
    "PR_TITLE": 5,
    "PR_CATEGORY": 6,

    # Review fields
    "RE_ID": 2,
    "RE_CUSTOMER": 1,
    "RE_STARS": 7,
    "RE_HEADLINE": 12,
    "RE_BODY": 13,
    "RE_DATE": 14
}

@dataclass
class Product:
    id: str
    parent: str
    title: str
    category: str

@dataclass
class Review:
    id: str
    customer_id: str
    stars: int
    headline: str
    body: str
    date: datetime.datetime
    product: Product

