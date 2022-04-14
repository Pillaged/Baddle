Builds on MAC OS
GOOS=linux GOARCH=amd64 go build -o baddle_server .

Build on windows
set "GOOS=linux" && set "GOARCH=amd64" && go build -o baddle_server .

ssh -i "baddle.pem" ?????

scp -i "baddle.pem" baddle_server ??????

chmod -R 700 baddle_server
./baddle_server

localhost:2441

