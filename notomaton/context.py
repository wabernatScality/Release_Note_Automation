from collections import namedtuple

from .constants import PRODUCT_TO_NAME, PRODUCT_TO_CANONICAL, PRODUCT_DOC_NAME
from .constants import Product as _Product
from .search import do_search
from .assets import discover_images
from datetime import date
from .util.ticket import ring_to_s3c_version, trim_version

Context = namedtuple('Context', ['product', 'issues', 'style', 'images', 'is_dashboard', 'date'])

Issues = namedtuple('Issues', ['known', 'fixed', 'new_features', 'improvements'])

Product = namedtuple('Product', ['name', 'canonical', 'version', 'doc_name', 'version_short'])

RingProduct = namedtuple('RingProduct', ['name', 'canonical', 'version', 's3c_version', 'doc_name', 'version_short', 's3c_version_short'])

def build_issues(product, version):
    search = do_search(product, version)
    return Issues(
        known = tuple(search.known),
        fixed = tuple(search.fixed),
        new_features=tuple(search.new_features),
        improvements=tuple(search.improvements)
    )

def build_images():
    images = discover_images()
    nt = namedtuple('Images', list(images.keys()))
    return nt(**{ k: v.encode() for k, v in images.items()})


def _build_ring_product(product, version):
    s3c_version = ring_to_s3c_version(version)
    return RingProduct(
        name=PRODUCT_TO_NAME[product],
        canonical=PRODUCT_TO_CANONICAL[product],
        version=version,
        version_short=trim_version(version),
        s3c_version=s3c_version,
        s3c_version_short=trim_version(s3c_version),
        doc_name=PRODUCT_DOC_NAME[product]
    )

def _build_generic_product(product, version): 
    return Product(
        name=PRODUCT_TO_NAME[product],
        canonical=PRODUCT_TO_CANONICAL[product],
        version=version,
        version_short=trim_version(version),
        doc_name=PRODUCT_DOC_NAME[product]

    )

def build_context(product, version, dashboard=False):
    if product == _Product.RING:
        _product = _build_ring_product(product, version)  
    else:
        _product = _build_generic_product(product, version)

    return Context(
        style=None, # Will be injected later
        product = _product,
        issues = build_issues(product, version),
        images = build_images(),
        is_dashboard=dashboard,
        date=date.today().strftime('%-d %B, %Y')
    )
