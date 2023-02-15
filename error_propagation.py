import numpy as np

class ErrorPropagation():
    def __init__(self):
        pass

    def sum_of_squares(self, arr):
        result = np.sum(arr**2)
        return result

    def root_sum_of_squares(self, arr):
        result = np.sqrt(self.sum_of_squares(arr))
        return result

    def add(self, best_guesses, uncertainties):
        best_guess = np.sum(best_guesses)
        uncertainty = self.root_sum_of_squares(uncertainties)
        return (best_guess, uncertainty)

    def multiply(self, best_guesses, uncertainties):
        best_guess = np.prod(best_guesses)
        uncertainty = self.root_sum_of_squares(uncertainties / best_guesses)
        return (best_guess, uncertainty)

    def average(self, best_guesses, uncertainties):
        best_guess = np.sum(best_guesses) / len(best_guesses)
        uncertainty = self.root_sum_of_squares(uncertainties) / len(uncertainties)
        return (best_guess, uncertainty)