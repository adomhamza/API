from fastapi import FastAPI
from . import schema
from .routes import user, product, auth
from .database import engine


# import app.db_conn as db

schema.Base.metadata.create_all(bind=engine)

tags_metadata = [
    {
        "name": "User",
        "description": "Operations with users. The logic is also here.",
    },
    {
        "name": "Product",
        "description": "Manage _products_.",
        "externalDocs": {
            "description": "Items external docs",
            "url": "https://fastapi.tiangolo.com/",
        },
    },
]

app = FastAPI(title="Ecommerce API", openapi_tags=tags_metadata)
app.include_router(user.router)
app.include_router(product.router)
app.include_router(auth.router)


@app.get("/")
async def root():
    return {"message": "Hello"}


# @app.get('/users', status_code=status.HTTP_200_OK)
# def get_users():
#     db.cursor.execute(sql.SQL("SELECT * FROM {}".format('users')))
#     users = db.cursor.fetchall()
#     # print(users)
#     return {'users': users}


# @app.get('/users/{phone_number}', status_code=status.HTTP_200_OK)
# def get_user(phone_number: int):
#     db.cursor.execute(
#         sql.SQL(
#             "SELECT * FROM {} WHERE users.phone_number = {}"
# .format('users', phone_number))
#     )
#     users = db.cursor.fetchone()
#     if not users:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f'{phone_number} Not found')
#     return {'user': users}


# @app.post('/create', status_code=status.HTTP_201_CREATED)
# def create_user(user: User):
#     db.cursor.execute(
#         sql.SQL(
#             "INSERT INTO {}
# (email,password,first_name,last_name,phone_number)
# VALUES (%s,%s,%s,%s,%s)")
#         .format(
#             sql.Identifier('users')),
#         (user.email, user.password, user.first_name,
#          user.last_name, user.phone_number)
#     )
#     db.conn.commit()
#     return {'user': user}


# @app.delete('/delete/{phone_number}', status_code=status.HTTP_200_OK)
# def delete_user(phone_number: int):
#     db.cursor.execute(
# sql.SQL('DELETE FROM {} WHERE phone_number= %s RETURNING *').format(
#         sql.Identifier('users')), (phone_number,))
#     deleted = db.cursor.fetchone()
#     db.conn.commit()

#     if deleted is None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"{phone_number} does not exist.")

#     # return Response(status_code=status.HTTP_204_NO_CONTENT)
#     return {'user': deleted}


# @app.put('/put/{phone_number}')
# def update_user(phone_number: int, user: User):
#     db.cursor.execute(
# sql.SQL('
# UPDATE {} SET email=%s, password=%s, first_name=%s, last_name=%s,
# phone_number=%s WHERE phone_number=%s RETURNING *')
# .format(
#         sql.Identifier('users')),
#         (user.email, user.password, user.first_name,
# user.last_name, user.phone_number, phone_number))
#     update = db.cursor.fetchone()

#     db.conn.commit()

#     if update is None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"{phone_number} not found")

#     return {'user': update}
