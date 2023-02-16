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

        l_best_guesses = np.array([4.443, 4.442, 4.441, 4.453, 4.455])
        l_uncertainties = np.zeros_like(l_best_guesses) + 0.0005

        (l_best_guess, l_uncertainty) = ErrorPropagation.average(l_best_guesses, l_uncertainties)

        self.zeroed_times = cff.remove_systematic_error(raw_times)
        self.approximate_angles = raw_positions / (2 * l_best_guess)
        
        self.y = self.approximate_angles
        fractional_errors_in_position = 0.0005 / raw_positions
        fractional_error_in_l = l_uncertainty / l_best_guess
        self.y_error = np.sqrt(fractional_errors_in_position**2 + fractional_error_in_l) * self.y
        
        self.x = self.zeroed_times
        self.x_error = np.zeros_like(self.zeroed_times) + 0.0005