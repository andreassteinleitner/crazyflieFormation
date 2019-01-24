"""
A script to scan for available Crazyflies and prompt their battery levels.
"""
import time
import logging

import cflib.crtp

from cflib.crazyflie import Crazyflie
from cflib.crazyflie.log import Log, LogVariable, LogConfig
from cflib.crazyflie.swarm import CachedCfFactory
from cflib.crazyflie.swarm import Swarm
from cflib.crazyflie.syncLogger import SyncLogger

def setup_logging(self, linkURI):
    # Log battery level
    self.logBatt = LogConfig("Battery", 200)
    self.logBatt.add_variable("pm.batteryLevel","float")
    self.logBatt.add_variable("pm.vbat","float")
    
    self.crazyflie.log.add_config(self.logBatt)
    
    if self.logBatt.valid:
        self.logBatt.data_received_cb.add_callback(self.print_batt_data)
        self.logBatt.start()
    else:
        logger.warning("Could not setup log configuration for stabilizer after connection!")

    
    
def print_battery_data(cf):
    logging.info("Battery level: Volts={1:.4f}, Percent={1:.4f}".format(ident, data["pm.vbat"], data["pm.batteryLevel"]))


if __name__ == '__main__':
# logging.basicConfig(level=logging.DEBUG)
# Initiate the low level drivers
    cflib.crtp.init_drivers(enable_debug_driver=False)

    factory = CachedCfFactory(rw_cache='./cache')
    with Swarm(uris, factory=factory) as swarm:
        swarm.parallel(log_battery_levels)
        
        # Set up the callback when connected
        self.crazyflie.connectSetupFinished.add_callback(self.connectSetupFinished)

        
        
        
        
        
        "For ROS: rostopic echo /crazyflie/battery"
        
        """
        crazyflie-firmware/src/hal/src/pm_stm32f4.c:
        
        LOG_GROUP_START(pm)
        LOG_ADD(LOG_FLOAT, vbat, &batteryVoltage)
        LOG_ADD(LOG_UINT16, vbatMV, &batteryVoltageMV)
        LOG_ADD(LOG_FLOAT, extVbat, &extBatteryVoltage)
        LOG_ADD(LOG_UINT16, extVbatMV, &extBatteryVoltageMV)
        LOG_ADD(LOG_FLOAT, extCurr, &extBatteryCurrent)
        LOG_ADD(LOG_FLOAT, chargeCurrent, &pmSyslinkInfo.chargeCurrent)
        LOG_ADD(LOG_INT8, state, &pmState)
        LOG_ADD(LOG_UINT8, batteryLevel, &batteryLevel)
        LOG_GROUP_STOP(pm)
        """