package game

import (
	"fmt"
	"sync"
)

type Game struct {
	rooms map[string]*Room
	lock  sync.Mutex
}

type Room struct {
	playerLost     bool
	playerOne      string
	playerOneWords []string
	playerTwo      string
	playerTwoWords []string
	lock           sync.Mutex
}

func New() *Game {
	return &Game{
		rooms: map[string]*Room{},
		lock:  sync.Mutex{},
	}
}

func (g *Game) GetRoom(roomId string) *Room {
	g.lock.Lock()
	defer g.lock.Unlock()

	return g.rooms[roomId]
}

func (g *Game) CreateRoom(roomId string) *Room {
	g.lock.Lock()
	defer g.lock.Unlock()

	if g.rooms[roomId] == nil {
		g.rooms[roomId] = &Room{}
	}
	return g.rooms[roomId]
}

func (g *Game) JoinRoom(roomId string, userId string) error {
	room := g.CreateRoom(roomId)
	room.lock.Lock()
	defer room.lock.Unlock()

	if room.playerOne == "" {
		room.playerOne = userId
		return nil
	}

	if room.playerTwo == "" {
		room.playerTwo = userId
		return nil
	}

	return fmt.Errorf("room: %s already filled", roomId)
}

func (g *Game) GetOpponentWords(roomId string, userId string) ([]string, error) {
	room := g.GetRoom(roomId)
	if userId == room.playerOne {
		room.lock.Lock()
		defer room.lock.Unlock()

		opponentWords := make([]string, len(room.playerTwoWords))
		copy(opponentWords, room.playerTwoWords)
		return opponentWords, nil
	}

	if userId == room.playerTwo {
		room.lock.Lock()
		defer room.lock.Unlock()

		opponentWords := make([]string, len(room.playerTwoWords))
		copy(opponentWords, room.playerOneWords)
		return opponentWords, nil
	}

	return nil, fmt.Errorf("room: %s does not have user: %s", roomId, userId)
}
