import os
import psutil
import rumps

class SystemMonitorApp(rumps.App):
    def __init__(self):
        super(SystemMonitorApp, self).__init__("System Monitor")
        self.cpu_status = rumps.MenuItem("CPU: --")
        self.ram_status = rumps.MenuItem("RAM: --")
        self.cpu_temp_status = rumps.MenuItem("CPU Temp: --")
        self.gpu_temp_status = rumps.MenuItem("GPU Temp: --")
        self.fan_status = rumps.MenuItem("Fan: --")

        self.menu = [self.cpu_status, self.ram_status, self.cpu_temp_status, self.gpu_temp_status, self.fan_status]

        self.update_status()
        self.timer = rumps.Timer(self.update_status, 2)
        self.timer.start()

    def update_status(self, _=None):
        cpu_percent = psutil.cpu_percent()
        memory_info = psutil.virtual_memory()
        memory_percent = memory_info.percent
        cpu_temp = self.get_info('CPU die temperature')
        gpu_temp = self.get_info('GPU die temperature')
        fan_speed = self.get_info('Fan')

        self.title = f"{cpu_percent}% | {memory_percent}% | {cpu_temp}°C | {gpu_temp}°C | {fan_speed} rpm"
        self.cpu_status.title = f"CPU: {cpu_percent}%"
        self.ram_status.title = f"RAM: {memory_percent}%"
        self.cpu_temp_status.title = f"CPU Temp: {cpu_temp}°C"
        self.gpu_temp_status.title = f"GPU Temp: {gpu_temp}°C"
        self.fan_status.title = f"Fan: {fan_speed} rpm"

    def get_info(self, info_type):
        data = [each.strip() for each in (os.popen('sudo powermetrics --samplers smc -i1 -n1')).read().split('\n') if each != '']
        for line in data:
            if info_type in line:
                return line.strip(f'{info_type}: ').rstrip(' C').rstrip(' rpm')
        return f'{info_type} not found'

if __name__ == "__main__":
    app = SystemMonitorApp()
    app.run()
