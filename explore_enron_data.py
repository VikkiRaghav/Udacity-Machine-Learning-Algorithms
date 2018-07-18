#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

count = 0
for i in range(len(enron_data)):
    a = enron_data.values()     # print total poi in the dataset
   if a[i]['poi'] == True:
        count = count + 1
print count

with  open('poi_names.txt', 'r') as f:   #print total number of persons in the text file
    print sum(1 for _ in f)

stock = enron_data['PRENTICE JAMES']['total_stock_value']   # total stock of value James Prentice
print stock

messages = enron_data['COLWELL WESLEY']['from_this_person_to_poi'] # total messages of Wesley Colwell
print messages


options = enron_data['SKILLING JEFFREY K']['exercised_stock_options']
print options    # total stock options of Jeffrey Skilling
count_salary = 0
count_email = 0


for i in enron_data.keys():
    if enron_data[i]['salary'] != 'NaN':
          count_salary = count_salary + 1
                                             # total quantified salary and email addresses in the dataset
for j in enron_data.keys(): 
    if enron_data[j]['email_address'] != 'NaN':
          count_email = count_email + 1

 print count_salary
 print count_email

count_payments = 0
total_count=0
for i in enron_data.keys():
    if enron_data[i]['total_payments'] == 'NaN':
       count_payments = count_payments + 1

print count_payments
print float(count_payments)/len(enron_data.keys()) #percentage of total payments which have no value as a part of the total dataset

new_poi=0
new_count = 0

for count in enron_data.keys():
    if enron_data[count]['poi'] != 'Nan':
        new_poi = new_poi + 1

for no in enron_data.keys():
    new_count = new_count + 1

print new_poi + 10          # new pois and new dataset number afer adding additional pois
print new_count + 10
