class Clampy:
    def __init__(self):
        self.DEBUG = False
        self.HANDLE_EXCEPTIONS = True 
        self.REROUTE_404_TO_HOME = False
        self.APP_ROUTE = "/"
        self.REROUTE_404 = self.APP_ROUTE
        self.SERVER_NAME = "Clam.py Server"
        self.SERVER_PORT = 2080
    def run(self):
        print(f"Attempting to start \"{self.SERVER_NAME}\" @ http://localhost:{self.SERVER_PORT}")