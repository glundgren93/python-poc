import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from application.create_team import CreateTeam
from application.get_players import GetPlayers
from application.get_team import GetTeam
from application.get_teams import GetTeams
from infra.controller.players import PlayerController
from infra.controller.teams import TeamController
from infra.http.fast_api_server import FastApiServer
from infra.repository.in_memory_player_repository import InMemoryPlayerRepository
from infra.repository.in_memory_team_repository import InMemoryTeamRepository



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

player_fake_data = InMemoryPlayerRepository()
team_fake_data = InMemoryTeamRepository()
get_players = GetPlayers(player_data=player_fake_data)
create_team = CreateTeam(team_data=team_fake_data)
get_teams = GetTeams(team_data=team_fake_data)
get_team = GetTeam(team_data=team_fake_data)

playerController = PlayerController(httpServer=server, getPlayers=get_players)
teamController = TeamController(
    _create_team=create_team, _get_teams=get_teams, _get_team=get_team, httpServer=server
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
