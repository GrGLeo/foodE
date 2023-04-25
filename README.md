# FoodE
# LeWagon Project batch 1004

## Goal

Tracking calories can be a complicated task, as of now, we need to scan every ingredients that goes in our recipe to get the nutrients value per 100G, and then scale each ingredient to get the nutients value for our meal.
The goal here, is to simplify this task. By taking a picture of the meal, we can get the complete nutritional information of the dish.

## Data

Our data, come from the Kaggle Dataset food101, it contain 101 dishes and for each one we have 1000 pictures, all pictures have been labeled with the correct recipe associated.
We have split this data into a train and test set. Taking 800 picture per dish for the training set and 200 for the test set.

## Transfer learning & training the model

We have selected a certain number of already existing pre trained model, InceptionV3, EfficientNetB2, ResNet50, VGG16, MobilNEtV2 and we also build our own CNN.
We then started training all of these model, with fixed hyper parameter. To see if some model would perform better then others on this task.
Two model were above the others, EfficientNetB2 and ResNet50.
We then started tunning some hyperparameters for those two model.

We end up with an accuracy of 82% on the test set with EfficientNetB2.

## Getting the macronutrients value

Once we were able to correctly detect the recipe from the picture, we still had to get the macronutrients value.For this part we use an API.
The predicted recipe would have several dishes associated from the API, for simplicity for this project we simply choose to take the mean value for all the macronutrients. 

At this point we had from one picture a recipe and all macronutrients values.

## UI for the diary journal

We used streamlit to create our interface and BigQuery to store the data and user information.

## Testing on your own

