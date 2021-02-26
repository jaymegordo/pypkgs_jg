import pandas as pd
from pypkgs_jg import __version__
from pypkgs_jg import pypkgs_jg as pj


def test_version():
    assert __version__ == '0.1.0'

def test_catbind():
    a = pd.Categorical(["character", "hits", "your", "eyeballs"])
    b = pd.Categorical(["but", "integer", "where it", "counts"])
    c = pd.Categorical(["macgrubie", "dont", "play", "like", "homie"])
    cat = pj.catbind(a, b, c)

    assert (cat.codes == [1,  5, 12,  4,  0,  7, 11,  2,  9,  3, 10,  8,  6]).all()
    
    assert (cat.categories == ['but', 'character', 'counts', 'dont', 'eyeballs', 'hits', 'homie', 'integer', 'like', 'macgrubie', 'play', 'where it', 'your']).all()
