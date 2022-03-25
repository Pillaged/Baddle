package server

import (
	"context"

	"github.com/Pillaged/Baddle/server/rpc"
	_ "github.com/twitchtv/twirp"
)

// Server implements the Baddle service

type Config struct {
	WordGetter WordGetter
}

var _ rpc.Baddle = &Server{}

type Server struct {
	wordGetter WordGetter
}

type WordGetter interface {
	GetRandomWord() string
}

func New(cfg *Config) *Server {
	return &Server{
		wordGetter: cfg.WordGetter,
	}
}

func (s *Server) GetWord(ctx context.Context, req *rpc.GetWordReq) (*rpc.GetWordResp, error) {
	return &rpc.GetWordResp{
		Word: s.wordGetter.GetRandomWord(),
	}, nil
}
