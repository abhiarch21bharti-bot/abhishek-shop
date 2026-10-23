from flask import Blueprint, jsonify, render_template

from abhishek.extensions import db
from abhishek.models import Product

main_bp = Blueprint("main", __name__)


@main_bp.get("/health")
def health_check():
    return jsonify({"status": "ok"}), 200


@main_bp.get("/")
def product_list():
    products = (
        db.session.execute(db.select(Product).order_by(Product.id)).scalars().all()
    )

    return render_template("products.html", products=products)


@main_bp.get("/products/<int:product_id>")
def product_detail(product_id):
    product = db.get_or_404(Product, product_id)
    return render_template("product_detail.html", product=product)
