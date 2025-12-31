import datetime
from app.models.fields import CharField, IntegerField, TimestampField, TextField
from app.models.base import BaseModel

class AntRiskAssessment(BaseModel):
    """
    风险评估表 (ant_risk_assessment)
    """
    stock_code = CharField(unique=True, null=False, help_text="股票代码", comment="股票代码")
    create_time = TimestampField(default=datetime.datetime.now, help_text="创建时间", comment="创建时间")
    description = TextField(null=True, help_text="风险描述", comment="风险描述")
    risk_type = CharField(null=True, help_text="风险类型", comment="风险类型")
    risk_level = IntegerField(default=0, null=True, help_text="风险等级 (0-10)", comment="风险等级 (0-10)")
    stock_hold_ratio = IntegerField(null=True, help_text="持股建议比例", comment="持股建议比例")
    future_action = TextField(null=True, help_text="后期操作", comment="后期操作")
    stock_tag_code = CharField(null=True, help_text="匹配标签", comment="匹配标签")
    stock_tag_desc = TextField(null=True, help_text="匹配标签描述", comment="匹配标签描述")
    final_point = IntegerField(null=True, help_text="最终总得分", comment="最终总得分")

    class Meta:
        table_name = 'ant_risk_assessment'
        table_settings = ["COMMENT='风险评估表 (ant_risk_assessment)'"]

class AntRiskAssessmentItem(BaseModel):
    """
    风险评估明细表 (ant_risk_assessment_item)
    """
    stock_code = CharField(null=False, help_text="股票代码", comment="股票代码")
    create_time = TimestampField(default=datetime.datetime.now, help_text="创建时间", comment="创建时间")
    description = TextField(null=True, help_text="风险描述", comment="风险描述")
    risk_type = CharField(null=True, help_text="风险类型", comment="风险类型")
    risk_level = IntegerField(default=0, null=True, help_text="风险等级", comment="风险等级")
    stock_tag_code = CharField(null=True, help_text="匹配标签", comment="匹配标签")
    strategy_code = CharField(null=False, help_text="策略代码", comment="策略代码")
    strategy_name = CharField(null=False, help_text="策略名称", comment="策略名称")
    strategy_group = IntegerField(null=True, help_text="策略分组 (0:风险型, 1:关注型)", comment="策略分组 (0:风险型, 1:关注型)")
    strategy_type = CharField(null=True, help_text="策略类型", comment="策略类型")
    analysis_day = IntegerField(null=True, help_text="分析天数", comment="分析天数")
    strategy_level = IntegerField(null=True, help_text="策略等级", comment="策略等级")

    class Meta:
        table_name = 'ant_risk_assessment_item'
        table_settings = ["COMMENT='风险评估明细表 (ant_risk_assessment_item)'"]
        indexes = (
            (('stock_code',), False),
            (('strategy_code',), False),
        )

class AntRiskSystemAssessment(BaseModel):
    """
    系统风险评估表 (ant_risk_system_assessment)
    """
    stock_code = CharField(null=False, help_text="股票代码", comment="股票代码")
    system_id = IntegerField(default=0, null=True, help_text="系统ID", comment="系统ID")
    create_version = CharField(default='', null=False, help_text="创建版本", comment="创建版本")
    create_time = TimestampField(default=datetime.datetime.now, help_text="创建时间", comment="创建时间")
    description = TextField(default='', null=True, help_text="描述", comment="描述")
    risk_type = CharField(default='未知风险类型', null=True, help_text="风险类型", comment="风险类型")
    risk_level = IntegerField(default=0, null=True, help_text="风险等级", comment="风险等级")
    stock_tag_code = CharField(default='', null=True, help_text="股票标签代码", comment="股票标签代码")
    strategy_code = CharField(null=False, help_text="策略代码", comment="策略代码")
    strategy_name = CharField(null=False, help_text="策略名称", comment="策略名称")
    strategy_group = IntegerField(default=0, null=True, help_text="策略分组", comment="策略分组")
    strategy_type = CharField(default='', null=True, help_text="策略类型", comment="策略类型")
    analysis_day = IntegerField(default=0, null=True, help_text="分析天数", comment="分析天数")
    strategy_level = IntegerField(default=0, null=True, help_text="策略等级", comment="策略等级")
    node_point = IntegerField(null=True, help_text="节点得分", comment="节点得分")

    class Meta:
        table_name = 'ant_risk_system_assessment'
        table_settings = ["COMMENT='系统风险评估表 (ant_risk_system_assessment)'"]
