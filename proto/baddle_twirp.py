# -*- coding: utf-8 -*-
# Generated by https://github.com/verloop/twirpy/protoc-gen-twirpy.  DO NOT EDIT!
# source: proto/baddle.proto

from google.protobuf import symbol_database as _symbol_database

from twirp.base import Endpoint
from twirp.server import TwirpServer
from twirp.client import TwirpClient

_sym_db = _symbol_database.Default()

class BaddleServer(TwirpServer):

	def __init__(self, *args, service, server_path_prefix="/twirp"):
		super().__init__(service=service)
		self._prefix = F"{server_path_prefix}/Baddle"
		self._endpoints = {
			"GetWord": Endpoint(
				service_name="Baddle",
				name="GetWord",
				function=getattr(service, "GetWord"),
				input=_sym_db.GetSymbol("GetWordReq"),
				output=_sym_db.GetSymbol("GetWordResp"),
			),
			"GetGameState": Endpoint(
				service_name="Baddle",
				name="GetGameState",
				function=getattr(service, "GetGameState"),
				input=_sym_db.GetSymbol("GetGameStateReq"),
				output=_sym_db.GetSymbol("GetGameStateResp"),
			),
			"JoinRoom": Endpoint(
				service_name="Baddle",
				name="JoinRoom",
				function=getattr(service, "JoinRoom"),
				input=_sym_db.GetSymbol("JoinRoomReq"),
				output=_sym_db.GetSymbol("JoinRoomResp"),
			),
			"Lose": Endpoint(
				service_name="Baddle",
				name="Lose",
				function=getattr(service, "Lose"),
				input=_sym_db.GetSymbol("LoseReq"),
				output=_sym_db.GetSymbol("LoseResp"),
			),
		}

class BaddleClient(TwirpClient):

	def GetWord(self, *args, ctx, request, server_path_prefix="/twirp", **kwargs):
		return self._make_request(
			url=F"{server_path_prefix}/Baddle/GetWord",
			ctx=ctx,
			request=request,
			response_obj=_sym_db.GetSymbol("GetWordResp"),
			**kwargs,
		)

	def GetGameState(self, *args, ctx, request, server_path_prefix="/twirp", **kwargs):
		return self._make_request(
			url=F"{server_path_prefix}/Baddle/GetGameState",
			ctx=ctx,
			request=request,
			response_obj=_sym_db.GetSymbol("GetGameStateResp"),
			**kwargs,
		)

	def JoinRoom(self, *args, ctx, request, server_path_prefix="/twirp", **kwargs):
		return self._make_request(
			url=F"{server_path_prefix}/Baddle/JoinRoom",
			ctx=ctx,
			request=request,
			response_obj=_sym_db.GetSymbol("JoinRoomResp"),
			**kwargs,
		)

	def Lose(self, *args, ctx, request, server_path_prefix="/twirp", **kwargs):
		return self._make_request(
			url=F"{server_path_prefix}/Baddle/Lose",
			ctx=ctx,
			request=request,
			response_obj=_sym_db.GetSymbol("LoseResp"),
			**kwargs,
		)
