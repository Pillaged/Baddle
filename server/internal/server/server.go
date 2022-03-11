package server

import (
	"context"
	 "github.com/Pillaged/Baddle/server/rpc"
	_ "github.com/twitchtv/twirp"
)

// Server implements the Haberdasher service
var _  rpc.Baddle = &Server{}
type Server struct {}

func (s *Server) GetWord(ctx context.Context, req *rpc.GetWordReq) (*rpc.GetWordResp, error) {
	panic("implement me")
}