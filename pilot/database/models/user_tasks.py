from database.config import DATABASE_TYPE
from database.models.components.progress_step import ProgressStep
from database.models.components.sqlite_middlewares import JSONField
from playhouse.postgres_ext import BinaryJSONField




class UserTasks(ProgressStep):
    user_tasks = BinaryJSONField() if DATABASE_TYPE == 'postgres' else JSONField()
    class Meta:
        table_name = 'user_tasks'
