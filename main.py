from game_classes.network_classes.network import *
from game_classes.game import *


if __name__ == "__main__":

    dv_print("[STARTING CLIENT]")
    server_ip = "25.0.254.69" #input("IP:")
    NETWORK.connect(server_ip)    
    NETWORK.ct.client_address = ""
    game = Game()
    game.run()
