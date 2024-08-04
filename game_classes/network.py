from game_classes.globals import *
from gilly_network_stack.client_api import *

#TODO set __ct.server_active_clients[0] to be the host
class Network:
    __inbox:MailParcel = []
    ct:ClientTransport = ClientTransport()

    def __init__(self):
       pass

    def connect(self, internet_protocal_address):
        self.ct.connect(internet_protocal_address)

        # Start Checking for mail
        networking_thread = threading.Thread(target=self.__net_work)
        networking_thread.start()
        finding_players_thread = threading.Thread(target=self.__find_players)
        finding_players_thread.start()
        
    
    def __find_players(self):
        while True:
            self.ct.request_active_clients()
            print("REQUESTING")
            time.sleep(5)
            
    
    def broadcast_event(self, id, event): 
        try:
            ips_to_send_to = self.ct.server_active_clients.remove(self.ct.client_address)
            self.ct.broadcast_parcel(id, ips_to_send_to, event)
        except:
            #print("awaiting active clients")
            pass

    def get_mail(self):
        if len(self.__inbox) == 0:
            return None
        print("GET MAIL IN NETWORK.PY RECIEVED MAIL:")
        print(f"{self.__inbox}")
        return self.__inbox[0]            

    def pop_mail(self):
        if len(self.__inbox) == 0:
            return 
        
        self.__inbox.pop(0)
        return       

    def __net_work(self):
        while(True):
            if self.ct.connected: 
                self.ct.listen() #populate CT buffers

            parcel = self.ct.next_parcel() #recieves parcel if all partials are here

            if parcel:
                print(str(parcel))
                self.__inbox.append(parcel)

            if len(self.ct.server_active_clients) > 0:
                print(self.ct.server_active_clients)

NETWORK = Network()
