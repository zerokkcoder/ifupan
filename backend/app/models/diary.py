import datetime
from app.models.fields import CharField, IntegerField, TimestampField, TextField
from app.models.base import BaseModel

class AntMonitorDiary(BaseModel):
    """
    监控日记表 (ant_monitor_diary)
    """
    code = CharField(null=True, help_text="日记编码", comment="日记编码")
    create_date = TimestampField(default=datetime.datetime.now, help_text="创建日期", comment="创建日期")
    basic_info = TextField(null=True, help_text="基本信息 (JSON)", comment="基本信息 (JSON)")
    focus_stock = TextField(null=True, help_text="关注股票 (JSON数组)", comment="关注股票 (JSON数组)")
    focus_plate = TextField(null=True, help_text="关注板块 (JSON数组)", comment="关注板块 (JSON数组)")
    result_diary = TextField(null=True, help_text="结果日记 (JSON对象)", comment="结果日记 (JSON对象)")
    result_analysis = TextField(null=True, help_text="结果分析 (JSON对象)", comment="结果分析 (JSON对象)")
    result_stock = TextField(null=True, help_text="结果股票 (JSON数组)", comment="结果股票 (JSON数组)")
    result_plate = TextField(null=True, help_text="结果板块 (JSON数组)", comment="结果板块 (JSON数组)")
    today_tag = TextField(null=True, help_text="今日标签 (JSON数组)", comment="今日标签 (JSON数组)")
    today_news = TextField(null=True, help_text="今日新闻 (JSON数组)", comment="今日新闻 (JSON数组)")

    class Meta:
        table_name = 'ant_monitor_diary'
        table_settings = ["COMMENT='监控日记表 (ant_monitor_diary)'"]
        indexes = (
            (('code',), False),
            (('create_date',), False),
        )

class AntMonitorPlate(BaseModel):
    """
    监控板块表 (ant_monitor_plate)
    """
    date_version = CharField(null=True, help_text="日期版本 (yyyyMMdd)", comment="日期版本 (yyyyMMdd)")
    create_date = TimestampField(default=datetime.datetime.now, help_text="创建日期", comment="创建日期")
    plate_level = IntegerField(null=True, help_text="板块级别", comment="板块级别")
    plate_main = CharField(null=True, help_text="主板块", comment="主板块")
    plate_main_info = TextField(null=True, help_text="主板块信息 (JSON)", comment="主板块信息 (JSON)")
    plate_other_info = TextField(null=True, help_text="其他板块信息 (JSON)", comment="其他板块信息 (JSON)")
    stock_main = CharField(null=True, help_text="主股票", comment="主股票")
    stock_main_info = TextField(null=True, help_text="主股票信息 (JSON)", comment="主股票信息 (JSON)")
    stock_other_info = TextField(null=True, help_text="其他股票信息 (JSON)", comment="其他股票信息 (JSON)")
    cycle_day = IntegerField(null=True, help_text="周期天数", comment="周期天数")

    class Meta:
        table_name = 'ant_monitor_plate'
        table_settings = ["COMMENT='监控板块表 (ant_monitor_plate)'"]
        indexes = (
            (('date_version',), False),
            (('create_date',), False),
        )

class AntMonitorPlateLink(BaseModel):
    """
    监控板块关联表 (ant_monitor_plate_link)
    """
    plate_name = CharField(null=True, help_text="板块名称", comment="板块名称")
    plate_link_stock = CharField(null=True, help_text="关联股票代码", comment="关联股票代码")
    last_popular_date = TimestampField(null=True, help_text="最后热门日期", comment="最后热门日期")
    cycle_day = IntegerField(null=True, help_text="周期天数", comment="周期天数")
    create_date = TimestampField(default=datetime.datetime.now, help_text="创建日期", comment="创建日期")
    modified_date = TimestampField(default=datetime.datetime.now, help_text="修改日期", comment="修改日期")

    class Meta:
        table_name = 'ant_monitor_plate_link'
        table_settings = ["COMMENT='监控板块关联表 (ant_monitor_plate_link)'"]
        indexes = (
            (('plate_name',), False),
            (('plate_link_stock',), False),
        )
