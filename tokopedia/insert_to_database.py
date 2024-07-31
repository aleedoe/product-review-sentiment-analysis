import json

def read_json_file(file_path):

    with open(file_path, 'r') as f:
        data = json.load(f)
    return data

# Example usage:
file_path = 'tokopedia/detail-products.json'
data = read_json_file(file_path)
# print(data)

import mysql.connector

# Koneksi ke database MySQL
db = mysql.connector.connect(
    host="localhost",
    user="alie",
    password="kmzway76aa",
    database="product_review_sentiment_analysis_tokopedia"
)

# Membuat cursor untuk menjalankan perintah SQL
cursor = db.cursor()

# Data JSON
data_list = data

# Ekstraksi data ke dalam list of tuples
reviews_data = []
for data in data_list:
    reviews = data["data"]["productrevGetReviewImage"]["detail"]["reviews"]
    for review in reviews:
        feedbackID = review["feedbackID"]
        reviewText = review["reviewText"]
        rating = review["rating"]
        reviewTime = review["reviewTime"]
        reviews_data.append((feedbackID, reviewText, rating, reviewTime))

# Query untuk bulk insert
insert_query = """
INSERT INTO reviews (feedbackID, reviewText, rating, reviewTime)
VALUES (%s, %s, %s, %s)
ON DUPLICATE KEY UPDATE
reviewText = VALUES(reviewText),
rating = VALUES(rating),
reviewTime = VALUES(reviewTime)
"""

# Melakukan bulk insert
cursor.executemany(insert_query, reviews_data)

# Commit perubahan dan tutup koneksi
db.commit()
cursor.close()
db.close()

