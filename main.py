import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

class data_graph:
    '''
    A class for data visualizations. Gives user ability to input data and pick the type of graph
    '''
    def __init__(self, x_label = '', y_label = '', x_data = [], y_data = []):
        # save the axis labels
        self.x_label = x_label
        self.y_label = y_label
        # data for the x-axis
        self.x_data = x_data
        # data for the y-axis
        self.y_data = y_data
    
    def scatter(self, data_color = ''):
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
        # no option to input color for boxplot method
        fig, ax = plt.subplots(1, 1)
        # plot the data inputted as x_data, and make it horizontal because it looks better
        ax.boxplot(self.x_data, vert = False)
        # customize the plot
        ax.set(xlabel = self.x_label, title = self.x_label)
        plt.show()
    


