from fastapi import APIRouter, HTTPException, Query

from models.document import Document
from config.database import collection_document
from schema.schemas import list_serial,individual_serial
from bson import ObjectId

router = APIRouter()

@router.get("/documents")
async def get_all_documents():
    documents = collection_document.find()
    return list_serial(documents)

# @router.get("/documents/{id}")
# async def get_document_by_id(id: str):
#     if not ObjectId.is_valid(id):
#         raise HTTPException(status_code=400, detail="Invalid ObjectId format")

#     document = collection_document.find_one({"_id": ObjectId(id)})
#     if not document:
#         raise HTTPException(status_code=404, detail="Document not found")

#     return individual_serial(document)

@router.get("/documents/category")
async def get_document_by_category(category):
    document = collection_document.find({"category":category})
    return list_serial(document)

@router.post("/documents")
async def create_document(document: Document):
    collection_document.insert_one(dict(document))
    return document

@router.get("/documents/search")
async def search_documents(
    name: str = Query(..., title="Search Query", description="Search documents by name")
):
    query = {"$or": [{"name": {"$regex": f".*{name}.*", "$options": "i"}},
                     {"author": {"$regex": f".*{name}.*", "$options": "i"}}]}

    documents = collection_document.find(query)
    return list_serial(documents)

from fastapi import Query

@router.get("/documents/search/byPosted")
async def search_documents_by_user_id(
    user_id: str = Query(..., title="User ID", description="Filter documents by user ID"),
    query_text: str = Query(None, title="Query Text", description="Search by either name or author"),
):
    query = {"idPoster": user_id}

    if query_text:
        query["$or"] = [
            {"name": {"$regex": f".*{query_text}.*", "$options": "i"}},
            {"author": {"$regex": f".*{query_text}.*", "$options": "i"}},
        ]

    documents = collection_document.find(query)
    return list_serial(documents)


@router.patch("/documents/{id}")
async def update_document(id, document: Document):
    collection_document.find_one_and_update({"_id":ObjectId(id)}, {"$set":dict(document)})
    return document

@router.delete("/documents/{id}")
async def delete_document(id):
    collection_document.find_one_and_delete({"_id":ObjectId(id)})
    return {"message":"Document with id {} has been deleted successfully.".format(id)}

@router.delete("/users/{id}")
async def delete_user_and_documents(id):
    # Xóa tất cả các tài liệu có idposter bằng id của người dùng
    deleted_result = collection_document.delete_many({"idPoster": id})
    
    if deleted_result.deleted_count > 0:
        return {"message": f"User with id {id} and associated documents have been deleted successfully."}
    else:
        return {"message": f"No documents found for user with id {id}."}

