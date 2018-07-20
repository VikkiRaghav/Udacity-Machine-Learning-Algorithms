#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
     data = []
     size = len(predictions)
     for i in range(size):
         error = (predictions[i][0] - net_worths[i][0])*(predictions[i][0] - net_worths[i][0])
         data.append(ages[i][0], net_worths[i][0], error)
         data.sort(key=lambda tup: tup[2])
    
         cleaned_data = data[:81]

    ### your code goes here

    
         return cleaned_data

