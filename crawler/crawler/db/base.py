# Import all the models, so that Base has them before being
# imported by Alembic
from crawler.db.base_class import Base  # noqa
from crawler.models.ghdb_categories import Ghdb_Categories  # noqa
from crawler.models.ghdb_queries import Ghdb_Queries  # noqa
from crawler.models.ghdb_authors import Ghdb_Authors  # noqa
from crawler.models.ghdb_authors_queries import Ghdb_Authors_Queries  # noqa
