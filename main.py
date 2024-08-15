from game_classes.network import *
from game_classes.game import *

if __name__ == "__main__":

    print("[STARTING CLIENT]")
    server_ip = input("IP:")
    NETWORK.connect(server_ip)    
    NETWORK.ct.client_address = ""
    game = Game()
    game.run()
