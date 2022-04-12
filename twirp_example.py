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
<<<<<<< HEAD
=======

def join_room(user_id, rm_num):
    try:
        response = client.JoinRoom(
            ctx=Context(), request=baddle_pb2.JoinRoomReq(user=user_id, room=rm_num)
        )
        print(response)
        return response
    except TwirpServerException as e:
        print(e.code, e.message, e.meta, e.to_dict())

get_word("1","1")
join_room("1","1")
send_loss("1")
game_state_req("1","1")
print(client)
>>>>>>> a75221bfb03aa2ccd7a52468bf20648a61144604
