import kaggle

kaggle.api.authenticate()
kaggle.api.competition_submit("https://github.com/LinoGoncalves/IceCube_dynet/blob/main/graphnet-baseline-submission.ipynb", "submission via Github", "IceCube Neutrinos")
