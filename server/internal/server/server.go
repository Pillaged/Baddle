package server

import (
	"context"

	"github.com/Pillaged/Baddle/server/rpc"
	_ "github.com/twitchtv/twirp"
)

// Server implements the Baddle service

type Config struct {
}

var _ rpc.Baddle = &Server{}

type Server struct{}

func New(cfg *Config) *Server {
	return &Server{}
}

func (s *Server) GetWord(ctx context.Context, req *rpc.GetWordReq) (*rpc.GetWordResp, error) {
	panic("implement me")
}
