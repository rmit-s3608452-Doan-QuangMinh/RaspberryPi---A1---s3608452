import sys
sys.path.insert(0,'/home/pi/RaspberryPi---A1---s3608452/CalibrateTemperature')

from sense_hat import SenseHat
import bluetooth
import regisdevice_db_manager
import calibrate_temperature

db_path = '/home/pi/RaspberryPi---A1---s3608452/BluetoothDetection/RegisteredDevicesDB/registered_devices.db'
db = regisdevice_db_manager.RegisteredDevicesDatabase(db_path)

def detect_nearby_registered_devices():
    s=SenseHat()
    registered_devices = db.getAllDevices()
    print("Scanning...")
    while True:
        nearby_devices = bluetooth.discover_devices()
        for mac_address in nearby_devices:
            for row in registered_devices:
                if mac_address == row[1]:
                    temp = round(calibrate_temperature.actual_temperature(),1)
                    s.show_message("Hi {}! Current Temperature is {}'C".format(row[0],temp),scroll_speed = 0.08)

detect_nearby_registered_devices()

