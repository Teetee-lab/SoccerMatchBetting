# SoccerMatchBetting

[Match prediction App](https://soccer-match-predictor-app.herokuapp.com/)

![Betting Image]([)](https://jcccampsatmedford.org/wp-content/uploads/2020/03/soccer-ball-ss-img.jpg)

## Business Problem
Forecasting sports events like matches or tournaments has attracted the interest of different communities all over the world for quite a long time and sport events like soccer matches take place regularly, which generate huge public attention. Winning soccer matches is becoming an essential aspect of soccer clubs and soccer fans. Also, The global sport gambling system is multi trillion dollar rich while there are billions of soccer fans that gamble everyday without yielding a return. My aim is to educate these set of people, to make a better decision using my model to predict the soccer game before making a bet.  with that, they can minimize loss and yield high returns.

## Data Overview
The dataset was obtained  from https://projects.fivethirtyeight.com/soccer-predictions/, and the soccer archive odds was downloaded from  https://www.kaggle.com/sashchernuh/european-football. 

- The first dataset is organized into four folders and was downloaded from [here](https://projects.fivethirtyeight.com/soccer-predictions/)
  - spi global rankings intl
  - spi global rankings
  - spi matches latest
  - spi matches
- The second dataset is organized into one folder.
  - This was an archive folder that I downloaded using [DBsqlite](https://sqlitebrowser.org/)
  
- After that, I clean and merge the two dataset. The Data cleaning notebook can be found in the [notebook folder.](https://github.com/Teetee-lab/SoccerMatchBetting/blob/main/Notebooks/DataCleaning.ipynb)         
- Finally, I create the target from the home and away scores, with that I have a multiclass category (Draw/HomeWin/AwayWin).

- Environment details can be found [here](https://github.com/Teetee-lab/SoccerMatchBetting/blob/main/environment.yml)

## Project Results
- There was a monotonic trend performance with the accuracy score of all the models. As one increases the other decreases, which is due to the complexity of soccer games. After tuning several models, the Logistic Regression model was the best performing model in classifying the business problem. The model achieved an accuracy score of 60% on unseen data, weighted average score at 54% with a probability of loss at -0.9. The macro-average area under the curve is 0.74 and the micro average area under the curve is 0.78.

## Conclusions
- My recommendation will be to take into consideration each team's soccer power index before using the model to predict the match. To make it simple, using the model to predict a match before betting will give you more relevant information about each team's quality and more valuable insights to their performance analysis than studying the results afterwards.

- The stakeholder can use the model to predict upcoming match fixtures, but will advise to backup bets, if the model predicts a win class, back it up with a draw class because soccer is a tricky sport to model due to few goals scored in each match.


## Next Steps
- **Deep Learning Approach:** I have only used the supervised learning approach in the process of developing the machine learning model. In the future, I would like to incorporate unsupervised learning techniques like deep learning to improve the accuracy of the model. 

- **Team players performance:** I would like to include the soccer players, their physical performance and capabilities in the future analysis. that will help improve the accuracy of the model.

- **Fifa World Cup soccer:** Since I only base my study on seven leagues. In the future, I will like to add more leagues and continue to update the model using the world cup data.


## Repository Structure

```
├── Images                      <- Folder containing graphs and images
│   
├── notebooks                   <- Directory containing project  notebooks
│   ├── Data Cleaning.ipynb     <- documentation of the data cleaning in Jupyter notebook            
│   ├── EDA.ipynb        		    <- documentation of the EDA and visualization in Jupyter  notebook         
│   ├── Models.ipynb            <- documentation of different models in Jupyter notebook
│   └──Catboost info            <- A folder with catboost algorithm models and scores
├── SoccerMatchBetting.ipynb    <- Narrative documentation of the project in Jupyter notebook
├── app.py                      <- streamlit documentation
├── model.sav
├── environment.yml             <- environment libraries 
├── requirement.txt             <- text file of liabries and dependency
├── setup.sh                    <- streamlit config
├── Procfile
├── Presentation.pdf            <- PDF version of project presentation
└── README.md                   <- Top-level README
``` 


## AUthor
- Titilayo Amuwo(Teetee)

