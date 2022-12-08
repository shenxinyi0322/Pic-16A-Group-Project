Find 🕵️

Names of group members: Benji Carrere, Daisy Watters, Ellen Lee, Xinyi Shen 

Short description of this project: For this project we plan to use the Song Popularity Dataset which can be used to predict the popularity of songs based on factors like liveness, acoustics, energy, etc. Specifically, we would love to find potential correlations between song characteristics such as loudness and energy. 

List of Python packages used and their versions (e.g. numpy 1.21.5): !!!!!!!!!!!!!!!!!!!!!!!!!!!!

Detailed description of the demo file:

System output: 
 - examples of data visualization between variables through scatterplot, lineplot, and boxplot
 - scatterplots that indicate the correlation between the different song characteristics
 - correlation coefficients of the scatterplots
 - prediction models of the characteristics illustrating the strongest correlations 

How to Run:
1. Import data frame of song popularity
2. Drop any songs that appeared multiple times in the dataset, as well as "liveness" subset since it is not relevant to song popularity.
3. Call data_graph class to display the correlation between "energy" and "loudness" through scatterplot, lineplot, and boxplot. 
![scatterplot](https://user-images.githubusercontent.com/114321320/206331509-f0838446-09b1-4f61-9c2a-d62f1b38280c.png)
![lineplot](https://user-images.githubusercontent.com/114321320/206331577-0d9f84eb-c6c7-4b97-910f-2c505a33cbac.png)
![boxplot](https://user-images.githubusercontent.com/114321320/206331608-ebf681b0-31cd-4a0e-b9b4-d711ef875def.png)

4. As presented by the above graphs, a line plot is not the most optimal figure to show the correlation between "energy" and "loudness". To present a better case of practicing line plot, variable "key", which has intervals, is plotted with the mean song popularity for each interval. Resulting in a line plot with better visualization of variable correlations.
![betterlineplot](https://user-images.githubusercontent.com/114321320/206331695-03a1826e-dd23-4b69-897a-16d3084bd27c.png)

5. Create a new data frame of song popularity af without "song_name" and "song_popularity" subset. "song_name" is dropped because it cannot be plotted as a string. 
6. Use the scatterplot_matrix function on this data frame to see the relationships between different variables in the dataset. This should result in a matrix of scatterplots that compare all the characteristics in the data frame with each other. The scatterplots can be interpretted by looking at the coeficcients listed at the bottoms of each graph as well as the visual pattern of the plots. If the absolute value of the correlation coefficient is between 0.3 and 0.7, this means there is a moderate correlation. Above 0.7 indicates a strong correlation and below 0.3 indicates no significant correlation.
![step 6](https://user-images.githubusercontent.com/114321320/205517811-5ad2978a-475d-4584-b89d-0ee519b2e8dc.png)

7. Use the strongest_correlation function to filter out the characteristcs with no significant correlation. The expected outputs are 4 scatterplots comparing acoutsticness and energy, acoutsticness and loudness, energy and loudness, and instrumentalness and loudness. 
![step 7](https://user-images.githubusercontent.com/114321320/205518052-e91987f1-f7e8-4137-a9fe-b675dd68536b.png)

8. Call the bestmodel function of each of the strongest_correlation results. The expected outputs are scatterplots with the actual data along with 1 linear regression model and second degree polynomial model. The function will also output the function of the better prediction model, printing out the equation.
![bestmodel](https://user-images.githubusercontent.com/114321320/206332392-07332f79-bd50-49a4-9eaa-8cbec029d1d5.png)

9. Use the scatterplot_matrix_song_popularity function to create scatterplots that compare all the characteristics in the data frame with song popularity. Based on the data visualizations and the correlation coeficcients listed at the bottoms of each graph, there is no significant correlation found between any of the song characteristics and song popularity.

Scope and limitations, including ethical implications, accessibility concerns, and ideas for potential extensions.
I. When we were cleaning the data, song names were dropped from the dataset. Since song names can be related to trendy events, such as movies or social movements, this could have affected song popularity. However, such kinds of correlations between song names and song popularity can not be indicateds through our code. 
II. This dataset contains songs that are mainly in English with some that are in Spanish. However, when looking at the recent music scene, we can see that Asian music has gained traction as well, making its way into the Billboard Global Top 100. Something else that we should keep in mind is the fact that song popularity is very strongly influenced by the time of year. For example, in December, we can see a spike in holiday/Christmas related songs which might greatly skew the data. If we were able to obtain more current informmation in the dataset, we could generate a more acurate statistic like a correlation between popular types of songs in a certain timme period. This could help musicians analyze song trends based on the time of year. 

References and acknowledgement.
Project utilizes the Song Popularity Dataset. This dataset is referred from Kaggle, and was created by M. Yasser H. 
[link](https://www.kaggle.com/datasets/yasserh/song-popularity-dataset/discussion?resource=download)
License: CCO: Public Domain
