import threading
import time
import random
from typing import List

def run_player(player_id: int) -> None:
    health = 100
    print(f"Player {player_id} entered the game with {health} HP")
    
    while health > 0:
        damage = random.randint(10, 30)
        health -= damage
        print(f"Player {player_id} took {damage} damage! Health: {health}")
        time.sleep(0.5)
    
    print(f"Player {player_id} was defeated!")

if __name__ == "__main__":
    players: List[threading.Thread] = []
    num_players = 4
    
    print("Game starting...")
    time.sleep(1)
    
    for player_id in range(1, num_players + 1):
        player = threading.Thread(target=run_player, args=(player_id,))
        players.append(player)
        player.start()
        print(f"Player {player_id} joined the battle!")
    
    for player in players:
        player.join()
    
    print("Game Over!")