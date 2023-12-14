import os
from datetime import datetime

class Logger:
    def __init__(self, log_dir):
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        log_filename = f"logfile_{timestamp}.txt"
        self.log_file = os.path.join(log_dir, log_filename)
        self.file = open(self.log_file, 'a')

    def _get_time_atual(self):
        return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def info(self, message):
        log_entry = f"{self._get_time_atual()} / INFO / {message}\n"
        self.file.write(log_entry)

    def error(self, message):
        log_entry = f"{self._get_time_atual()} / ERROR / {message}\n"
        self.file.write(log_entry)

    def close(self):
        self.file.close()

