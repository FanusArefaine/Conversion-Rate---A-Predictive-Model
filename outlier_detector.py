
# A function to return the minimum outlier value

import numpy as np

outliers = list()

class outlier:

    def minoutlier(self, data):


        """ data_mean : calculate the mean of the data
            data_std : calculate the standard deviation of the data
        """

        data_mean = np.mean(data)
        data_std = np.std(data)

        for record in data:
            z_score = (record - data_mean)/ data_std
            # An outlier if the data record lies beyond the 3rd standard deviation
            if np.abs(z_score) > 3: 
                outliers.append(record)
        return min(outliers)


    def add(self, a, b):
        return a+b

        
    


