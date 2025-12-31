import datetime
from app.models.fields import CharField, TimestampField, TextField
from app.models.base import BaseModel

class AutomationOperationLog(BaseModel):
    """
    自动化操作日志表 (automation_operation_log)
    """
    execution_time = TimestampField(default=datetime.datetime.now, help_text="执行时间", comment="执行时间")
    execution_type = CharField(null=False, help_text="执行类型", comment="执行类型")
    execution_content = TextField(null=False, help_text="执行内容", comment="执行内容")
    execution_module = CharField(null=False, help_text="执行模块", comment="执行模块")
    create_time = TimestampField(default=datetime.datetime.now, help_text="创建时间", comment="创建时间")
    update_time = TimestampField(default=datetime.datetime.now, help_text="更新时间", comment="更新时间")

    class Meta:
        table_name = 'automation_operation_log'
        table_settings = ["COMMENT='自动化操作日志表 (automation_operation_log)'"]
