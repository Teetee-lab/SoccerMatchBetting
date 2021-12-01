# SoccerMatchBetting

![Betting Image](https://news.wagertalk.com/wp-content/uploads/2018/07/soccer_money.jpg)

## Business Problem
Forecasting sports events like matches or tournaments has attracted the interest of different communities all over the world for quite a long time and sport events like soccer matches take place regularly, which generate huge public attention. Winning soccer matches is becoming an essential aspect of soccer clubs and soccer fans. Also, The global sport gambling system is multi trillion dollar rich while there are billions of soccer fans that gamble everyday without yielding a return. My aim is to educate these set of people, to make a better decision using my model to predict the soccer game before making a bet.  with that, they can minimize loss and yield high returns.

## Data Overview
The dataset was obtained  from https://projects.fivethirtyeight.com/soccer-predictions/ , and the soccer archive odds was downloaded from  https://www.kaggle.com/sashchernuh/european-football. 
- The first dataset is organized into four folders with a total of 66542rows and 27columns.
    - spi global rankings intl
    - spi global rankings
    - spi matches latest
    - spi matches    

- the second dataset is organized into one folder with a total of 12674 rows and 13columns.
    - Football data 

- After cleaning and merging the two dataset I end up with a 24750rows and 27columns.
     - Data cleaning notebook can be found in the notebook folder.
        - Data cleaning process;
          * remove unused leagues from each data csv file.
          * change the date to python datetime.
          * split the season date, in order to use just the year. 
          * drop the season column, and create a new one.
          * fill nan with zeros for the bet365 column, which I end up dropping due to less values.
          * drop nan for the scores to avoid bias information.
          
- Create the target from the home and away scores, with that I have a multiclass category (Draw/HomeWin/AwayWin).


## Project Result
- There was a monotonic trend performance with the accuracy score of all the models. As one increases the other decreases, which is due to the complexity of soccer games. After tuning several models, the Logistic Regression model was the best performing model in classifying the business problem. The model achieved an accuracy score of 60% on unseen data, weighted average score at 53% with a probability of loss at -0.9. The macro-average area under the curve is 0.74 and the micro average area under the curve is 0.77.

## Conclusions
- My recommendation will be to take into consideration each team's soccer power index before using the model to predict the match. To make it simple, using the model to predict a match before betting will give you more relevant information about each team's quality and more valuable insights to their performance analysis than studying the results afterwards.

- The stakeholder can use the model to predict upcoming match fixtures, but will advise to backup bets, if the model predicts a win class, back it up with a draw class because soccer is a tricky sport to model due to few goals scored in each match.


## Next Steps
- **Deep Learning Approach:** I have only used the supervised learning approach in the process of developing the machine learning model. In the future, I would like to incorporate unsupervised learning techniques like deep learning to improve the accuracy of the model. 

- **Team players performance:** I would like to include the soccer players, their physical performance and capabilities in the future analysis that will help improve the accuracy of the model.

- **Fifa World Cup soccer:** Since I only base my study on seven leagues. In the future, I will like to add more leagues and continue to update the model using the world cup data.


## Repository Structure

```
├── Images                              <- Folder containing graphs and images
│   
├── notebooks                           <- Directory containing project  notebooks
│   ├── Data Cleaning.ipynb      	<- documentation of the data cleaning in Jupyter notebook            
│   ├── EDA.ipynb        		<- documentation of the EDA and visualization in Jupyter  notebook         
│   └── Models.ipynb               	<- documentation of different models in Jupyter notebook  
│   ├── SoccerMatchBetting.ipynb       <- Narrative documentation of the project in Jupyter notebook
├── model.sav
├── Presentation   <- PDF version of project presentation
└── README.md                             <- Top-level README
``` 

## AUthor
- Titilayo Amuwo(Teetee)

