# client.py
from twirp.context import Context
from twirp.exceptions import TwirpServerException

from proto import baddle_twirp, baddle_pb2

client = baddle_twirp.BaddleClient("http://localhost:2441")

try:
    response = client.GetWord(ctx=Context(), request=baddle_pb2.GetWordReq(user="test-user"))
    print(response)
except TwirpServerException as e:
    print(e.code, e.message, e.meta, e.to_dict())