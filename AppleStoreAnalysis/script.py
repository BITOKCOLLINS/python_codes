#opened_file = open('AppleStore.csv')
opened_file = open('AppleStore.csv', encoding='utf-8')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

rating_sum=[]
for row in apps_data[1:]:
    rating= float(row[8])
    rating_sum.append(rating)
    
#print(rating_sum)
avg_rating=sum(rating_sum)/len(rating_sum)
print(avg_rating)
''' #Using if statements
free_apps_ratings = []
for row in apps_data[1:]:
    rating = float(row[8])
    price = float(row[5])

    if price==0.0:
        free_apps_ratings.append(rating)
        
avg_rating_free= sum(free_apps_ratings)/len(free_apps_ratings)
print(avg_rating_free) '''