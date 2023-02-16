import matplotlib.pyplot as plt
from matplotlib import rc
font = {'family' : 'DejaVu Sans',
        'weight' : 'normal',
        'size'   : 30}
rc('font', **font)
import numpy as np

import data_loader
import fit_models
import fitting


def run_main(filename, show=False, save=False):
    data = data_loader.DataLoader(filename)
    model = fit_models.DecayingSinusoid()

    units_for_parameters = ('rad', 'rad', 's', '(unitless)', r's$^{-1}$')

    try:
        fit = fitting.Fitting(model=model, x=data.x, x_error=data.x_error, y_measured=data.y, y_error=data.y_error,
                              units_for_parameters=units_for_parameters, p0=(0, 0.02, 250, 1, 0.01))
    except RuntimeError:
        fit = fitting.Fitting(model=model, x=data.x, x_error=data.x_error, y_measured=data.y, y_error=data.y_error,
                              units_for_parameters=units_for_parameters, p0=(0, 0.02, 250, -1, 0.01))
    
    fig, ax = plt.subplots(1, 1, figsize=(16, 9))
    
    fit.scatter_plot_data_and_fit(ax)

    plot_title = filename.split('_')[0] + ' trial ' + filename.split('_')[1]

    ax.set_title(plot_title)
    ax.grid(visible=True, which='both')
    ax.set_ylabel(r'x / m')
    ax.set_xlabel(r'time / s')
    
    if save:
            fig.savefig('graphs/%s_plot.png' % filename)
    if show:
            fig.show()

    fig.clear()


    fig, ax = plt.subplots(1, 1, figsize=(16, 9))

    fit.plot_residuals(ax)

    plot_title = filename.split('_')[0] + ' trial ' + filename.split('_')[1] + ' residuals'

    ax.set_title(plot_title)
    ax.grid(visible=True, which='both')
    ax.set_ylabel(r'residuals / m')
    ax.set_xlabel(r'time / s')

    if save:
        fig.savefig('graphs/%s_residual.png' % filename)
    if show:
        fig.show()
            
# filename labels: 0 -> feb2, 1 -> feb7, 2 -> feb9

CCW_filenames = {'CCW_%d' % trial : 'CCW_%d' % trial for trial in [1, 2]}
CW_filenames = {'CW_%d' % trial : 'CW_%d' % trial for trial in [1, 2]}
Neutral_filenames = {'Neutral_%d' % trial : 'Neutral_%d' % trial for trial in [1, 2]}

all_filenames = {**CCW_filenames, **CW_filenames, **Neutral_filenames}

def run_all(all_filenames):
    for filename in all_filenames:
        print(filename)
        run_main(filename, show=True, save=True)

run_all(all_filenames)