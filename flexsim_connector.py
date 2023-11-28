import os
import subprocess

class FlexsimConnector:
    def __init__(self, file) -> None:
        self.gui_command = f'"C:/Program Files/FlexSim 2023 Update 2/program/flexsim.exe" "C:/Users/koush/Documents/MRT/Flexsim/FlexSim 2023 Projects/projet/ga_optimisation/{file}" /maintenance /automated true'
        self.nogui_command = f'"C:/Program Files/FlexSim 2023 Update 2/program/flexsim.exe" "C:/Users/koush/Documents/MRT/Flexsim/FlexSim 2023 Projects/projet/ga_optimisation/{file}" /maintenance nogui_disablemsg /automated true'            

    def simulate(self, gui=False):
        if (gui):
            subprocess.run(self.gui_command, shell=True)
        else:
            subprocess.run(self.nogui_command, shell=True)

        with open("results.txt", 'r') as file:
            file_contents = file.read()
            return float(file_contents)