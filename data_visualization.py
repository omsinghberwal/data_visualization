import csv
import matplotlib.pyplot as plt
import datetime


data = []
with open('data.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:

        row['Date'] = datetime.datetime.strptime(row['Date'], '%Y-%m-%d')
        row['Value'] = float(row['Value'])
        data.append(row)

dates = [row['Date'] for row in data]
values = [row['Value'] for row in data]
categories = [row['Category'] for row in data]

print(data[:5])


plt.figure(figsize=(10, 5))
plt.plot(dates, values, marker='o')
plt.title('Line Plot of Values Over Time')
plt.xlabel('Date')
plt.ylabel('Value')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


plt.figure(figsize=(10, 5))
category_counts = {category: categories.count(category) for category in set(categories)}
plt.bar(category_counts.keys(), category_counts.values())
plt.title('Bar Chart of Categories')
plt.xlabel('Category')
plt.ylabel('Frequency')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
