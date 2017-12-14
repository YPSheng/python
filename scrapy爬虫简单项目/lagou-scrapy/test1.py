import redis
from datetime import datetime, timedelta
import faker
import random

faker = faker.Faker('zh-CN')
r = redis.Redis()
DEADLINE = datetime.now() + timedelta(hours=1)


def exam(course,students=50):
    for i in range(students):
        name = faker.name()
        time_remaining = (DEADLINE - datetime.now()).total_seconds()
        score = '%s.%s'%(random.randint(50,100), str(time_remaining).replace('.',''))
        r.zadd(course, name, score)
def top():
    stus = r.zrevrange('English', 0, 9, withscores=True)
    for i,s in enumerate(stus):
        print(i+1, s[0], s[1])


if __name__ == '__main__':
    # exam('English',students=100)
    top()