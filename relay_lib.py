import os

class Relay:
    MAX_PIN = 8

    def __init__(self) -> None:
        self.relay_command_path = "./USBLRB 0 "
        self.curr_state = 0
        self.pins = { f'pin{i}' : i for i in range(1, self.MAX_PIN + 1)}

    def print_config(self) -> None:
        print("========= RELAY CONFIG =========")
        print(f"|* Relay's path: {self.relay_command_path}")
        print(f"|* Max pins: {self.MAX_PIN}")
        print(f"|* Pins detail: {self.pins}")
        print(f"|* Current state: {bin(self.curr_state)[2:]}")
        print("============= END ==============")

    def debug_log_curr_state(self):
        print(f"Current state: {self.curr_state} ({bin(self.curr_state)[2:]})")

    # Set bit of relay_pos to 1
    def enablePin(self, relay_pos):
        self.curr_state = self.curr_state | (1 << (relay_pos - 1))
        # relay_command = self.relay_command_path + str(self.curr_state)
        # os.system(relay_command)
        self.debug_log_curr_state()
    
    # Set bit of relay_pos to 0
    def disablePin(self, relay_pos):
        self.curr_state = self.curr_state & ~ (1 << (relay_pos - 1))
        # relay_command = self.relay_command_path + str(self.curr_state)
        # os.system(relay_command)
        self.debug_log_curr_state()

    # Given a number curr_state, check if the Kth bit of curr_state is set or not.
    def isKthBitSet(self, kth_bit):
        '''
        Input:
        * n: number
        * k: kth bit
        
        Output:
        * True: set
        * False: not set yet
        '''
        return self.curr_state & (1 << (kth_bit - 1))
    
    def disableAllPin(self):
        print("Turn off all relay pins")
        self.curr_state = 0
        # relay_command = RELAY_COMMAND_PATH + str(self.curr_state)
        # os.system(relay_command)
        self.debug_log_curr_state()
        
    def connectPin(self, pin):
        print(f"Connect pin{pin}")
        try:
            if not self.isKthBitSet(pin):
                self.enablePin(pin)
            else: pass
        except TypeError as err:
            print(f"Input pin is invalid! Error: {err}")
    
    def disconnectPin(self, pin):
        print(f"Disconnect pin{pin}")
        try:
            if self.isKthBitSet(pin):
                self.disablePin(pin)
            else: pass
        except TypeError as err:
            print(f"Input pin is invalid! Error: {err}")

if __name__ == '__main__':
    myrl = Relay()
    print(myrl.print_config())
    for i in range(1, Relay.MAX_PIN+1):
        myrl.connectPin(Relay.MAX_PIN + 1 - i)