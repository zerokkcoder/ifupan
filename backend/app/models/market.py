from app.models.fields import CharField, FloatField, DateField
from app.models.base import BaseModel

class AntMonitorDay(BaseModel):
    """
    股票日线数据表 (ant_monitor_day)
    """
    stock_code = CharField(null=False, help_text="股票代码", comment="股票代码")
    trade_date = DateField(null=False, help_text="交易日期", comment="交易日期")
    open = FloatField(null=True, help_text="开盘价", comment="开盘价")
    high = FloatField(null=True, help_text="最高价", comment="最高价")
    low = FloatField(null=True, help_text="最低价", comment="最低价")
    close = FloatField(null=True, help_text="收盘价", comment="收盘价")
    pre_close = FloatField(null=True, help_text="前收盘价", comment="前收盘价")
    change = FloatField(null=True, help_text="涨跌额", comment="涨跌额")
    pct_chg = FloatField(null=True, help_text="涨跌幅", comment="涨跌幅")
    vol = FloatField(null=True, help_text="成交量", comment="成交量")
    amount = FloatField(null=True, help_text="成交金额", comment="成交金额")

    class Meta:
        table_name = 'ant_monitor_day'
        table_settings = ["COMMENT='股票日线数据表 (ant_monitor_day)'"]
        indexes = (
            (('stock_code',), False),
            (('trade_date',), False),
        )

class KLineData(BaseModel):
    """
    K线数据表 (k_line_data) - 周K、月K、年K
    """
    stock_code = CharField(null=False, help_text="股票代码", comment="股票代码")
    trade_date = DateField(null=False, help_text="交易日期", comment="交易日期")
    open = FloatField(null=True, help_text="开盘价", comment="开盘价")
    high = FloatField(null=True, help_text="最高价", comment="最高价")
    low = FloatField(null=True, help_text="最低价", comment="最低价")
    close = FloatField(null=True, help_text="收盘价", comment="收盘价")
    pre_close = FloatField(null=True, help_text="前收盘价", comment="前收盘价")
    change = FloatField(null=True, help_text="涨跌额", comment="涨跌额")
    pct_chg = FloatField(null=True, help_text="涨跌幅", comment="涨跌幅")
    vol = FloatField(null=True, help_text="成交量", comment="成交量")
    amount = FloatField(null=True, help_text="成交金额", comment="成交金额")
    type = CharField(null=False, help_text="类型：W-周K, M-月K, Y-年K", comment="类型：W-周K, M-月K, Y-年K") # 'W', 'M', 'Y'

    class Meta:
        table_name = 'k_line_data'
        table_settings = ["COMMENT='K线数据表 (k_line_data) - 周K、月K、年K'"]
        indexes = (
            (('stock_code',), False),
            (('trade_date',), False),
        )
