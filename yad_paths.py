import os
import glob

def yad_read_configuration(user_name=None):
	if user_name is None:
		config_name = os.path.join(os.path.expanduser('~'), '.config', 'yandex-disk', 'config.cfg')
		configuration = dict()
		with open(config_name, 'r') as config:
			for line in config:
				if line.startswith('auth="'):
					configuration['auth'] = line[6:len(line)-2]
				elif line.startswith('dir="'):
					configuration['dir'] = line[5:len(line)-2]
		if configuration.has_key('dir'):
			status_name = os.path.join(configuration['dir'], '.sync', 'status')
			configuration['daemon_started'] = os.path.exists(status_name)
		return configuration

def yad_get_daemon_socket():
	temp_dirs = glob.glob('/tmp/yandex-disk*')
	return os.path.join(temp_dirs[0], 'daemon') if temp_dirs else None 

if __name__ == '__main__':
	print yad_read_configuration(None)
	print yad_get_daemon_socket()
