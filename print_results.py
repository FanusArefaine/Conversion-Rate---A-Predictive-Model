# A function to print results based on the combinations of model parameter

def print_results(results):

    print("Best Params: {}\n".format(results.best_params_))   
    means = results.cv_results_['mean_test_score']
    stds = results.cv_results_['std_test_score']
    
    for mean, std, params in zip(means, stds, results.cv_results_['params']):
        print('{} (+/-{}) for {}'.format(round(mean,3), round(std*2, 3), params))