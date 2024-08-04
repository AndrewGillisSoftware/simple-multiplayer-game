from game_classes.network import *
from game_classes.game import *

if __name__ == "__main__":

    print("[STARTING CLIENT]")
    server_ip = "25.63.61.91" #input("IP:")
    NETWORK.connect(server_ip)    
    NETWORK.ct.client_address = "25.3.36.205"
    game = Game()
    game.run()
