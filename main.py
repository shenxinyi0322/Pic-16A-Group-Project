import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

def scatterplot_matrix(cols, figsize, df):
    """ Creates a matrix of scatterplots, each with a different possible pair of variables
    on the x and y axis.
    Args:
        cols: a list or array of strings. Each string is the name of one of the data columns.
        figsize: a tuple of two integers. Sets figure size to be element 0 by element 1.
        df: a datasest of various data types. Columns data is indexed and plotted from it.
    Returns:
        None
    """
    # sets n equal to the number of columns, then creates n by n new plots of size 
    # specified in parameters
    n = len(cols)
    fig, ax = plt.subplots(n, n, figsize=figsize)
    
    # loops through subplots by rows
    for i in range(n):
        # loops through subplots by columns
        for j in range(n):
            # creates variable corr_coeff that finds correlation coefficient of
            # dataset columns i and j
            corr_coef = np.corrcoef(x=(df[cols[i]]), y=(df[cols[j]]))
            corr_coef = corr_coef[0, 1]
            # sets title and y axis label of subplot in row i and column j 
            # to be i-th data column name and j-th column name respectively 
            # sets x axis label to be a "caption" with the correlation 
            # coefficient for each subplot
            ax[i,j].set(title = cols[i], ylabel = cols[j], xlabel = r"$\rho$ = " 
                                + str(np.round(corr_coef, 2)))
            # if i does not equal j, body of code is run
            if i != j:
                # subplot in row i and column j is made into a scatter plot, with data
                # column i of the dataset as x axis, and column j as y axis
                ax[i,j].scatter(df[cols[i]], df[cols[j]])
    
    # subplot adjusted so it fits into figure area, and subplots below the 
    # diagonal of blank graphs are deleted such that only subplots above are shown
    # this is to avoid variable combination repeats
    for i in range(n):
        for j in range(n):
            if i < j:
                continue
            else: 
                plt.delaxes(ax[i, j])
                
    # adjusts subplot params so that the subplot(s) fits in to the figure area
    # sublots are displayed
    plt.tight_layout()
    plt.show()

class data_graph:
    '''
    A class for data visualizations. Gives user ability to input data and pick the type of graph
    '''
    def __init__(self, x_label = '', y_label = '', x_data = [], y_data = []):
        # save the axis labels
        self.x_label = x_label
        self.y_label = y_label
        # save the data for the x and y axis
        self.x_data = x_data
        self.y_data = y_data
    
    def scatter(self, data_color = ''):
        ''' Creates a scatter plot using the instance variables for data and labels
        Args: 
            data_color: color of the plot points (empty string if not inputted)
        Returns:
            None
        '''
        fig, ax = plt.subplots(1, 1)
        # if the user inputted a value for the data_color argument
        if data_color != '':
            # try to plot as long as the inputted string is a valid color
            try:
                # make a scatter plot using the inputted data
                ax.scatter(self.x_data, self.y_data, color = data_color)
                # customize the scatter plot using the inputted data
                ax.set(xlabel = self.x_label, ylabel = self.y_label, title = self.y_label + " vs. " + self.x_label)
            # if the string was not a valid color, print the error message
            except ValueError:
                print("Error: must input a valid color")
        # if the user did not input a color, do the same thing without changing the color of the data
        else:
            ax.scatter(self.x_data, self.y_data)
            ax.set(xlabel = self.x_label, ylabel = self.y_label, title = self.y_label + " vs. " + self.x_label)
        plt.show()
            
    def line(self, data_color = ''):
        ''' Creates a line plot using the instance variables for data and labels
        Args: 
            data_color: color of the line (empty string if not inputted)
        Returns:
            None
        '''
        # this method is the same as scatter but with plot instead
        fig, ax = plt.subplots(1, 1)
        if data_color != '':
            try:
                ax.plot(self.x_data, self.y_data, color = data_color)
                ax.set(xlabel = self.x_label, ylabel = self.y_label, title = self.y_label + " vs. " + self.x_label)
            except ValueError:
                print("Error: must input a valid color")
        else:
            ax.plot(self.x_data, self.y_data)
            ax.set(xlabel = self.x_label, ylabel = self.y_label, title = self.y_label + " vs. " + self.x_label)
        plt.show()
            
    def boxplot(self):
        ''' Creates boxplot using the instance variables for data and labels
        Args: 
            None
        Returns:
            None
        '''
        # no option to input color for boxplot method
        fig, ax = plt.subplots(1, 1)
        # plot the data inputted as x_data, and make it horizontal because it looks better
        ax.boxplot(self.x_data, vert = False)
        # customize the plot
        ax.set(xlabel = self.x_label, title = self.x_label)
        plt.show()
    


