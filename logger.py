import logging as lg

class site_logger:
    
    def __init__(self):
        pass
        
    def log(self,username,loglevel,message):
        self.username=username  # this variable will store name of logger/user who is entering data
        self.loglevel=loglevel  # this will store level of logging data eg. error,critical etc
        self.message=message    # here is the messsge of the logger
        
        lg.basicConfig(filename="testtest.log",level=lg.DEBUG,format='%(name)s - %(asctime)s - %(levelname)s - %(message)s')
        self.logger=lg.getLogger(self.username)
        
        if self.loglevel=='debug':
            self.logger.debug(self.message)
        elif self.loglevel=='info':
            self.logger.info(self.message)
        elif self.loglevel=='warning':
            self.logger.warning(self.message)
        elif self.loglevel=='error':
            self.logger.error(self.message)
        elif self.loglevel=='critical':
            self.logger.critical(self.message)
        else:
            print('Check logger file for for syntax')

    def __str__(self):
        return "This is logger for easy entry to logger data."