"save cameramatrix in config format"
import configparser

def save_device_camera_matrix(config_file, mtx, dist, comment=''):
    "save the device matrix i config file"
    config = configparser.ConfigParser(allow_no_value=True)
    config.add_section("camera")
    #print("mtx", mtx)
    config.set('camera','; '+comment)
    config['camera']['fx'] = str(mtx[0][0])
    config['camera']['fy'] = str(mtx[1][1])
    config['camera']['s'] = str(mtx[1][0])
    config['camera']['cx'] = str(mtx[0][2])
    config['camera']['cy'] = str(mtx[1][2])
    config['camera']['dist0'] = str(dist[0][0])
    config['camera']['dist1'] = str(dist[0][1])
    config['camera']['dist2'] = str(dist[0][2])
    config['camera']['dist3'] = str(dist[0][3])
    config['camera']['dist4'] = str(dist[0][4])
    #print('dist',dist)

    with open(config_file, 'w', encoding="UTF8") as configfile:
        config.write(configfile)
