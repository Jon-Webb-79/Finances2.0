# Import necessary packages here
import matplotlib
from matplotlib import rcParams, pyplot as plt
import matplotlib.dates as mdates

# =============================================================================================
# =============================================================================================
# Date:    November 26, 2017
# Purpose: This code contains functions necessary to plot 2-D data streams

# Source Code Metadata
__author__ = "Jonathan A. Webb"
__copyright__ = "Copyright 2017, Jon Webb Inc."
__version__ = "1.0"
# =============================================================================================
# =============================================================================================


def twodplot(x_data, y_data, xscale, yscale, colors, labels,
             plot_name, x_label, y_label, position=0,
             label_fontsize=18, tick_fontsize=18, plots='single'):
    """

    :param x_data: int, float
                   An array of list of arrays of x-data
    :param y_data: int float
                   An array or list of arrays of y-data
    :param xscale: char str
                   'log' or 'lin'
    :param yscale: char str
                   'log' or 'lin'
    :param colors: char str
                   line colors
    :param labels: char str
                   The label for each line
    :param plot_name: char str
                      The name of the plot
    :param x_label: char str
                    The label for the x-axis
    :param y_label: char str
                    The label for the y-axis
    :param position: int
                     The position for the labels (0-4)
    :param label_fontsize: int
    :param tick_fontsize: int
    :param plots: char str
                  'single' or 'multiple'
    :return:
    """
    plt.rcParams.update({'figure.autolayout': True})
    fig, td_plot = plt.subplots()
    matplotlib.rc('xtick', labelsize=tick_fontsize)
    matplotlib.rc('ytick', labelsize=tick_fontsize)
    if x_label.upper() != 'NONE':
        td_plot.set_xlabel(x_label, fontsize=label_fontsize)
    if y_label.upper() != 'NONE':
        td_plot.set_ylabel(y_label, fontsize=label_fontsize)
    if xscale.upper() == 'LOG':
        td_plot.set_xscale('log')
    if yscale.upper() == 'LOG':
        td_plot.set_yscale('log')

    if plots != 'single':
        for i in range(len(labels)):
            td_plot.plot(x_data[i], y_data[i], color=colors[i], label=labels[i])
    else:
        td_plot.plot(x_data, y_data, color=colors, label=labels)

    plt.legend(loc=position)
    plt.savefig(plot_name)
    plt.close()
    return
# =============================================================================================


def timedateplot(timedate_data, y_data, x_label, y_label, colors,
                 labels, plot_name, position=0, yscale='lin',
                 tick_fontsize=18, label_fontsize=18):
    """

    :param timedate_data: object
                          A time string built with the datetime module, can be an \
                          array of multiple datetime-streams
    :param y_data: float
                   The independent variable, can be an array of independent variables \
                   of same length as 'timedate_data'
    :param x_label: char string
                    The name of the x-axis
    :param y_label: char string
                    The name of the y-axis
    :param colors: char string
                   Line color, can be an array
    :param labels: char string
                   the name of each plot, can be an array
    :param plot_name: char string
                      The name of the plot
    :param position: int
                     The position of the legend, 0-4
    :param yscale: char string
                   'log' or 'lin'
    :param tick_fontsize: int
                          The font size for the axis ticks
    :param label_fontsize: int
                           The font size of the labels
    :return:

    This function will produce a time series plot
    """
    fig, td_plot = plt.subplots()
    matplotlib.rc('xtick', labelsize=tick_fontsize)
    matplotlib.rc('ytick', labelsize=tick_fontsize)
    if yscale.upper() == 'LOG':
        td_plot.set_yscale('log')
    td_plot.set_xlabel(x_label, fontsize=label_fontsize)
    td_plot.set_ylabel(y_label, fontsize=label_fontsize)
    if colors.size == 1:
        delta = (timedate_data[len(timedate_data) - 1] - timedate_data[0]).days + 1
        if delta <= 15:
            myfmt = mdates.DateFormatter('%d')
            td_plot.xaxis.set_major_locator(mdates.DayLocator())
        elif delta <= 180:
            myfmt = mdates.DateFormatter('%b-%y')
            td_plot.xaxis.set_major_locator(mdates.MonthLocator())
        else:
            myfmt = mdates.DateFormatter('%b-%y')
            td_plot.xaxis.set_major_locator(plt.MaxNLocator(4))
            # td_plot.xaxis.set_major_locator(mdates.MonthLocator())
        td_plot.xaxis.set_major_formatter(myfmt)
        td_plot.plot(timedate_data, y_data, label=labels, color=colors)
    else:
        for i in range(len(y_data)):
            delta = (timedate_data[i][len(timedate_data[i]) - 1] - timedate_data[i][0]).days + 1
            if delta <= 15:
                myfmt = mdates.DateFormatter('%d')
                td_plot.xaxis.set_major_locator(mdates.DayLocator())
            elif delta <= 180:
                myfmt = mdates.DateFormatter('%b-%y')
                td_plot.xaxis.set_major_locator(mdates.MonthLocator())
            else:
                myfmt = mdates.DateFormatter('%b-%y')
                td_plot.xaxis.set_major_locator(plt.MaxNLocator(4))
                # td_plot.xaxis.set_major_locator(mdates.MonthLocator())
            td_plot.xaxis.set_major_formatter(myfmt)
            td_plot.plot(timedate_data[i], y_data[i], label=labels[i], color=colors[i])
    plt.legend(loc=position)
    plt.savefig(plot_name)
    plt.close()
    return
# =============================================================================================


def histogramplot(data, x_label, y_label, title, nbins=10,
                  tick_fontsize=18, label_fontsize=18):
    """

    :param data: float
                 The dependent variable data
    :param x_label: char string
                    The x-axis name
    :param y_label: char string
                    The y-axis name
    :param title: char string
                  The plot name
    :param nbins: int
                  The number of histogram bins
    :param tick_fontsize: int
                          The tick font size
    :param label_fontsize: int
                           the label fon size
    :return:

    This function will produce a histogram plot of data
    """
    matplotlib.rc('xtick', labelsize=tick_fontsize)
    matplotlib.rc('ytick', labelsize=tick_fontsize)
    plt.xlabel(x_label, fontsize=label_fontsize)
    plt.ylabel(y_label, fontsize=label_fontsize)
    plt.hist(data, bins=nbins)
    plt.savefig(title)
    plt.close()
# eof
