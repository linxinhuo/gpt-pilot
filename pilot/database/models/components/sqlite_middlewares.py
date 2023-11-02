import json
from peewee import TextField


class JSONField(TextField):
    def python_value(self, value):
        return json.loads(value) if value is not None else value

    def db_value(self, value):
        return json.dumps(value) if value is not None else value
