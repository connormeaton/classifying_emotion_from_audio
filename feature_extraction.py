import numpy as np
import pandas as pd

# Audio feature extraction
import librosa as lb

# Visualization
import matplotlib.pyplot as plt
import librosa.display
# Render figures interactively in the notebook
get_ipython().run_line_magic('matplotlib', 'nbagg')

# Audio widget for playback
from IPython.display import Audio

# Importing files
from os import listdir
from os.path import isfile, join


def get_files(path):
    '''This function gets all files from a directory as strings in a list.
    The path used in this project is: /Users/cmeaton/Documents/code/ds/
    METIS/sea19_ds7_workingdir/Project_McNulty/CREMA-D/AudioMP3'''

    filenames = [f for f in listdir(path) if isfile(join(path, f))]
    return filenames

get_files('/Users/cmeaton/Documents/code/ds/
METIS/sea19_ds7_workingdir/Project_McNulty/CREMA-D/AudioMP3')


def extract_features(filename):
    '''Loading in audiofiles and extracting features. Features include:
        - mfcc = Mel-frequency cepstral coefficients. Commonly used for vocals.
        - centroid = Spectral Centroid. Represents mean value of frequency form.
        - flatness = Spectral flatness. Distinguishes noisy vs harmonic sound.
        - tempo = Spectral onset envelope. Describes rythm.
        - cens = Chroma Energy Normalized Statistics. Smooths frequency windows for matching.
        - energy = Root Mean Square Energy. Computes energy of each frame.
        - melspec = Mel-Scaled Spectrogram.
        - contrast = Spectral Contrast.
        - tonnetz = Tonnetz. Computes tonal centroid features.
        - chroma = Chromagram from waveform.
    '''

    # load in file. y is the waveform, sr is the sampling rate.
    y, sr = lb.load(filename)

    # Short-time Fourier transformation.
    stft = np.abs(lb.stft(y))
    S, phase = lb.magphase(np.abs(stft))

    # all features
    mfcc = np.mean(lb.feature.mfcc(y=y, sr=sr))
    centroid = np.mean(lb.feature.spectral_centroid(y=y, sr=sr))
    flatness = np.mean(lb.feature.spectral_flatness(y=y, S=S))
    tempo = np.mean(lb.feature.tempogram(y=y, sr=sr))
    cens = np.mean(lb.feature.chroma_cens(y=y, sr=sr))
    energy = np.mean(lb.feature.rmse(y=y))
    melspec = np.mean(lb.feature.melspectrogram(y=y, sr=sr))
    contrast = np.mean(lb.feature.spectral_contrast(y=y, sr=sr))
    tonnetz = np.mean(lb.feature.tonnetz(y=y, sr=sr))
    chroma = np.mean(librosa.feature.chroma_stft(S=stft, sr=sr))

    # Create a dict of features
    audio_features = {'filename': filename,
                     'mfcc': mfcc,
                     'centroid': centroid,
                     'flatness': flatness,
                     'tempo': tempo,
                     'cens': cens,
                     'energy': energy,
                     'melspec': melspec,
                     'contrast': contrast,
                     'tonnetz': tonnetz,
                     'chroma': chroma
                     }
    return audio_features


def make_df(extract_features):
    '''This function calls the extract_feature function on every file, putting each audiofile dict into
    a list and returns a df with each dict as a row.'''

    data = []
    for i in filenames:
        data.append(extract_features(i))
    df_features = pd.DataFrame(data)
    df_features.to_csv('features_data.csv', sep=',', encoding='utf-8')
    return df_features

make_df(extract_features)
