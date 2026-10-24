import click

from abhishek.extensions import db
from abhishek.models import Product


@click.command("seed")
def seed_command() -> None:
    """Add sample products to the database."""
    sample_products = [
        {
            "name": "Laptop",
            "description": "A laptop for everyday work and study.",
            "price": "55000.00",
        },
        {
            "name": "Wireless Mouse",
            "description": "A wireless mouse for everyday use.",
            "price": "799.00",
        },
        {
            "name": "Mechanical Keyboard",
            "description": "A mechanical keyboard for comfortable typing.",
            "price": "3499.00",
        },
    ]

    added_count = 0

    for item in sample_products:
        existing_product = db.session.execute(
            db.select(Product).where(Product.name == item["name"])
        ).scalar_one_or_none()

        if existing_product is None:
            db.session.add(Product(**item))
            added_count += 1

    db.session.commit()
    click.echo(f"Seed completed. Added {added_count} new product(s).")
