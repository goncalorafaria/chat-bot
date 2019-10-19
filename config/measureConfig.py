from runtime.metric import Metric

class MeasureConfig(object):
    
    def __init__(self, 
                 m: Metric,
                 processConfig: tuple):
        self.m = m
        self.processConfig = processConfig
        
        