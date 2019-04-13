import redis
from InitState import InitState

r = redis.Redis(host='redis', port=6379, password='')


r.set('Hello', 'Kiwi')

currentState = InitState(r)

while(True):
    currentState = currentState.process()
