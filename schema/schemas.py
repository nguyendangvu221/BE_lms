def individual_serial(document)-> dict:
    return {
        'id': str(document['_id']),
        'name': document['name'],
        'author': document['author'],
        'category': document['category'],
        'publisher': document['publisher'],
        'description': document['description'],
        'numberOfPage': document['numberOfPage'],
        'reprint': document['reprint'],
        'numberOfEditions': document['numberOfEditions'],
        'language': document['language'],
        'releaseDate': document['releaseDate'],
        'image': document['image'],
        'pdf': document['pdf'],
        'namePoster': document['namePoster'],
        'idPoster': document['idPoster'],
    }
def list_serial(documents) -> list:
    return [individual_serial(document) for document in documents]
