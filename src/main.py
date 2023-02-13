import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from CreateTeam import CreateTeam
from FakeTeamRepository import FakeTeamRepository
from GetPlayers import GetPlayers
from GetTeams import GetTeams

from controller.http.teams import TeamController
from FakePlayerRepository import FakePlayerRepository

from FastApiServer import FastApiServer
from controller.http.players import PlayerController

app = FastAPI()

# Allow CORS connections from all origins
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

server = FastApiServer()

player_fake_data = FakePlayerRepository()
team_fake_data = FakeTeamRepository()
get_players = GetPlayers(player_data=player_fake_data)
create_team = CreateTeam(team_data=team_fake_data)
get_teams = GetTeams(team_data=team_fake_data)

playerController = PlayerController(httpServer=server, getPlayers=get_players)
teamController = TeamController(
    createTeam=create_team, getTeams=get_teams, httpServer=server
)

app.include_router(server.router)


def main(port: int):
    uvicorn.config.LOGGING_CONFIG["formatters"]["default"][
        "fmt"
    ] = "%(asctime)s %(levelprefix)s %(message)s"
    uvicorn.config.LOGGING_CONFIG["formatters"]["access"]["fmt"] = (
        "%(asctime)s "
        "%(levelprefix)s %(client_addr)s "
        '- "%(request_line)s" %(status_code)s'
    )

    uvicorn.run("main:app", host="localhost", port=port, log_level="info", reload=True)


if __name__ == "__main__":
    port = 5001
    main(port)
