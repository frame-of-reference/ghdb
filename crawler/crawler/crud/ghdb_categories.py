from crawler.crud.base import CRUDBase
from crawler.models.ghdb_categories import Ghdb_Categories
from crawler.schemas.ghdb_categories import GhdbCategoriesCreate, GhdbCategoriesUpdate


class CRUDItem(CRUDBase[Ghdb_Categories, GhdbCategoriesCreate, GhdbCategoriesUpdate]):
    pass


ghdb_categories = CRUDItem(Ghdb_Categories)
