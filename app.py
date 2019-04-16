import redis
from States.InitState import InitState

r = redis.Redis(host='redis', port=6379, password='')

currentState = InitState(r)

while True:
    currentState = currentState.process()
