import os

class Multiplexer:
    MUX_COMMAND_PATH = "USBswitchCmd "
    curr_state = 0
    
    def switch_to_normal_mode(self):
        print("Normal mode")
    
    def swith_to_DLT_mode(self):
        print("DLT mode")
    
    def switch_to_flash_mode_gmvcu(self):
        print("USBswitchCmd 1 -# 0")
    
    def switch_to_normal_mode_gmvcu(self):
        print("USBswitchCmd 1 -# 1")
