import json
import sys
import redis
import logging
from .pipelines import MysqlPipeline

logger = logging.getLogger()


r = redis.Redis()
def get_item(spider):
    key = '%s:items' % spider
    #堵塞，有值就执行
    item = r.blpop(key)
    if item:
        return json.loads(item[1])


if __name__ == "__main__":
    if len(sys.argv) < 2:
        logger.warning('need spider name')
    spider = sys.argv[1]
    logger.info("start")
    db = MysqlPipeline()
    db.open_spider(spider)
    item = get_item(spider)
    while item:
        db.process_item(item,spider)
        item = get_item(spider)
    db.close_spider(spider)