# client.py
from twirp.context import Context
from twirp.exceptions import TwirpServerException

from proto import baddle_twirp, baddle_pb2

client = baddle_twirp.BaddleClient("http://localhost:2441")


def get_word(user_id, rm_num):
    try:
        response = client.GetWord(
            ctx=Context(), request=baddle_pb2.GetWordReq(user=user_id)
        )
        print(response)
        return response
    except TwirpServerException as e:
        print(e.code, e.message, e.meta, e.to_dict())


def send_loss(rm_num):
    try:
        response = client.Lose(ctx=Context(), request=baddle_pb2.LoseReq(room=rm_num))
        print(response)
        return response
    except TwirpServerException as e:
        print(e.code, e.message, e.meta, e.to_dict())


def game_state_req(user_id, rm_num):
    try:
        response = client.GetGameState(
            ctx=Context(), request=baddle_pb2.GetGameStateReq(user=user_id, room=rm_num)
        )
        print(response)
        return response
    except TwirpServerException as e:
        print(e.code, e.message, e.meta, e.to_dict())
