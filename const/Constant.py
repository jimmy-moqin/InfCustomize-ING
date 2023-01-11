import pickle as pkl


class Const(object):
    def __init__(self):
        with open("./const/towerNameZh.pkl",mode="rb") as f:
            self.towerNameZh = pkl.load(f)
        with open("./const/AbilityNameZh.pkl",mode="rb") as f:
            self.AbilityNameZh = pkl.load(f)
        with open("./const/game-values.pkl",mode="rb") as f:
            self.game_values = pkl.load(f)
        with open("./const/selectKeywordDict.pkl",mode="rb") as f:
            self.selectKeywordDict = pkl.load(f)
        with open("./const/attributesZh.pkl",mode="rb") as f:
            self.attributesZh = pkl.load(f)
        with open("./const/attributesEn.pkl",mode="rb") as f:
            self.attributesEn = pkl.load(f)
    
