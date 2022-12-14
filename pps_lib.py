'''
Library for PPS
'''

class PPS:
    def __init__(self) -> None:    
        self._volt_idx = 12.0
        self._curr_idx = 2.3
        self._channel = "2"
        self._com_port = "12"

    def set_volt_idx(self, v: float):
        self._volt_idx = v
        print(f"[pps] set volt = {v}")
    
    def set_curr_idx(self, c: float):
        self._curr_idx = c
        print(f"[pps] set current = {c}")

    def set_channel(self, channel: str):
        self._channel = channel
        print(f"[pps] set channel = {channel}")

    def set_com_port(self, com_port: str):
        self._com_port = com_port
        print(f"[pps] set com port = {com_port}")

    def get_volt_idx(self): return self._volt_idx
    def get_curr_idx(self): return self._curr_idx
    def get_com_port(self): return self._com_port
    def get_channel(self): return self._channel

    def get_info(self):
        print(f"[pps] volt = {self._volt_idx}")
        print(f"[pps] curr = {self._curr_idx}")
        print(f"[pps] channel = {self._channel}")
        print(f"[pps] com port = {self._com_port}")

