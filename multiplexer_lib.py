import os

class Multiplexer:
    def __init__(self) -> None:    
        self.mux_command_path = "USBswitchCmd "
    
    def switch_to_normal_mode(self):
        print("Normal mode")
    
    def switch_to_flashing_mode(self):
        print("Flashing mode")

    def swith_to_DLT_mode(self):
        print("DLT mode")
    
    def switch_to_flash_mode_gmvcu(self):
        print("USBswitchCmd 1 -# 0")
    
    def switch_to_normal_mode_gmvcu(self):
        print("USBswitchCmd 1 -# 1")

