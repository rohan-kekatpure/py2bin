from sklearn.ensemble import GradientBoostingRegressor
from sklearn.externals import joblib


def gbm_regressor(X, y):
    gbm = GradientBoostingRegressor(n_estimators=50)
    gbm.fit(X, y)
    joblib.dump(gbm, "gbm_regressor.pkl")

