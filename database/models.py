from pony.orm import PrimaryKey, Required, Database
from pony.orm import LongStr

db = Database()

class Report(db.Entity):
    id = PrimaryKey(int, auto=True)
    filename = Required(str)
    content = Required(LongStr)

class Test(db.Entity):
    id = PrimaryKey(int, auto=True)
    filename = Required(str)
    content = Required(LongStr)

class Screenshot(db.Entity):
    id = PrimaryKey(int, auto=True)
    filename = Required(str)
    content = Required(LongStr)

db.bind(provider="sqlite", filename="uy-testing.sqlite", create_db=True)
db.generate_mapping(create_tables=True)