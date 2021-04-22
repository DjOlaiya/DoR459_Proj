# CMP 459 - Introduction to Data Mining - Spring 2021, SFU
**Prof** - Martin Ester

**TAs** - Madana Krishnan V K, Arash Khoeini

This repository consists of the dataset to be used for the course project. The dataset revolves around the novel COVID-19 pandemic that has emerged and taken the world by storm. The first file contains the data for individual cases and the second file contains the number of cases based on location. The 2 files are obtained from an open-source repository (link below) and have been processed to make it easier to use. To ensure consistency, the dataset has been frozen to September 20th, 2020.

* https://github.com/beoutbreakprepared/nCoV2019
* https://github.com/CSSEGISandData/COVID-19


Total runtime to train all three models on the whole data set took 5 hours on an i7 9700k, with RTX 2070 SUPER, and 32gbs of RAM

Packages we use are:

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import sklearn.model_selection as model_selection
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
import xgboost as xgb
from sklearn.metrics import confusion_matrix
import pickle

