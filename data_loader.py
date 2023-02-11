import numpy as np
from fitting_and_analysis import CurveFitFuncs
cff = CurveFitFuncs()

class DataLoader():
    def __init__(self, filename):
        self.full_data = np.loadtxt(filename, dtype=str).T
        
        start_sample = 20
        
        raw_positions = np.array([float(x) for x in self.full_data[1][start_sample:]])
        
        raw_times = [time.split(':') for time in self.full_data[0][start_sample:]]
        raw_times = np.array([float(h) * 3600 + float(m) * 60 + float(s) for [h, m, s] in raw_times])
        
        self.zeroed_times = cff.remove_systematic_error(raw_times)
        self.zeroed_positions = cff.remove_systematic_error(raw_positions)
        
        self.y = self.zeroed_positions
        self.y_error = np.zeros_like(self.zeroed_positions) + 0.001
        
        self.x = self.zeroed_times
        self.x_error = np.zeros_like(self.zeroed_times) + 0.001