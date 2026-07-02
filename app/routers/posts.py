from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List
from .. import models, schemas
from ..database import get_db

router = APIRouter(
   prefix = "/posts", 
   tags = ["posts"]
)

# 1.GET ALL POSTS
@router.get("/",response_model=List[schemas.Post])
def get_posts(db:Session = Depends(get_db)):
   # cursor.execute("""SELECT * FROM posts""")
   # posts = cursor.fetchall()
   
   posts = db.query(models.Post).all()
   return {"data":posts}

# 2.CREATE A POST
@router.post("/",status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
def create_posts(post: schemas.PostCreate,
                 db:Session = Depends(get_db)):
   new_post = models.Post(**post.dict())
   db.add(new_post)
   db.commit()
   db.refresh(new_post)
   return new_post

# 3.GET ONE POST BY ID() anytime we know there should be one .first() should be used

@router.get("/{id}",response_model=List[schemas.Post])
def get_idpost(id: int, db: Session = Depends(get_db)):
   post = db.query(models.Post).filter(models.Post.id == id).first()
   print(post)

   if not post:
     raise HTTPException(
        status_code =status.HTTP_404_NOT_FOUND,
        detail=f"post with is: {id} was not found"
       )
   return post

# 4.DELETE A POST

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db)):

    post= db.query(models.Post).filter(models.Post.id == id)

    if post.first() == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with id {id} does not exist"
        )

    post.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.put("/{id}", response_model=schemas.Post)
def update_post(id:int, updatedpost:schemas.PostCreate , db: Session = Depends(get_db)):
   post_query = db.query(models.Post).filter(models.Post.id == id)
   post = post_query.first()

   if post== None:
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"post with id : {id} does not exist"
    )

   post_query.update(updatedpost.dict(), synchronize_session=False)
   
   db.commit()

   return post_query.first()
