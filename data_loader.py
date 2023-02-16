import numpy as np

import error_propagation
ErrorPropagation = error_propagation.ErrorPropagation()
from fitting_and_analysis import CurveFitFuncs
cff = CurveFitFuncs()

class DataLoader():
    def __init__(self, filename):
        directory = 'data/%s.txt' % filename
        self.full_data = np.loadtxt(directory, dtype=str, skiprows=2).T
        
        start_sample = 20
        
        raw_positions = np.array([float(x) for x in self.full_data[1][start_sample:]])
        
        raw_times = [time.split(':') for time in self.full_data[0][start_sample:]]
        raw_times = np.array([float(h) * 3600 + float(m) * 60 + float(s) for [h, m, s] in raw_times])


        self.zeroed_times = cff.remove_systematic_error(raw_times)
        
        self.y = raw_positions
        self.y_error = np.zeros_like(raw_positions) + 0.0005
        
        self.x = self.zeroed_times
        self.x_error = np.zeros_like(self.zeroed_times) + 0.0005