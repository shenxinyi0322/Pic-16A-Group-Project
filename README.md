SpotiFind 🕵️

Ellen Lee, Xinyi Shen, Daisy Watters, Benji Carrere

For this project we plan to use the Song Popularity Dataset which can be used to predict the popularity of songs based on factors like liveness, acoustics, energy, etc. Specifically, we would love to find potential correlations between song characteristics such as loudness and energy. 

List of Python packages used and their versions (e.g. numpy 1.21.5). This is good practice for reproducible and responsible programming!

Detailed description of the demo file. This includes detailed instructions on how to run it, what output one should expect to see, and any explanations or interpretations of the result. There should be at least 2 figures embedded in this section. It can be screenshots of your game, or plots generated by your data visualization code. Make sure these figures have appropriate titles and captions, and are sufficiently explained in your text.

System output: 
- scatterplots that indicate the correlation between the different song characteristics
- correlation coefficients of the scatterplots
- prediction models of the characteristics illustrating the strongest correlations 

How to Run:
1. Import data frame
2. Drop "song_name" subset because this cannot be plotted as a string 
3. Use the scatterplot_matrix function, dropping "song_name" as well as "song_popularity". This should result in a matrix of scatterplots that compare all the characteristics in the data frame with each other. The scatterplots can be interpretted by looking at the coeficcients listed at the bottoms of each graph as well as the visual pattern of the plots. If the absolute value of the correlation coefficient is between 0.3 and 0.7, this means there is a moderate correlation. Above 0.7 indicates a strong correlation and below 0.3 indicates no significant correlation.
![step 3](https://user-images.githubusercontent.com/114321320/205517811-5ad2978a-475d-4584-b89d-0ee519b2e8dc.png)



4. Use the strongest_correlation function to filter out the characteristcs with no significant correlation. The expected outputs are 4 scatterplots comparing acoutsticness and energy, acoutsticness and loudness, energy and loudness, and instrumentalness and loudness. 


5. Call the bestmodel function of each of the strongest_correlation results. The expected outputs are scatterplots with the actual data along with 1 linear regression model and second degree polynomial model. The function will also output the function of the better prediction model, printing out the equation.
  

Scope and limitations, including ethical implications, accessibility concerns, and ideas for potential extensions.

References and acknowledgement.

Background and source of the dataset:
This dataset is referred from Kaggle, and was created by M. Yasser H. 
[link](https://www.kaggle.com/datasets/yasserh/song-popularity-dataset/discussion?resource=download)

(If appropriate) links to any tutorials you used, and at least 3 specific things you implemented that differentiates your project from what’s already in the tutorial.
