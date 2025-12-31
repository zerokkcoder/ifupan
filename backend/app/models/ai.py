import datetime
from app.models.fields import CharField, IntegerField, TimestampField, TextField, FloatField
from app.models.base import BaseModel

class MonitorAiConfig(BaseModel):
    """
    AI 配置表 (monitor_ai_config)
    """
    config_name = CharField(unique=True, null=False, help_text="配置名称（唯一标识）", comment="配置名称（唯一标识）")
    config_desc = CharField(null=True, help_text="配置描述", comment="配置描述")
    config_type = CharField(default='general', help_text="类型：general/specific", comment="类型：general/specific")
    channel = CharField(null=False, help_text="AI渠道：openai/zhipu/kimi/qwen", comment="AI渠道：openai/zhipu/kimi/qwen")
    model_name = CharField(null=True, help_text="模型名称", comment="模型名称")
    base_url = CharField(null=True, help_text="API Base URL", comment="API Base URL")
    api_token = CharField(null=False, help_text="API Token", comment="API Token")
    prompt_config = TextField(null=True, help_text="提示词配置 (JSON)", comment="提示词配置 (JSON)")
    max_tokens = IntegerField(null=True, help_text="最大Token数", comment="最大Token数")
    temperature = FloatField(null=True, help_text="温度参数", comment="温度参数")
    top_p = FloatField(null=True, help_text="Top P参数", comment="Top P参数")
    enabled = IntegerField(default=1, help_text="是否启用", comment="是否启用")
    priority = IntegerField(default=100, help_text="优先级（数字越小优先级越高）", comment="优先级（数字越小优先级越高）")
    scene_tags = TextField(null=True, help_text="场景标签 (JSON数组)", comment="场景标签 (JSON数组)")
    extra_config = TextField(null=True, help_text="扩展配置 (JSON)", comment="扩展配置 (JSON)")
    create_time = TimestampField(default=datetime.datetime.now, help_text="创建时间", comment="创建时间")
    update_time = TimestampField(default=datetime.datetime.now, help_text="更新时间", comment="更新时间")
    last_used_time = TimestampField(null=True, help_text="最后使用时间", comment="最后使用时间")
    use_count = IntegerField(default=0, help_text="使用次数统计", comment="使用次数统计")

    class Meta:
        table_name = 'monitor_ai_config'
        table_settings = ["COMMENT='AI 配置表 (monitor_ai_config)'"]
        indexes = (
            (('enabled', 'priority'), False),
        )

class MonitorAiAgent(BaseModel):
    """
    AI 智能体编排表 (monitor_ai_agent)
    """
    agent_name = CharField(unique=True, null=False, help_text="编排名称（唯一标识）", comment="编排名称（唯一标识）")
    agent_desc = CharField(null=True, help_text="编排描述", comment="编排描述")
    agents_config = TextField(null=False, help_text="智能体配置 (JSON数组)", comment="智能体配置 (JSON数组)")
    enabled = IntegerField(default=1, help_text="是否启用", comment="是否启用")
    priority = IntegerField(default=100, help_text="优先级（数字越小优先级越高）", comment="优先级（数字越小优先级越高）")
    scene_tags = TextField(null=True, help_text="场景标签 (JSON数组)", comment="场景标签 (JSON数组)")
    extra_config = TextField(null=True, help_text="扩展配置 (JSON)", comment="扩展配置 (JSON)")
    create_time = TimestampField(default=datetime.datetime.now, help_text="创建时间", comment="创建时间")
    update_time = TimestampField(default=datetime.datetime.now, help_text="更新时间", comment="更新时间")
    last_used_time = TimestampField(null=True, help_text="最后使用时间", comment="最后使用时间")
    use_count = IntegerField(default=0, help_text="使用次数统计", comment="使用次数统计")

    class Meta:
        table_name = 'monitor_ai_agent'
        table_settings = ["COMMENT='AI 智能体编排表 (monitor_ai_agent)'"]
        indexes = (
            (('enabled', 'priority'), False),
        )
