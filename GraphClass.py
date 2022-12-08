import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn import preprocessing
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

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

def strongest_correlation(cols, desired_coef, figsize, df):
    """ Creates a matrix of scatterplots, each with a different possible pair of variables
    on the x and y axis.
    Args:
        cols: a list or array of strings. Each string is the name of one of the data columns.
        desired_coef: a float between 0 and 1. Dictates the minimum correlation coefficient between
        variables for displayed plots. 
        figsize: a tuple of two integers. Sets figure size to be element 0 by element 1
        df: a datasest of various data types. Columns data is indexed and plotted from it.
    Returns:
        None
    """
    # sets n equal to the number of columns
    n = len(cols)
    # initializes empty list "strong_corr"
    strong_corr = []

    # loops through n times
    for i in range(n):
        # loops through n times
        for j in range(n):
            # creates variable corr_coeff that finds correlation coefficient of
            # dataset column names cols[i] and cols[j]
            corr_coef = np.corrcoef(x=(df[cols[i]]), y=(df[cols[j]]))
            corr_coef = corr_coef[0, 1]
            # if absolute value of the correlation coefficient is greater than or
            # equal to inputted desired minimum coefficient AND
            # the two indexed columns are not the same,
            # the two indexed columns are appended to list "strong_corr" as a tuple
            if (abs(corr_coef) >= desired_coef) & ((cols[i] >= cols[j])==False):
                strong_corr.append((cols[i], cols[j]))

    # sets s equal to length of list "strong_corr"
    s = len(strong_corr)
    # if length of strong_corr is less than one error is raised
    if s < 1:
        raise ValueError('There is no combination of variables that yields a correlation coefficient this high.')
    # creates s by 1 new plots of size specified in parameters
    fig, ax = plt.subplots(s, 1, figsize=figsize)
    
    # if length of strong_corr is 1
    if s == 1:
        # creates variable corr_coeff that finds correlation coefficient of
        # the two variable in tuple
        corr_coef = np.corrcoef(x=(df[strong_corr[0][0]]), y=(df[strong_corr[0][1]]))
        corr_coef = corr_coef[0, 1]
        # sets title and y axis label of subplot to be the 1st and 2nd tuple value respectively 
        # sets x axis label to be a "caption" with the correlation coefficient of the variables
        ax.set(title = strong_corr[0][0], ylabel = strong_corr[0][1], xlabel = r"$\rho$ = " 
                                    + str(np.round(corr_coef, 2)))
        # subplot is made into a scatter plot, with tuple value 0 as x axis and value 1 as y axis
        ax.scatter(df[strong_corr[0][0]], df[strong_corr[0][1]]) 
    # if length of strong_corr is greater than 1
    else:
        # loops through s times
        for i in range(s):
            # creates variable corr_coeff that finds correlation coefficient of
            # the two variable in tuple i
            corr_coef = np.corrcoef(x=(df[strong_corr[i][0]]), y=(df[strong_corr[i][1]]))
            corr_coef = corr_coef[0, 1]
            # sets title and y axis label of subplot row i to be the 1st and 2nd tuple value respectively 
            # sets x axis label to be a "caption" with the correlation coefficient of the variables
            ax[i].set(title = strong_corr[i][0], ylabel = strong_corr[i][1], xlabel = r"$\rho$ = " 
                                        + str(np.round(corr_coef, 2)))
            # subplot of row i is made into a scatter plot, 
            # with list index i's tuple value 0 as x axis and value 1 as y axis
            ax[i].scatter(df[strong_corr[i][0]], df[strong_corr[i][1]])

    # adjusts subplot params so that the subplot(s) fits in to the figure area
    # sublots are displayed
    plt.tight_layout()
    plt.show()

def scatterplot_matrix_song_popularity(cols, figsize, df):
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
    fig, ax = plt.subplots(n-1, 1, figsize=figsize)
    

    # loops through subplots by columns
    for j in range(n-1):
        # creates variable corr_coeff that finds correlation coefficient of
        # dataset columns i and j
        corr_coef = np.corrcoef(x=(df[cols[j+1]]), y=(df[cols[0]]))
        corr_coef = corr_coef[0, 1]
        # sets title and y axis label of subplot in row i and column j 
        # to be i-th data column name and j-th column name respectively 
        # sets x axis label to be a "caption" with the correlation 
        # coefficient for each subplot
        ax[j].set(title = cols[j+1], ylabel = cols[0], xlabel = r"$\rho$ = " 
                            + str(np.round(corr_coef, 2)))
        # if i does not equal j, body of code is run
        ax[j].scatter(df[cols[j+1]], df[cols[0]])
                
    # adjusts subplot params so that the subplot(s) fits in to the figure area
    # sublots are displayed
    plt.tight_layout()
    plt.show()
    
def PolynomialRegression(degree=2, **kwargs):
    return make_pipeline(preprocessing.PolynomialFeatures(degree),
                         LinearRegression(**kwargs))
    
def bestmodel(X,y,Xlabel,ylabel):
    """ Create a graph comparing linear regression model and polynomial regression model with actual data point
    Args:
        X: a series of data from one data columns 
        y: another series of data from one data columns 
        Xlabel: a string input, serving as the x-axis label for the graph output
        ylabel: a string input, serving as the x-axis label for the graph output
    Returns:
        None
    """
    X = np.array(X)
    y = np.array(y)
    X = X.reshape(-1, 1) #convert 1D array to 2D array to fit the function
    y = y.reshape(-1, 1)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
    #test_size indicates the proportion of test data used for evaluating the best model; default value set to 0.3

    model1 = PolynomialRegression(1) # linear regression model
    model1.fit(X_train,y_train)
    #print(model1[-1].coef_, model1[-1].intercept_) 

    model2 = PolynomialRegression(2) # polynomial regression model 
    model2.fit(X_train, y_train)
    #print(model2[-1].coef_, model2[-1].intercept_)

    #plot both models with real data points
    fig, ax = plt.subplots(1, figsize=(12,8))
    ax.scatter(X, y, label = "data points")
    xfit = np.linspace(0.01, 1, 1000).reshape(-1,1) 
    ax.plot(xfit, model1.predict(xfit), 'k', label='prediction model - degree 1')
    ax.plot(xfit, model2.predict(xfit), 'r', label='prediction model - degree 2')
    ax.set(xlabel=Xlabel, ylabel=ylabel)
    ax.set_title(Xlabel + " vs. "+ ylabel)
    plt.legend(fontsize=20)
    plt.show()  

    #determine the better model
    if model1.score(X_test, y_test) > model2.score(X_test, y_test):
        print("The linear regression model is the better perdiction model.")
        print("The model function is f(x) = " + model1[-1].coef_[0][1] +"x + (" +model1[-1].intercept_[0] + ")")
    if model1.score(X_test, y_test) < model2.score(X_test, y_test):
        print("The polynomial regression model is the better perdiction model.")
        print("The model function is f(x) = " + str(model2[-1].coef_[0][2]) +" x^2 + ("+ str(model2[-1].coef_[0][1]) +") x + ("                 +str(model2[-1].intercept_[0])+")")

    
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
            
    def box(self):
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
    
