#!/usr/bin/env python3
import pymoos
import time
import sys
import numpy as np
import pydyna
import inhousedp
from MoosReader import MoosReader

class iDP(pymoos.comms):

    def __init__(self, moos_community, moos_port):
        """Initiates MOOSComms, sets the callbacks and runs the loop"""
        super(iDP, self).__init__()
        self.server = moos_community
        self.port = moos_port
        self.name = 'iDP'

        self.set_on_connect_callback(self.__on_connect)
        self.set_on_mail_callback(self.__on_new_mail)

        self.add_active_queue('dp_queue', self.on_dp_message)
        self.add_message_route_to_active_queue('dp_queue', 'DP_X')
        self.add_message_route_to_active_queue('dp_queue', 'DP_Y')
        self.add_message_route_to_active_queue('dp_queue', 'DP_HEADING')
        self.add_message_route_to_active_queue('dp_queue', 'DP_MODE')
        

        self.add_active_queue('nav_queue', self.on_nav_message)
        self.add_message_route_to_active_queue('nav_queue', 'NAV_X')
        self.add_message_route_to_active_queue('nav_queue', 'NAV_Y')
        self.add_message_route_to_active_queue('nav_queue', 'NAV_HEADING')
        
        file = sys.argv[1]
        params=MoosReader(file,"iDP")

        self.dp_x=0
        self.dp_y=0
        self.dp_heading=0
        self.dp_mode="off"

        self.nav_x=0
        self.nav_y=0
        self.nav_heading=0

        self.desired_rotation=0
        self.desired_rudder=0


        self.dt=0.1
        
        p3d = "Navio_L15B4_Conv.p3d"
        num = 207
        self.my_dp = inhousedp.InhouseDP("/home/lhscaldas/moos-ivp-lhscaldas/missions/DP/"+p3d, num)

        self.run(self.server, self.port, self.name)
        pymoos.set_moos_timewarp(params['MOOSTimeWarp'])


    def __on_connect(self):
        """OnConnect callback"""
        print("Connected to", self.server, self.port,
              "under the name ", self.name)
        self.notify('NAV_DEPTH', float(0), -1)
        return (self.register('DP_X', 0) and
                self.register('DP_Y', 0) and
                self.register('DP_HEADING', 0) and
                self.register('DP_MODE', 0) and
                self.register('NAV_X', 0) and
                self.register('NAV_Y', 0) and
                self.register('NAV_HEADING', 0))

    def __on_new_mail(self):
        """OnNewMail callback"""
        for msg in self.fetch():
            pass
        return True

    def on_dp_message(self, msg):
        """Special callback for Desired"""
        if msg.key() == 'DP_MODE':
            self.dp_mode= msg.string()
        elif msg.key() == 'DP_X':
            self.dp_x = msg.double()
        elif msg.key() == 'DP_Y':
            self.dp_y = msg.double()
        elif msg.key() == 'DP_HEADING':
            self.dp_heading = msg.double()
        return True

    def on_nav_message(self, msg):
        """Special callback for Sensor"""
        if msg.key() == 'NAV_X':
            self.sensor_speed = msg.double()
        elif msg.key() == 'NAV_Y':
            self.sensor_heading = msg.double()
        elif msg.key() == 'NAV_HEADING':
            self.sensor_heading = msg.double()
        return True


    def send(self, key, value):
        self.notify(key, value, -1)

    def update(self):
        self.send('DESIRED_RUDDER', self.desired_rudder)
        self.send('DESIRED_ROTATION', self.desired_rotation)

    def debug(self):
        print(" ")
        print(" ")
        print(" ")
        print("iDP Debug")
        print(f"desired rudder = {self.desired_rudder*180/np.pi}")
        print(f"desired rotation = {self.desired_rotation}")


    def iterate(self):
        dt = self.dt
        dt_fast_time = dt/pymoos.get_moos_timewarp()
        while True:
            time.sleep(dt_fast_time)
            if self.dp_mode=="on":
                # Atualiza setpoint
                self.my_dp.setreference([self.dp_x, self.dp_y, (90-self.dp_heading)*np.pi/180])

                # Iteração do inHouseDP
                my_var = self.my_dp.dostep([self.nav_x,
                                        self.nav_y,
                                        (90-self.nav_heading)*np.pi/180])
                print(my_var)

                # Atualiza atuadores
                self.desired_rotation = my_var['0'].getDemandedRps()
                self.desired_rudder = my_var['0'].getDemandedAzimuth()
                # for one_thr in my_thrusters:
                #     self.my_vessel.thrusters[one_thr].dem_rotation = my_var[one_thr].getDemandedRps()
                #     self.my_vessel.thrusters[one_thr].dem_pitch = my_var[one_thr].getDemandedPod()
                #     self.my_vessel.thrusters[one_thr].dem_angle = my_var[one_thr].getDemandedAzimuth()

                
                # atualiza as variáveis dos atuadores
                self.update()
            self.debug()


def main():
    DPcontrol = iDP('localhost', 9000)
    DPcontrol.iterate()


if __name__ == "__main__":
    main()
