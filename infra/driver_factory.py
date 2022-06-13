class DriverFactory:

    def get_driver(self, env):
        if env['DRIVER'] == "remoto":
            return self.instancia_driver_remoto()
        else:
            return self.instancia_driver_local()
        
    def instancia_driver_local(self):
        return 'local'

    def instancia_driver_remoto(self):
        return 'remoto'