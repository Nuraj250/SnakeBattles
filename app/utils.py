def assign_room(players_online, max_players_per_room=4):
    """Assigns a room based on current players online"""
    for room, players in players_online.items():
        if len(players) < max_players_per_room:
            return room
    return f"room_{len(players_online)+1}"
