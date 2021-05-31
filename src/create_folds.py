import pandas as pd
from sklearn.model_selection import train_test_split

if __name__ == '__main__':
    df = pd.read_csv('../input/Categorical Feature Encoding Challenge/train.csv')
    df['kfold'] = -1
    df = df.sample(frac=1).reset_index(drop = True)