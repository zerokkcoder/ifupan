import datetime
from app.models.fields import CharField, DateField, TimestampField, TextField
from app.models.base import BaseModel

class AntNewsSearchRecord(BaseModel):
    """
    新闻搜索记录表 (ant_news_search_record)
    """
    search_date = DateField(default=datetime.date.today, help_text="搜索日期", comment="搜索日期")
    record_type = CharField(null=False, help_text="类型（资讯、新闻、分析等）", comment="类型（资讯、新闻、分析等）")
    sub_type = CharField(null=True, help_text="小类（科技、金融、医药等）", comment="小类（科技、金融、医药等）")
    search_query = TextField(null=True, help_text="搜索关键词/查询内容", comment="搜索关键词/查询内容")
    json_data = TextField(null=False, help_text="JSON数据内容", comment="JSON数据内容")
    source = CharField(null=True, help_text="数据来源（PPLX、Kimi等）", comment="数据来源（PPLX、Kimi等）")
    status = CharField(default='active', help_text="状态（active、archived、deleted）", comment="状态（active、archived、deleted）")
    created_at = TimestampField(default=datetime.datetime.now, help_text="创建时间", comment="创建时间")
    updated_at = TimestampField(default=datetime.datetime.now, help_text="更新时间", comment="更新时间")

    class Meta:
        table_name = 'ant_news_search_record'
        table_settings = ["COMMENT='新闻搜索记录表 (ant_news_search_record)'"]
        indexes = (
            (('search_date', 'record_type'), False),
        )
