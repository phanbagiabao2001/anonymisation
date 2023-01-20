import pandas as pd
import numpy as np
from collections import Counter


def age_utility(df,df_anon):
    """
        This utility is information loss measure introduced by yaWCO2
    """
    sum = 0
    col = 'age'
    std = df[col].std()
    for i in range(len(df[col])):
        x = abs(df[col][i]-df_anon[col][i])
        y = np.sqrt(2)*std
        sum += x/y
    return sum/df.shape[0]

# function to compute covaricance of 2 vector
def cov(a, b):
    a_mean = np.mean(a)
    b_mean = np.mean(b)

    sum = 0

    for i in range(0, len(a)):
        sum += ((a[i] - a_mean) * (b[i] - b_mean))
    return sum / (len(a) - 1)


def overall_hits_utility(df, df_anon):
    """

    """
    utility = 0

    covariance_overall = cov(df.overall, df_anon.overall)
    covariance_hist = cov(df.hits, df_anon.hits)

    if covariance_overall>0:
        utility +=0.25*covariance_overall
    if covariance_hist>0:
        utility +=0.25*covariance_hist

    correlation_overall = df['overall'].corr(df_anon['overall'])
    correlation_hits = df['hits'].corr(df_anon['hits'])

    if correlation_overall >0:
        utility += 0.25*correlation_overall
    if correlation_hits>0:
        utility +=0.25*correlation_hits

    return utility

def information_loss_nationality(original_data, anonymized_data):
    """
    This function takes two arguments: the original data column nationality and the anonymized data column nationality
    """
    original_counts = Counter(original_data)
    anonymized_counts = Counter(anonymized_data)

    original_total = sum(original_counts.values())
    anonymized_total = sum(anonymized_counts.values())

    loss = 0
    for category in original_counts:
        if category in anonymized_counts:
            anonymized_prob = anonymized_counts[category] / anonymized_total
            original_prob = original_counts[category] / original_total
            loss += original_prob * (1 - anonymized_prob)
        else:
            original_prob = original_counts[category] / original_total
            loss += original_prob
    return loss


def main():
    df = pd.read_csv('dataset_origine.csv',sep=";")
    df_anon = pd.read_csv('data_anon.csv')
    util1 = age_utility(df,df_anon)
    util2 = overall_hits_utility(df,df_anon)
    util3 = information_loss_nationality(df['nationality'],df_anon['nationality'])
    final_score = (util1+util2+util3) /3
    print(final_score)

if __name__ == '__main__':
    main()











