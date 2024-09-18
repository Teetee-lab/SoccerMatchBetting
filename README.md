# SoccerMatchBetting

[Match prediction App](https://soccer-match-predictor-app.herokuapp.com/)

![Betting Image](./Images/soccermatchbet.png)

## Business Problem
- Forecasting sports events like matches or tournaments has attracted the interest of different communities all over the world for quite a long time and sports events like soccer take place regularly because they generate huge public attention. Winning soccer matches is becoming an essential aspect of soccer clubs and soccer fans. While the global sports gambling system is multi-billion dollar rich, there are billions of soccer fans that gamble every day without yielding a return. Therefore, my aim in this project is to build a machine learning algorithm for soccer fans to predict a match wisely and minimize loss.

## Data Overview
The dataset was obtained from FiveThirtyEight, and the soccer archive odds were downloaded from Kaggle. 

- The first dataset is organized into four folders and was downloaded from FiveThirtyEight
  - spi global rankings intl
  - spi global rankings
  - spi matches latest
  - spi matches
- The second dataset is organized into one folder.
  - This was an archive folder that was downloaded from Kaggle
  
- After that, I cleaned and merged the two datasets and the exploratory data analysis can be found in the [notebook folder](https://github.com/Teetee-lab/SoccerMatchBetting/blob/main/Notebooks/DataCleaning.ipynb)         
- Finally, I created the target from the home and away scores, and with that, I have a multiclass category of (Draw/HomeWin/AwayWin).

- Project library dependencies can be found [here](https://github.com/Teetee-lab/SoccerMatchBetting/blob/main/environment.yml)

## Project Results
- There was a monotonic trend performance with the accuracy score of all the models. As one increases the other decreases, which is due to the complexity of soccer games. However, after tuning the models, the logistic regression algorithm was performing at its best in classifying the soccer dataset. The model achieved an accuracy score of 60% on unseen data, and a weighted average score of 54% with a probability of loss at -0.9. The macro-average area under the curve is 74% and the micro average area under the curve is 78%.

## Conclusions
- Take into consideration each team's soccer power index before using the model to predict the match. Using the model as a tool to predict a match before betting will give you more relevant information about each team's quality and more valuable insights into their performance analysis than studying the results afterward.

- The model can be used to predict upcoming match fixtures, however, I will advise stakeholders to back up bets, if the model predicts a Win, back it up with a Draw because soccer is a complex sport to model due to the few goals that are scored in the game.


## Next Steps
- Deep Learning Approach: I have only used the supervised learning approach in the process of developing the algorithm. I would like to incorporate unsupervised learning techniques like deep learning to improve the accuracy of the model.

- Team player's performance: I would like to include the soccer players' physical performance and capabilities.

- Fifa World Cup soccer: I would like to add more leagues and continue to update the model using other soccer data.

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
├── app.py                      <- Streamlit documentation
├── model.sav
├── environment.yml             <- environment libraries 
├── requirement.txt             <- text file of libraries and dependency
├── setup.sh                    <- Streamlit config
├── Procfile
├── Presentation.pdf            <- PDF version of project presentation
└── README.md                   <- Top-level README
``` 


## AUthor
- Titilayo Amuwo(Teetee)

