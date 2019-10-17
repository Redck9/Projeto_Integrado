def tally(rows):
    teams = {}
    for result in rows:
        analyze_result(result, teams)

    teams_sorted = sorted(teams.values(), key =lambda team: (-team.p, team.name))
    teams_str = [str(team) for team in teams_sorted]
    teams_str.insert(0, 'Team                           | MP |  W |  D |  L |  P')

    return teams_str

name_length = 31

class team:
    def __init__(self, name):
        self.name = name
        self.mp = 0
        self.w = 0
        self.d = 0 
        self.l = 0
        self.p = 0

    def __str__(self):
        return f"{self.name}{' '*(name_length-len(self.name))}|  {str(self.mp)} |  {str(self.w)} |  {str(self.d)} |  {str(self.l)} |  {str(self.p)}"
        
    def win(self):
        self.mp += 1
        self.w += 1
        self.p += 3

    def draw(self):
        self.mp += 1
        self.d += 1
        self.p += 1

    def loss(self):
        self.mp += 1
        self.l += 1

def analyze_result(result, teams):
    result_split = result.split(';')
    team1 = teams.setdefault(result_split[0], team(result_split[0]))
    team2 = teams.setdefault(result_split[1], team(result_split[1]))
    if result_split[2] == 'win':
        team1.win()
        team2.loss()
    elif result_split[2] == 'draw':
        team1.draw()
        team2.draw()
    else:
        team1.loss()
        team2.win()