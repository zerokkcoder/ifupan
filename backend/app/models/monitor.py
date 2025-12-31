import datetime
from app.models.fields import CharField, IntegerField, FloatField, TimestampField, TextField
from app.models.base import BaseModel

class AntMonitorStock(BaseModel):
    """
    股票监控表 (ant_monitor_stock)
    """
    stock_name = CharField(null=True, help_text="股票名称", comment="股票名称")
    stock_code = CharField(null=False, help_text="股票代码", comment="股票代码")
    stock_plates = CharField(null=True, help_text="股票板块", comment="股票板块")
    stock_final_point = IntegerField(null=True, help_text="股票积分", comment="股票积分")
    stock_focus_level = IntegerField(null=True, help_text="股票关注等级", comment="股票关注等级")
    stock_risk_level = IntegerField(null=True, help_text="股票风险等级", comment="股票风险等级")
    monitor_current_price = FloatField(null=True, help_text="当前价格", comment="当前价格")
    monitor_day_ratio = FloatField(null=True, help_text="最新涨幅", comment="最新涨幅")
    monitor_volume = FloatField(null=True, help_text="成交量", comment="成交量")
    stock_status = IntegerField(null=True, help_text="股票状态", comment="股票状态")
    stock_category = IntegerField(null=True, help_text="股票分类", comment="股票分类")
    stock_tag = TextField(null=True, help_text="打标标签", comment="打标标签")
    stock_next_advice = TextField(null=True, help_text="股票后续建议", comment="股票后续建议")
    month_up_day = IntegerField(null=True, help_text="30交易日内上涨天数", comment="30交易日内上涨天数")
    week_up_day = IntegerField(null=True, help_text="本周上涨天数", comment="本周上涨天数")
    other_info = TextField(null=True, help_text="其他信息", comment="其他信息")
    modified_date = TimestampField(default=datetime.datetime.now, help_text="上传更新时间", comment="上传更新时间")
    last_cal_date = TimestampField(default=datetime.datetime.now, help_text="最后计算时间", comment="最后计算时间")

    class Meta:
        table_name = 'ant_monitor_stock'
        table_settings = ["COMMENT='股票监控表 (ant_monitor_stock)'"]
        indexes = (
            (('stock_code',), False),
            (('stock_status',), False),
            (('stock_category',), False),
        )

class AntMonitorTag(BaseModel):
    """
    股票标签表 (ant_monitor_tag)
    """
    tag_name = CharField(null=False, help_text="标签名称", comment="标签名称")
    tag_code = CharField(unique=True, null=False, help_text="标签代码", comment="标签代码")
    tag_group = CharField(null=False, help_text="标签分组", comment="标签分组")
    tag_status = IntegerField(default=1, null=True, help_text="标签状态", comment="标签状态")
    tag_weight = FloatField(default=1.0, null=True, help_text="标签权重", comment="标签权重")
    tag_ratio = FloatField(default=0.0, null=True, help_text="标签比例", comment="标签比例")
    created_at = TimestampField(default=datetime.datetime.now, help_text="创建时间", comment="创建时间")
    updated_at = TimestampField(default=datetime.datetime.now, help_text="更新时间", comment="更新时间")

    class Meta:
        table_name = 'ant_monitor_tag'
        table_settings = ["COMMENT='股票标签表 (ant_monitor_tag)'"]

class AntMonitorSystem(BaseModel):
    """
    股票监控系统表 (ant_monitor_system)
    """
    stock_code = CharField(null=False, help_text="股票代码", comment="股票代码")
    stock_version = CharField(null=False, help_text="股票版本", comment="股票版本")
    type = CharField(null=False, help_text="类型", comment="类型")
    status = CharField(null=False, help_text="状态", comment="状态")
    target_price = FloatField(null=True, help_text="目标价格", comment="目标价格")
    target_ratio = FloatField(null=True, help_text="目标比例", comment="目标比例")
    monitor_start_price = FloatField(null=True, help_text="监控开始价格", comment="监控开始价格")
    monitor_current_price = FloatField(null=True, help_text="监控当前价格", comment="监控当前价格")
    monitor_end_price = FloatField(null=True, help_text="监控结束价格", comment="监控结束价格")
    monitor_current_ratio = FloatField(null=True, help_text="监控当前比例", comment="监控当前比例")
    stock_current_number = IntegerField(null=True, help_text="股票当前数量", comment="股票当前数量")
    stock_max_number = IntegerField(null=True, help_text="股票最大数量", comment="股票最大数量")
    stock_advice_number = IntegerField(null=True, help_text="股票建议数量", comment="股票建议数量")
    summary_point = FloatField(null=True, help_text="总结得分", comment="总结得分")
    reason = TextField(null=True, help_text="原因", comment="原因")
    summary = TextField(null=True, help_text="总结", comment="总结")
    create_time = TimestampField(default=datetime.datetime.now, help_text="创建时间", comment="创建时间")
    update_time = TimestampField(default=datetime.datetime.now, help_text="更新时间", comment="更新时间")

    class Meta:
        table_name = 'ant_monitor_system'
        table_settings = ["COMMENT='股票监控系统表 (ant_monitor_system)'"]

class AntMonitorSystemRecord(BaseModel):
    """
    股票监控系统记录表 (ant_monitor_system_record)
    """
    recordId = CharField(null=True, help_text="记录ID", comment="记录ID")
    stock_code = CharField(null=True, help_text="股票代码", comment="股票代码")
    log = TextField(null=True, help_text="日志内容", comment="日志内容")
    image = TextField(null=True, help_text="镜像信息", comment="镜像信息")
    type = CharField(null=True, help_text="类型（自动/建仓/清仓/手动日志/归档）", comment="类型（自动/建仓/清仓/手动日志/归档）")
    price = FloatField(null=True, help_text="当天收盘股价", comment="当天收盘股价")
    current_ratio = FloatField(null=True, help_text="当天盈利金额", comment="当天盈利金额")
    create_time = TimestampField(default=datetime.datetime.now, help_text="创建时间", comment="创建时间")
    update_time = TimestampField(default=datetime.datetime.now, help_text="更新时间", comment="更新时间")
    date_version = CharField(null=True, help_text="日期版本 (yyyyMMdd)", comment="日期版本 (yyyyMMdd)")

    class Meta:
        table_name = 'ant_monitor_system_record'
        table_settings = ["COMMENT='股票监控系统记录表 (ant_monitor_system_record)'"]
