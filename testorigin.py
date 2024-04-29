import time
import random

from fastapi import FastAPI, Response

MAX_MB_SIZE = 10

app = FastAPI()

@app.get('/')
async def index():
    result = {'name':'test origin'}
    result['seconds_since_epoch'] = int(time.time())
    return result

@app.get('/test/{num_bytes}/bytes')
async def get_random_bytes(num_bytes:int):
    if num_bytes > MAX_MB_SIZE*1024*1024:
        return {'error': '{nmb} too big'.format(nmb=num_megabytes)}
    random.seed(int(time.time()))
    return Response(random.randbytes(num_bytes))

@app.get('/test/{num_megabytes}/MB')
async def get_random_bytes(num_megabytes:int):
    if num_megabytes > MAX_MB_SIZE:
        return {'error': '{nmb} too big'.format(nmb=num_megabytes)}
    
    random.seed(int(time.time()))
    return Response(random.randbytes(num_megabytes*1024*1024))
    
