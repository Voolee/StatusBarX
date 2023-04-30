import psutil
import rumps

class SystemMonitorApp(rumps.App):
    def __init__(self):
        super(SystemMonitorApp, self).__init__("System Monitor")
        self.update_status()
        self.timer = rumps.Timer(self.update_status, 2)
        self.timer.start()

    def update_status(self, _=None):
        cpu_percent = psutil.cpu_percent()
        memory_info = psutil.virtual_memory()
        memory_percent = memory_info.percent

        self.title = f"CPU: {cpu_percent}% | RAM: {memory_percent}%"

if __name__ == "__main__":
    app = SystemMonitorApp()
    app.run()
