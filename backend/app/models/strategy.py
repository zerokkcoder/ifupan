import datetime
from app.models.fields import CharField, IntegerField, FloatField, TimestampField, TextField
from app.models.base import BaseModel

class StrategyClassInfo(BaseModel):
    """
    策略信息表 (strategy_class_info)
    """
    strategy_code = CharField(unique=True, null=False, help_text="策略代码", comment="策略代码")
    strategy_name = CharField(null=False, help_text="策略名称", comment="策略名称")
    strategy_group = IntegerField(null=False, help_text="策略分组", comment="策略分组")
    strategy_type = IntegerField(null=False, help_text="策略类型", comment="策略类型")
    analysis_day = IntegerField(null=False, help_text="分析天数", comment="分析天数")
    strategy_level = IntegerField(null=False, help_text="策略等级", comment="策略等级")
    enabled = IntegerField(default=1, null=True, help_text="是否启用", comment="是否启用")
    create_date = TimestampField(default=datetime.datetime.now, help_text="创建时间", comment="创建时间")
    update_date = TimestampField(default=datetime.datetime.now, help_text="更新时间", comment="更新时间")

    class Meta:
        table_name = 'strategy_class_info'
        table_settings = ["COMMENT='策略信息表 (strategy_class_info)'"]

class AntStrategyFound(BaseModel):
    """
    策略发现结果表 (ant_strategy_found)
    """
    stock_code = CharField(null=False, help_text="股票代码", comment="股票代码")
    stock_name = CharField(null=False, help_text="股票名称", comment="股票名称")
    stock_plates = CharField(null=True, help_text="股票板块", comment="股票板块")
    total_score = IntegerField(null=False, help_text="总得分", comment="总得分")
    risk_level = IntegerField(null=False, help_text="风险等级 (1-10)", comment="风险等级 (1-10)")
    focus_level = IntegerField(null=False, help_text="关注等级 (1-10)", comment="关注等级 (1-10)")
    latest_price = FloatField(null=True, help_text="最新股价", comment="最新股价")
    risk_assessments = TextField(null=True, help_text="风险评估结果 (JSON)", comment="风险评估结果 (JSON)")
    strategy_code = CharField(null=True, help_text="命中策略", comment="命中策略")
    create_time = TimestampField(default=datetime.datetime.now, help_text="创建时间", comment="创建时间")

    class Meta:
        table_name = 'ant_strategy_found'
        table_settings = ["COMMENT='策略发现结果表 (ant_strategy_found)'"]
        indexes = (
            (('stock_code',), False),
            (('create_time',), False),
        )

class StrategyBindSetting(BaseModel):
    """
    策略绑定设置表 (strategy_bind_setting)
    """
    stock_category = CharField(null=False, help_text="股票分类", comment="股票分类")
    stock_code = CharField(null=True, help_text="股票代码（可为空）", comment="股票代码（可为空）")
    strategies = TextField(null=True, help_text="策略列表（逗号分隔）", comment="策略列表（逗号分隔）")
    strategy_code = CharField(null=False, help_text="策略代码", comment="策略代码")
    strategy_name = CharField(null=False, help_text="策略名称", comment="策略名称")
    strategy_group = CharField(null=True, help_text="策略分组", comment="策略分组")
    strategy_type = CharField(null=True, help_text="策略类型", comment="策略类型")
    analysis_day = IntegerField(default=0, null=True, help_text="分析天数", comment="分析天数")
    strategy_level = IntegerField(default=1, null=True, help_text="策略等级", comment="策略等级")

    class Meta:
        table_name = 'strategy_bind_setting'
        table_settings = ["COMMENT='策略绑定设置表 (strategy_bind_setting)'"]
