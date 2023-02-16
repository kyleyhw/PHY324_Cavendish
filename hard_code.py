import numpy as np

import error_propagation
ErrorPropagation = error_propagation.ErrorPropagation()

R_best_guesses = np.array([63.82, 63.51, 63.87, 63.80, 63.73, 63.79]) / 1000
R_uncertainties = np.zeros_like(R_best_guesses) + 0.1 / 1000
R_best_guess, R_uncertainty = ErrorPropagation.average(R_best_guesses, R_uncertainties)

w_best_guesses = np.array([29.85, 29.48, 29.37, 29.29, 29.31]) / 1000
w_uncertainties = np.zeros_like(w_best_guesses) + 0.1 / 1000

w_best_guess, w_uncertainty = ErrorPropagation.average(w_best_guesses, w_uncertainties)

d_best_guess = 0.05
d_uncertainty = 0

l_best_guesses = np.array([4.443, 4.442, 4.441, 4.453, 4.455])
l_uncertainties = np.zeros_like(l_best_guesses) + 0.002

l_best_guess, l_uncertainty = ErrorPropagation.average(l_best_guesses, l_uncertainties)

eq_1_best_guess, eq_1_uncertainty = 0.162258, 0.000009
CW_1_best_guess, CW_1_uncertainty = np.abs(0.141559 - eq_1_best_guess), ErrorPropagation.root_sum_of_squares(np.array([0.00004, eq_1_uncertainty]))
CCW_1_best_guess, CCW_1_uncertainty = np.abs(0.18356 - eq_1_best_guess), ErrorPropagation.root_sum_of_squares(np.array([0.00001, eq_1_uncertainty]))

eq_2_best_guess, eq_2_uncertainty = 0.164589, 0.000009
CW_2_best_guess, CW_2_uncertainty = np.abs(0.145376 - eq_2_best_guess), ErrorPropagation.root_sum_of_squares(np.array([0.000009, eq_2_uncertainty]))
CCW_2_best_guess, CCW_2_uncertainty =np.abs( 0.18783 - eq_2_best_guess), ErrorPropagation.root_sum_of_squares(np.array([0.00001, eq_2_uncertainty]))

CW_1_angle_best_guess, CW_1_angle_uncertainty = CW_1_best_guess / (2*l_best_guess), ErrorPropagation.root_sum_of_squares(np.array([CW_1_uncertainty, 2*l_uncertainty]))
CCW_1_angle_best_guess, CCW_1_angle_uncertainty = CCW_1_best_guess / (2*l_best_guess), ErrorPropagation.root_sum_of_squares(np.array([CCW_1_uncertainty, 2*l_uncertainty]))

CW_2_angle_best_guess, CW_2_angle_uncertainty = CW_2_best_guess / (2*l_best_guess), ErrorPropagation.root_sum_of_squares(np.array([CW_2_uncertainty, 2*l_uncertainty]))
CCW_2_angle_best_guess, CCW_2_angle_uncertainty = CCW_2_best_guess / (2*l_best_guess), ErrorPropagation.root_sum_of_squares(np.array([CCW_2_uncertainty, 2*l_uncertainty]))

CW_1_b_best_guess, CW_1_b_uncertainty = R_best_guess + w_best_guess/2 - d_best_guess*CW_1_angle_best_guess, ErrorPropagation.root_sum_of_squares(np.array([R_uncertainty, w_uncertainty/2, (d_best_guess*CW_1_angle_best_guess*ErrorPropagation.root_sum_of_squares(np.array([d_uncertainty/d_best_guess, CW_1_angle_uncertainty/CW_1_angle_best_guess])))]))

CCW_1_b_best_guess, CCW_1_b_uncertainty = R_best_guess + w_best_guess/2 - d_best_guess*CCW_1_angle_best_guess, \
                                        ErrorPropagation.root_sum_of_squares(np.array([R_uncertainty, w_uncertainty/2,
                                        (d_best_guess*CCW_1_angle_best_guess*ErrorPropagation.root_sum_of_squares(np.array([d_uncertainty/d_best_guess, CCW_1_angle_uncertainty/CCW_1_angle_best_guess])))]))

CW_2_b_best_guess, CW_2_b_uncertainty = R_best_guess + w_best_guess/2 - d_best_guess*CW_2_angle_best_guess, \
                                        ErrorPropagation.root_sum_of_squares(np.array([R_uncertainty, w_uncertainty/2,
                                        (d_best_guess*CW_2_angle_best_guess*ErrorPropagation.root_sum_of_squares(np.array([d_uncertainty/d_best_guess, CW_2_angle_uncertainty/CW_2_angle_best_guess])))]))

CCW_2_b_best_guess, CCW_2_b_uncertainty = R_best_guess + w_best_guess/2 - d_best_guess*CCW_2_angle_best_guess, \
                                        ErrorPropagation.root_sum_of_squares(np.array([R_uncertainty, w_uncertainty/2,
                                        (d_best_guess*CCW_2_angle_best_guess*ErrorPropagation.root_sum_of_squares(np.array([d_uncertainty/d_best_guess, CCW_2_angle_uncertainty/CCW_2_angle_best_guess])))]))

def G_guess(b, d, S, m, T, L):
    pi = np.pi
    return ((2 * pi**2 * b**2 * d * S) / (m * T**2 * L))

def G_uncertainty(b, d, S, m, T, L, u_b, u_s, u_m, u_T, u_L):
    pi = np.pi
    term_1 = (((2 * pi * b * d * S) / (m * T**2 * L)) * u_b)**2
    term_2 = (((pi**2 * b**2 + d ) / (m * T**2 * L)) * u_s)**2
    term_3 = (((pi**2 * b**2 * d * S) / (m**2 * T**2 * L)) * u_m)**2
    term_4 = (((2 * pi**2 * b**2 * d * S) / (m * T**3 * L)) * u_T)**2
    term_5 = (((pi**2 * b**2 * d * S) / (m * T**2 * L**2)) * u_L)
    square_result = term_1 + term_2 + term_3 + term_4 + term_5
    return np.sqrt(square_result)

