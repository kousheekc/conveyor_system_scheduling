import subprocess

command = '"C:/Program Files/FlexSim 2023 Update 2/program/flexsim.exe" "C:/Users/koush/Documents/MRT/Flexsim/FlexSim 2023 Projects/projet/ga_optimisation/Projet_auto.fsm" /maintenance nogui_disablemsg /automated true'
subprocess.run(command, shell=True)