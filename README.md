**Connor Eaton**

**Metis: Project McNulty. January, 30, 2019.**

# Affective Audio
## Using logistic regression to classify vocal emotion

### Overview

Human and machine interaction is becoming increasingly foundational to our society. From highly efficent automated call centers to suprisingly intimate companion machines, learning how to conduct life along side machines will be one of the major advancements and challenges of the 21st century. One of the principal components of fostering this cultural transition will be building machines that can perceive our emotions, however irrational and imcomprehensible they may sometimes seem. We generally understand  machines, so it would be good if they generally understood us.


### Proposal
In this project, I am proposing to build a logistic regression model to classify human speech audio files into positive or negative emotion classes.

### Data sources
The data source for this project will be the Crowd-sourced Emotional Mutimodal Actors Dataset (CREMA-D). It can be found here:

https://github.com/CheyneyComputerScience/CREMA-D/tree/master/docs

There are multiple files/directories within this data set that will be utilized for this project. I will mainly be using the directory containing ~7,000 .mp3 files containing recordings of actors saying the same sentences with different emotions. In addition, I will be using data that tags each individual .mp3 with 1 of 6 emotions.

### Feature Extraction & Analysis
There will be several steps to my analysis. First, features will be extracted from the raw mp3 files using the Librosa library. Then, a database with the extracted features along with data from other tables will be created and processed with SQL. Finally, I will create my model by training a logistic regresion algorithm on my data, which which classify whether or not an audio file will exhibit positive or negative emotion.

### Potential Features
Using Librosa, numerous features can be extracted from raw .mp3 files, such as Mel-frequency cepstrum coefficients (MFCCs). However, more research is needed into learning about the selection of audio features for human voice prior to building the model.
