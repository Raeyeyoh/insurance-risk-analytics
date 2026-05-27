from scipy.stats import ttest_ind


def run_ttest(group_a, group_b):

    t_stat, p_value = ttest_ind(
        group_a,
        group_b,
        nan_policy="omit"
    )

    return t_stat, p_value
