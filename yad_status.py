#!/usr/bin/env python

import yad_paths
from yad_connection import YadConnection

class Status(object):
    pass

class EmptyStatus(Status):
    def __init__(self, message):
        self._message = message

    def ok(self):
        return False

    def message(self):
        return self._message

def stringify_core_status(status_code):
    STATUS_NAMES = ['paused', 'idle', 'index', 'busy', 'error',
                    'photo_search', 'photo_copy', 'photo_upload']
    return STATUS_NAMES[status_code] if status_code < len(STATUS_NAMES) else 'undefined'

class DaemonStatus(Status):
    def __init__(self, config, daemon_answer):
        result = daemon_answer['result'][0]
        core = result['internet_access']
        self.core_status = core['core_status']
        self.core_status_text = stringify_core_status(self.core_status)
        if self.core_status_text == 'error':
            self.error_path = core['core_path']
            self.error_code = core['core_error']
        else:
            self.sync_dir = result['sync_dir'] if result.has_key('sync_dir') else config['dir']
            self.size_status = result['size_status'] if result.has_key('size_status') else {}
            self.quota_info = result['quota_info'] if result.has_key('quota_info') else {}

    def ok(self):
        return not hasattr(self, 'error_code')

    def message(self):
        if not self.ok():
            return 'Error: %i in file "%s"' % (self.error_code, self.error_path)
        return 'Current status: %s\nSync size: %s\nQuota info: %s' \
                % (self.core_status_text, self.size_status, self.quota_info)

def get_status():
    config = yad_paths.yad_read_configuration(None)
    if not config['daemon_started']:
        return EmptyStatus('Daemon isn\'t started.')
    socket_name = yad_paths.yad_get_daemon_socket()
    if not socket_name:
        return EmptyStatus('Can\'t connect to daemon!')
    cnn = YadConnection()
    try:
        cnn.connect(socket_name)
        status_request = {'method': 'status', 'params': None}
        answer = cnn.send_with_answer(status_request)
        return DaemonStatus(config, answer) if answer and answer['method'] == 'status' \
           else EmptyStatus('Wrong daemon answer!')
    finally:
        cnn.close()

if __name__ == '__main__':
    status = get_status()
    print status.message()

