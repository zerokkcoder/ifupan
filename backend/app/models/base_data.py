import datetime
from app.models.fields import CharField, IntegerField, DateField, TimestampField, TextField
from app.models.base import BaseModel

class BaseStockInfo(BaseModel):
    """
    股票基础信息表 (base_stock_info)
    """
    ts_code = CharField(unique=True, null=False, help_text="股票代码", comment="股票代码")
    symbol = CharField(null=False, help_text="股票简称", comment="股票简称")
    name = CharField(null=False, help_text="股票名称", comment="股票名称")
    area = CharField(null=True, help_text="所在区域", comment="所在区域")
    industry = CharField(null=True, help_text="行业分类", comment="行业分类")
    cnspell = CharField(null=True, help_text="拼音首字母", comment="拼音首字母")
    market = CharField(null=True, help_text="市场分类", comment="市场分类")
    list_date = DateField(null=True, help_text="上市日期", comment="上市日期")
    act_name = CharField(null=True, help_text="实控人名称", comment="实控人名称")
    act_ent_type = CharField(null=True, help_text="实控人企业性质", comment="实控人企业性质")
    last_data = DateField(null=True, help_text="最后刷新日期", comment="最后刷新日期")

    class Meta:
        table_name = 'base_stock_info'
        table_settings = ["COMMENT='股票基础信息表 (base_stock_info)'"]

class DataDictionary(BaseModel):
    """
    数据字典表 (data_dictionary)
    """
    dict_key = CharField(unique=True, null=False, help_text="字典键", comment="字典键")
    dict_value = CharField(null=False, help_text="字典值", comment="字典值")
    dict_desc = CharField(null=True, help_text="字典描述", comment="字典描述")
    data_group = CharField(default='BASIC_SETTINGS', null=True, help_text="数据组", comment="数据组")
    create_time = TimestampField(default=datetime.datetime.now, help_text="创建时间", comment="创建时间")
    update_time = TimestampField(default=datetime.datetime.now, help_text="更新时间", comment="更新时间")

    class Meta:
        table_name = 'data_dictionary'
        table_settings = ["COMMENT='数据字典表 (data_dictionary)'"]

class DbMetadata(BaseModel):
    """
    数据库元信息表 (db_metadata)
    """
    version = CharField(null=False, help_text="数据库版本", comment="数据库版本")
    description = CharField(null=True, help_text="版本描述", comment="版本描述")
    applied_at = TimestampField(default=datetime.datetime.now, help_text="应用时间", comment="应用时间")
    checksum = CharField(null=True, help_text="校验和", comment="校验和")

    class Meta:
        table_name = 'db_metadata'
        table_settings = ["COMMENT='数据库元信息表 (db_metadata)'"]
