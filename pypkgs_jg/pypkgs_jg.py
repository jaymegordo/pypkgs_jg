import pandas as pd


def catbind(*args):
    concatenated = pd.concat([pd.Series(arg.astype('str')) for arg in args])
    return pd.Categorical(concatenated)