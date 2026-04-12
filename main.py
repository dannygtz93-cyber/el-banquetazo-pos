from src.database.models import create_tables, seed_products

def main():
    create_tables()
    seed_products()

if __name__ == "__main__":
    main()