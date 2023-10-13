import numpy as np

def bootstrap_mean_confidence_interval(data, num_iterations, alpha=0.05):
    means = []

    for _ in range(num_iterations):
        # Resample with replacement
        resampled_data = np.random.choice(data, size=len(data), replace=True)
        resampled_mean = np.mean(resampled_data)
        means.append(resampled_mean)

    # Calculate the lower and upper percentiles
    lower_percentile = 100 * alpha / 2
    upper_percentile = 100 * (1 - alpha / 2)

    lower_bound = np.percentile(means, lower_percentile)
    upper_bound = np.percentile(means, upper_percentile)

    return lower_bound, upper_bound