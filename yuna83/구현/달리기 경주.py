def solution(players, callings):
    for call in callings:
        a = players.index(call)
        players[a], players[a-1] = players[a-1], players[a]
       
    return players