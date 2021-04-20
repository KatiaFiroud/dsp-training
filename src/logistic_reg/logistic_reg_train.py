import pandas as pd
from sklearn.linear_model import LogisticRegression
from joblib import dump
import logging

import src.constants.columns as c


def logistic_reg_train(preprocessed_train_path, logistic_reg_model_path):
    """
    Read preprocessed train data, instantiate model, fit on train data and save model.

    :param preprocessed_train_path: path to preprocessed training data.
    :param logistic_reg_model_path: path to saved logistic reg model.

    :return: None
    """
    train_df = pd.read_csv(preprocessed_train_path)

    logistic_reg = LogisticRegression()
    
    logistic_reg.fit(
        train_df.drop(c.Loans.target(), axis=1).values,
        train_df[c.Loans.target()].values
    )

    logging.info("Saving model")
    dump(logistic_reg, logistic_reg_model_path)
