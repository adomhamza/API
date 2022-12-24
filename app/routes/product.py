from typing import List
from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, schema
from ..database import get_db


router = APIRouter(prefix="/product", tags=["Product"])


@router.post(
    "", status_code=status.HTTP_201_CREATED, response_model=models.ResponseProductModel
)
def create_product(product: models.Product, db: Session = Depends(get_db)):
    products = schema.Product(**product.dict())
    db.add(products)
    db.commit()
    db.refresh(products)
    return products


@router.get(
    "", status_code=status.HTTP_200_OK, response_model=List[models.ResponseProductModel]
)
def get_all_products(db: Session = Depends(get_db)):
    products = db.query(schema.Product).all()
    if not products:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Nothing here"
        )

    return products


@router.delete("/{product_id}", status_code=status.HTTP_404_NOT_FOUND)
def delete_product(product_id: int, db: Session = Depends(get_db)):
    deleted = db.query(schema.Product).filter(schema.Product.product_id == product_id)

    if deleted.first() is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Product not found"
        )
    deleted.delete(synchronize_session=False)
    db.commit()
    return "Product deleted successfully"


# Updates specific product by product_id


@router.put(
    "/{product_id}",
    status_code=status.HTTP_200_OK,
    response_model=models.ResponseProductModel,
)
def update_product(
    product_id: int, product: models.Product, db: Session = Depends(get_db)
):
    update = db.query(schema.Product).filter(schema.Product.product_id == product_id)

    if update.first() is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"{product_id} not found"
        )
    update.update(product.dict(), synchronize_session=False)
    db.commit()
    return "Product updated successful"
