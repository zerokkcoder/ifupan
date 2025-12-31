import datetime
from app.models.fields import CharField, FloatField, DateField, TimestampField, TextField
from app.models.base import BaseModel

class StockValuation(BaseModel):
    """
    股票估值表 (stock_valuation)
    """
    stock_code = CharField(null=False, help_text="股票代码", comment="股票代码")
    cal_date = DateField(null=False, help_text="交易日期", comment="交易日期")
    valuation_desc = TextField(null=True, help_text="估值策略", comment="估值策略")
    valuation_method = CharField(null=True, help_text="估值方法", comment="估值方法")
    valuation_formula = TextField(null=True, help_text="估值公式", comment="估值公式")
    valuation_formula_cal = TextField(null=True, help_text="估值公式计算", comment="估值公式计算")
    stock_valuation = FloatField(null=True, help_text="股票估值", comment="股票估值")
    calculation_time = TimestampField(default=datetime.datetime.now, help_text="计算时间", comment="计算时间")
    industry = CharField(null=True, help_text="行业", comment="行业")
    market_status = CharField(null=True, help_text="市场状态", comment="市场状态")
    current_price = FloatField(null=True, help_text="当前股价", comment="当前股价")
    pe_ratio = FloatField(null=True, help_text="市盈率", comment="市盈率")
    pb_ratio = FloatField(null=True, help_text="市净率", comment="市净率")
    notes = TextField(null=True, help_text="备注", comment="备注")
    create_time = TimestampField(default=datetime.datetime.now, help_text="创建时间", comment="创建时间")
    update_time = TimestampField(default=datetime.datetime.now, help_text="更新时间", comment="更新时间")

    class Meta:
        table_name = 'stock_valuation'
        table_settings = ["COMMENT='股票估值表 (stock_valuation)'"]
        indexes = (
            (('stock_code',), False),
            (('cal_date',), False),
            (('calculation_time',), False),
        )

class StockValuationResult(BaseModel):
    """
    股票估值结果表 (stock_valuation_result)
    """
    ts_code = CharField(null=False, help_text="股票代码", comment="股票代码")
    trade_date = DateField(null=False, help_text="交易日期", comment="交易日期")
    close = FloatField(null=True, help_text="收盘价", comment="收盘价")
    turnover_rate = FloatField(null=True, help_text="换手率", comment="换手率")
    turnover_rate_f = FloatField(null=True, help_text="换手率（自由流通股）", comment="换手率（自由流通股）")
    volume_ratio = FloatField(null=True, help_text="量比", comment="量比")
    pe = FloatField(null=True, help_text="市盈率", comment="市盈率")
    pe_ttm = FloatField(null=True, help_text="市盈率TTM", comment="市盈率TTM")
    pb = FloatField(null=True, help_text="市净率", comment="市净率")
    ps = FloatField(null=True, help_text="市销率", comment="市销率")
    ps_ttm = FloatField(null=True, help_text="市销率TTM", comment="市销率TTM")
    dv_ratio = FloatField(null=True, help_text="股息率", comment="股息率")
    dv_ttm = FloatField(null=True, help_text="股息率TTM", comment="股息率TTM")
    total_share = FloatField(null=True, help_text="总股本（万股）", comment="总股本（万股）")
    float_share = FloatField(null=True, help_text="流通股本（万股）", comment="流通股本（万股）")
    free_share = FloatField(null=True, help_text="自由流通股本（万股）", comment="自由流通股本（万股）")
    total_mv = FloatField(null=True, help_text="总市值（万元）", comment="总市值（万元）")
    circ_mv = FloatField(null=True, help_text="流通市值（万元）", comment="流通市值（万元）")
    notes = TextField(null=True, help_text="备注信息", comment="备注信息")
    create_time = TimestampField(default=datetime.datetime.now, help_text="创建时间", comment="创建时间")
    update_time = TimestampField(default=datetime.datetime.now, help_text="更新时间", comment="更新时间")

    class Meta:
        table_name = 'stock_valuation_result'
        table_settings = ["COMMENT='股票估值结果表 (stock_valuation_result)'"]
        indexes = (
            (('ts_code', 'trade_date'), True),
        )
