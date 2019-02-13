**Connor Eaton**

**Metis: Project McNulty. January, 30, 2019.**

# Affective Audio
## Using logistic regression to classify vocal emotion

### Overview

Human and machine interaction is becoming increasingly foundational to our society. From highly efficent automated call centers to suprisingly intimate companion machines, learning how to conduct life along side machines will be one of the major advancements and challenges of the 21st century. One of the principal components of fostering this cultural transition will be building machines that can predict our emotions, however irrational and imcomprehensible they may sometimes seem. We generally understand  machines, so it would be good if they generally understood us. 

In this project, I built a classification model to predict positive or negative emotion in human speech.

### Data sources
The data source for this project will be the Crowd-sourced Emotional Mutimodal Actors Dataset (CREMA-D). It can be found here:

https://github.com/CheyneyComputerScience/CREMA-D/tree/master/docs

This data contains ~7,500 .mp3 files containing recordings of actors saying the same 12 sentences with six different emotions. Other tables containing demographic data per actor and emotional tone per file were merged with audio files and cleaned in a postgress database.

Numerous spectral features were extracted from waveforms (see below) as arrays from the raw mp3 files using the Librosa library. To prepare features for modeling, the mean and standard deviation was computed for each feature and merged into my postgreSQL database.

[![Screen-Shot-2019-02-12-at-10-32-36-AM.png](https://i.postimg.cc/RCkJ184d/Screen-Shot-2019-02-12-at-10-32-36-AM.png)](https://postimg.cc/yWTNsLJ3)

The final spectral features I included in my model were: chroma (standard deviation), contrast (mean), energy (mean), energy (standard deviation), MFCC (standard deviation), flatness (standard deviation), and zero cross rate (mean & standard deviation). My target was positive emotion (neutral/happy) and negative emotion (anger/disgust).

### Project Layout
All data cleaning and engineering was completed in postgress. For feature extraction and compilation, a .py script was written to input audio files and return a data frame of features. Modeling and visualizations were done in a .ipynb file. All of the above can be found in this repo.

### Tools
To compelte this project, I used python, jupyter notebooks, postgreSQL, pandas, numpy, matplotlib, scikit-learn, Ipython, Librosa, and XGBoost.

### Model and Results
I constructed a variety of models in this project, including Logistic Regression, K Nearest Neihbors, Random Forest, SVM, and XGBoost, all optimized with GridSearchCV. Parameters were tuned to optimize precision, which was my metric of concern so that my model limited false positives. XGBoost was chosen as my final model because it was the strongest performer across the board, with **precision and accuracy at .83.** 

### Future Work
The goal of this project was to build a binary classification model, however, this data is begging for multiclass classification. Notice in the image below how polar emotions like happiness and anger look farily similar compared to neutral and sadness in terms of spectral flatness? This illustrates a positive class emotion (happiness) appearing more similar to a negative class emotion (anger) than its fellow positve emotions (neutral). Forcing spectral features from emotions that we intuitively group together in similar classes may not be optimal for machine learning, and predicting a class for each emotion on its own may increase overall performance. 

[![Screen-Shot-2019-02-12-at-8-45-10-AM.png](https://i.postimg.cc/L51R6NW6/Screen-Shot-2019-02-12-at-8-45-10-AM.png)](https://postimg.cc/K3xC0rFd)

In addition, natural language processing and deep learning was outside of the scope of this project. This prevented me from diving into text, image, or video emotional analysis, which I am looking forward to diving into in the future.

### Final Thoughts
Even though I built a classification model to predict emotion with 83% accuracy, I’m not necessarily happy about it. Internally, I carry two polarizing perceptions of this technology, of which I have only scratched the surface. The romantic within me feels that the subjectivity, mystery, and power of emotion is one of the last frontiers of the human experience left unspoiled. If we strip emotion down to synapses and waveform statistics, will that degrade the potency of art, love, and beauty? However, the technologist in me envisions a future with human-centered AI, where our daily lives are full of interactions with emotionally perceptive machines that enhance the human experience. 

This is an amazing era to study the psychology and machine learning and I am so grateful to be somewhere in the middle. This intersection will greatly influence the way we interact with machines in the coming years, and I look forward to playing my role in shaping a meaningful future.

