import sys
import os
import argparse
from datetime import datetime

# 添加项目根目录到 python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.db.session import db
from app.models.base_data import DataDictionary
from loguru import logger

def add_or_update_config(key, value, desc=None, group='BASIC_SETTINGS'):
    """添加或更新配置项"""
    if db.is_closed():
        db.connect()
    
    try:
        # 尝试查找是否存在
        config = DataDictionary.get_or_none(DataDictionary.dict_key == key)
        
        if config:
            logger.info(f"ℹ️ 配置项 {key} 已存在，正在更新...")
            config.dict_value = str(value)
            if desc:
                config.dict_desc = desc
            if group:
                config.data_group = group
            config.update_time = datetime.now()
            config.save()
            logger.success(f"✔ 配置项 {key} 更新成功: {value}")
        else:
            logger.info(f"🆕 配置项 {key} 不存在，正在创建...")
            DataDictionary.create(
                dict_key=key,
                dict_value=str(value),
                dict_desc=desc,
                data_group=group
            )
            logger.success(f"✔ 配置项 {key} 创建成功: {value}")
            
    except Exception as e:
        logger.error(f"❌ 操作失败: {e}")
    finally:
        if not db.is_closed():
            db.close()

def list_configs():
    """列出所有配置项"""
    if db.is_closed():
        db.connect()
    
    try:
        configs = DataDictionary.select().order_by(DataDictionary.data_group, DataDictionary.dict_key)
        print(f"{'Group':<20} | {'Key':<30} | {'Value':<10} | {'Description'}")
        print("-" * 100)
        for c in configs:
            print(f"{c.data_group:<20} | {c.dict_key:<30} | {c.dict_value:<10} | {c.dict_desc}")
    finally:
        if not db.is_closed():
            db.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="配置管理工具")
    subparsers = parser.add_subparsers(dest='command', help='子命令')

    # set 命令
    parser_set = subparsers.add_parser('set', help='设置配置项')
    parser_set.add_argument('key', type=str, help='配置键')
    parser_set.add_argument('value', type=str, help='配置值')
    parser_set.add_argument('--desc', type=str, help='描述')
    parser_set.add_argument('--group', type=str, default='BASIC_SETTINGS', help='分组')

    # list 命令
    parser_list = subparsers.add_parser('list', help='列出所有配置')

    args = parser.parse_args()

    if args.command == 'set':
        add_or_update_config(args.key, args.value, args.desc, args.group)
    elif args.command == 'list':
        list_configs()
    else:
        parser.print_help()
