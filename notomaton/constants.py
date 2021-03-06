from enum import Enum

class Product(Enum):
    ZENKO = 1
    S3C = 2
    RING = 3

PRODUCT_TO_NAME = {
    Product.ZENKO: 'Zenko',
    Product.S3C: 'S3 Connector',
    Product.RING: 'RING',
}

PRODUCT_TO_CANONICAL = {
    Product.ZENKO: 'zenko',
    Product.S3C: 's3c',
    Product.RING: 'ring'
}

CANONICAL_TO_PRODUCT = {
    'zenko': Product.ZENKO,
    's3c': Product.S3C,
    'ring': Product.RING
}

PRODUCT_DOC_NAME = {
    Product.ZENKO: 'Zenko',
    Product.RING: 'RING',
    Product.S3C: 'S3C',
}

class TicketType(Enum):
    BUG = 1
    IMPROVEMENT = 4
    EPIC = 10000
