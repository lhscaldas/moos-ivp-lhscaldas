#!/usr/bin/env python3
import pymoos
import time
import numpy as np

class pSimDVL(pymoos.comms):

    def __init__(self, moos_community, moos_port):
        """Initiates MOOSComms, sets the callbacks and runs the loop"""
        super(pSimDVL, self).__init__()
        self.server = moos_community
        self.port = moos_port
        self.name = 'pSimDVL'

        self.set_on_connect_callback(self.__on_connect)
        self.set_on_mail_callback(self.__on_new_mail)

        self.add_active_queue('real_queue', self.on_real_message)
        self.add_message_route_to_active_queue('real_queue', 'REAL_SPEED')

        self.real_speed = 0
        self.nav_speed = 0

        self.run(self.server, self.port, self.name)
        pymoos.set_moos_timewarp(20)
        self.dt=0.01


    def __on_connect(self):
        """OnConnect callback"""
        print("Connected to", self.server, self.port,
              "under the name ", self.name)
        return (self.register('REAL_SPEED', 0))

    def __on_new_mail(self):
        """OnNewMail callback"""
        for msg in self.fetch():
            pass
        return True

    def on_real_message(self, msg):
        """Special callback for Desired"""
        if msg.key() == 'REAL_SPEED':
            self.real_speed = msg.double()
        return True

    def send(self, key, value):
        self.notify(key, value, -1)

    def update(self):
        self.send('NAV_SPEED', self.nav_speed)

    def debug(self, dt):
        print(" ")
        print(" ")
        print(" ")
        print("pTrajectPID Debug")
        # print("nav_heading", self.nav_heading)
        # print("desired_heading", self.desired_heading)
        # print("SETPOINT", self.coursePID.setpoint)
        print("desired_rudder", self.desired_rudder)
        # print("heading_diff", heading_diff)
        print("dt", dt*pymoos.get_moos_timewarp())
        print(f"freq_real {1 / dt / pymoos.get_moos_timewarp()}Hz")
        print(f"freq_fast {1 / dt}Hz")


    def iterate(self):
        dt = self.dt
        dt_fast_time = dt/pymoos.get_moos_timewarp()
        while True:
            time.sleep(dt_fast_time)
           
            self.nav_speed = self.real_speed

            self.update()
            # self.debug(dt)


def main():
    DVL = pSimDVL('localhost', 9000)
    DVL.iterate()


if __name__ == "__main__":
    main()
