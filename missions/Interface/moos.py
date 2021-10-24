import numpy as np
import os


def write_bhv(path,posf):
    # gen new lines
    polygon = "polygon ="
    for wp in path:
        polygon+=f" {wp[0]},{wp[1]} :"
    polygon=polygon[:-1]
    polygon+="\n"
    station_pt = f"station_pt = {posf[0]}, {posf[1]} \n"
    # find and modify lines
    text=[]
    with open("modelo.bhv", 'r') as f:
        text = f.readlines()
        for line in text:
            if "polygon" in line:
                idx=text.index(line)
                text[idx] = polygon
            if "station_pt" in line:
                idx=text.index(line)
                text[idx] = station_pt
    #  write new file
    with open("main.bhv", 'w') as f:
        f.writelines(text)

def write_moos(pos0,origem, hdg):
    # gen new lines
    LatOrigin = f"LatOrigin = {origem[0]} \n"
    LongOrigin = f"LongOrigin = {origem[1]} \n"
    START_X = f"START_X = {pos0[0]} \n"
    START_Y = f"START_Y = {pos0[1]} \n"
    START_HEADING = f"START_HEADING = {hdg} \n"
    # find and modify lines
    text=[]
    with open("modelo.moos", 'r') as f:
        text = f.readlines()
        for line in text:
            if "LatOrigin" in line:
                idx=text.index(line)
                text[idx] = LatOrigin
            if "LongOrigin" in line:
                idx=text.index(line)
                text[idx] = LongOrigin
            if "START_X" in line:
                idx=text.index(line)
                text[idx] = START_X
            if "START_Y" in line:
                idx=text.index(line)
                text[idx] = START_Y
            if "START_HEADING" in line:
                idx=text.index(line)
                text[idx] = START_HEADING
    #  write new file
    with open("main.moos", 'w') as f:
        f.writelines(text)

def run():
    cmd = 'gnome-terminal -- pAntler main.moos'
    os.system(cmd)

# if __name__ == '__main__':
#     path=[[720.0, -1230.0], [1665.0, -1425.0], [2535.0, -1470.0]]
#     pos0=[480.0, -1110.0]
#     origem=[-22.9269, -43.867]
#     write_bhv(path,pos0)
#     write_moos(pos0,origem)
#     run()