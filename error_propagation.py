import numpy as np

class ErrorPropagation():
    def __init__(self):
        pass

    def add(self, a, b): # a + b
        best_guess = a.data + b.data
        uncertainty = np.sqrt(a.uncertainty ** 2 + b.uncertainty ** 2)

        result = PhysicalQuantity(best_guess, uncertainty)
        return result

    def subtract(self, a, b): # a - b
        best_guess = a.data - b.data
        uncertainty = np.sqrt(a.uncertainty ** 2 + b.uncertainty ** 2)

        result = PhysicalQuantity(best_guess, uncertainty)
        return result

    def multiply(self, a, b): # a * b
        best_guess = a.data * b.data
        uncertainty = np.sqrt(((a.uncertainty / a.data) ** 2 + (b.uncertainty / b.data) ** 2)) * best_guess

        result = PhysicalQuantity(best_guess, uncertainty)
        return result

    def divide(self, a, b): # a / b
        best_guess = a.data / b.data
        uncertainty = ((a.uncertainty / a.data) + (b.uncertainty / b.data)) * best_guess

        result = PhysicalQuantity(best_guess, uncertainty)
        return result

    def exponentiate(self, a, b): # a ** b
        best_guess = a.data ** b.data
        a_uncertainty = ((b.data.value * (a.data.value ** (b.data.value - 1))) * a.uncertainty)
        b_uncertainty = ((np.log(a.data.value) * (a ** b)) * b.uncertainty)
        uncertainty = np.sqrt(a_uncertainty ** 2 + b_uncertainty ** 2)

        result = PhysicalQuantity(best_guess, uncertainty)
        return result

    def reciprocate(self, a): # 1 / a
        from astropy import units as u
        constant_1 = PhysicalQuantity(1 * u.dimensionless_unscaled, 0 * u.dimensionless_unscaled)

        result = self.divide(constant_1, a)
        return result