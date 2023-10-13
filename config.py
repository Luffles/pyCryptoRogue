

class CONFIG(object):
    """Unconfigured build variables"""
    # CONFIG(debug = debug,
    #        environment='local',
    #        alive_interval=0,
    #        tests='all',
    #        buildme=True )
    def __init__(self) -> object:
        debug: bool
        alive_interval: int
        tests:  enum
        buildme: bool
        version: float
        success: bool
        return self




@CONFIG
def Build_Config(object):
    """Configured build variables"""
    builder = CONFIG(object)
        #send me to test cases
        # if env == 'local':
        # debug=True, env='local'



# Build('local')