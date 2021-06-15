#!/usr/bin/env python3
import pymoos
import time
import numpy as np

class pSimIMU(pymoos.comms):

    def __init__(self, moos_community, moos_port):
        """Initiates MOOSComms, sets the callbacks and runs the loop"""
        super(pSimIMU, self).__init__()
        self.server = moos_community
        self.port = moos_port
        self.name = 'pSimIMU'

        self.set_on_connect_callback(self.__on_connect)
        self.set_on_mail_callback(self.__on_new_mail)

        self.add_active_queue('real_queue', self.on_real_message)
        self.add_message_route_to_active_queue('real_queue', 'REAL_HEADING')

        self.real_heading = 90
        self.nav_heading = 0

        self.run(self.server, self.port, self.name)
        pymoos.set_moos_timewarp(20)
        self.dt=0.01


    def __on_connect(self):
        """OnConnect callback"""
        print("Connected to", self.server, self.port,
              "under the name ", self.name)
        return (self.register('REAL_HEADING', 0))

    def __on_new_mail(self):
        """OnNewMail callback"""
        for msg in self.fetch():
            pass
        return True

    def on_real_message(self, msg):
        """Special callback for Desired"""
        if msg.key() == 'REAL_HEADING':
            self.real_heading = msg.double() # graus
        return True

    def send(self, key, value):
        self.notify(key, value, -1)

    def update(self):
        self.send('NAV_HEADING', self.nav_heading)

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
           
            self.nav_heading = self.real_heading

            self.update()
            # self.debug(dt)


def main():
    IMU = pSimIMU('localhost', 9000)
    IMU.iterate()


if __name__ == "__main__":
    main()