CW_1_T_best_guess, CW_1_T_uncertainty = 305.21, 0.02
CCW_1_T_best_guess, CCW_1_T_uncertainty = 305.98, 0.05
CW_2_T_best_guess, CW_2_T_uncertainty = 303.12, 0.05
CCW_2_T_best_guess, CCW_2_T_uncertainty = 305.83, 0.05

'''
CW_1_S_best_guess, CW_1_S_uncertainty = 0.05366, 0.00004
CCW_1_S_best_guess, CCW_1_S_uncertainty = 0.02147, 0.00005
CW_2_S_best_guess, CW_2_S_uncertainty = 0.01381, 0.00004
CCW_2_S_best_guess, CCW_2_S_uncertainty = 0.02052, 0.00005
'''

CW_1_S_best_guess, CW_1_S_uncertainty = CW_1_best_guess, CW_1_uncertainty
CCW_1_S_best_guess, CCW_1_S_uncertainty = CCW_1_best_guess, CCW_1_uncertainty
CW_2_S_best_guess, CW_2_S_uncertainty = CW_2_best_guess, CW_2_uncertainty
CCW_2_S_best_guess, CCW_2_S_uncertainty = CCW_2_best_guess, CCW_2_uncertainty

m_best_guess, m_uncertainty = ErrorPropagation.average(np.array([1.4723, 1.4776]), np.array([0.05, 0.05]))


def beta_guess(r, d):
    result = (r**2) / ((r**2 + 4*d**2) * np.sqrt(r**2 + 4*d**2))
    return result
    
def beta_uncertainty(r, d, u_r, u_d):
    result = u_r * ((8 * d**2 * r - r**3) / (4 * d**2 + r**2)**(5/2))
    return result
 
CW_1_beta_guess, CW_1_beta_uncertainty = beta_guess(CW_1_b_best_guess, d_best_guess), beta_uncertainty(CW_1_b_best_guess, d_best_guess, CW_1_b_uncertainty, d_uncertainty)    
CCW_1_beta_guess, CCW_1_beta_uncertainty = beta_guess(CCW_1_b_best_guess, d_best_guess), beta_uncertainty(CCW_1_b_best_guess, d_best_guess, CCW_1_b_uncertainty, d_uncertainty) 
CW_2_beta_guess, CW_2_beta_uncertainty = beta_guess(CW_2_b_best_guess, d_best_guess), beta_uncertainty(CW_2_b_best_guess, d_best_guess, CW_2_b_uncertainty, d_uncertainty) 
CCW_2_beta_guess, CCW_2_beta_uncertainty = beta_guess(CCW_2_b_best_guess, d_best_guess), beta_uncertainty(CCW_2_b_best_guess, d_best_guess, CCW_2_b_uncertainty, d_uncertainty) 




CW_1_G_best_guess, CW_1_G_uncertainty = G_guess(CW_1_b_best_guess, d_best_guess, CW_1_S_best_guess, m_best_guess, CW_1_T_best_guess, l_best_guess) / CW_1_beta_guess,\
    G_uncertainty(CW_1_b_best_guess, d_best_guess, CW_1_S_best_guess, m_best_guess, CW_1_T_best_guess, l_best_guess, CW_1_b_uncertainty, CW_1_S_uncertainty, m_uncertainty, CW_1_T_uncertainty, l_uncertainty)

CCW_1_G_best_guess, CCW_1_G_uncertainty = G_guess(CCW_1_b_best_guess, d_best_guess, CCW_1_S_best_guess, m_best_guess, CCW_1_T_best_guess, l_best_guess) / CCW_1_beta_guess,\
    G_uncertainty(CCW_1_b_best_guess, d_best_guess, CCW_1_S_best_guess, m_best_guess, CCW_1_T_best_guess, l_best_guess, CCW_1_b_uncertainty, CCW_1_S_uncertainty, m_uncertainty, CCW_1_T_uncertainty, l_uncertainty)

CW_2_G_best_guess, CW_2_G_uncertainty = G_guess(CW_2_b_best_guess, d_best_guess, CW_2_S_best_guess, m_best_guess, CW_2_T_best_guess, l_best_guess) / CW_2_beta_guess,\
    G_uncertainty(CW_2_b_best_guess, d_best_guess, CW_2_S_best_guess, m_best_guess, CW_2_T_best_guess, l_best_guess, CW_2_b_uncertainty, CW_2_S_uncertainty, m_uncertainty, CW_2_T_uncertainty, l_uncertainty)

CCW_2_G_best_guess, CCW_2_G_uncertainty = G_guess(CCW_2_b_best_guess, d_best_guess, CCW_2_S_best_guess, m_best_guess, CCW_2_T_best_guess, l_best_guess) / CCW_2_beta_guess,\
    G_uncertainty(CCW_2_b_best_guess, d_best_guess, CCW_2_S_best_guess, m_best_guess, CCW_2_T_best_guess, l_best_guess, CCW_2_b_uncertainty, CCW_2_S_uncertainty, m_uncertainty, CCW_2_T_uncertainty, l_uncertainty)



print(CW_1_G_best_guess, CW_1_G_uncertainty)
print(CCW_1_G_best_guess, CCW_1_G_uncertainty)
print(CW_2_G_best_guess, CW_2_G_uncertainty)
print(CCW_2_G_best_guess, CCW_2_G_uncertainty)