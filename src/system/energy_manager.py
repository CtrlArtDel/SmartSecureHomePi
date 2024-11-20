class EnergyManager:
    def __init__(self, energy_config):
        self.low_power_mode = energy_config['low_power_mode']

    def activate(self):
        print("Activating system (full power).")

    def deactivate(self):
        if self.low_power_mode:
            print("Switching to low power mode.")

