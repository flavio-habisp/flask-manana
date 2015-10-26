from manana import config
from manana.application import create_application


application = create_application(config.ConfigDev)
application.run()
