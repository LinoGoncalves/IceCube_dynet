import kaggle

kaggle.api.authenticate()
kaggle.api.competition_submit("path/to/notebook.ipynb", "submission message", "competition-name")
