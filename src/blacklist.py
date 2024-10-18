import pandas as pd

def load_blacklist(file_path):
    return pd.read_csv(file_path)

def is_blacklisted(url, blacklist):
    return url in blacklist['urls'].values
