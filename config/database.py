from pymongo import MongoClient
client = MongoClient("mongodb+srv://nguyendangvu221:Dangvu123@cluster0.ne1ulet.mongodb.net/?retryWrites=true&w=majority")

db = client.lms_db

collection_document = db["document"]
