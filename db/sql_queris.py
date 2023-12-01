CREATE_TABLE_REVIEW = """
    CREATE TABLE IF NOT EXISTS reviews
    (id INTEGER PRIMARY KEY AUTOINCREMENT,
    name_product VARCHAR(255),
    articul VARCHAR(255),
    info VARCHAR(255),
    city VARCHAR(255) NULL,
    photo_check TEXT,
    
    )
"""

INSERT_INTO_TABLE_REVIEW = """
    INSERT INTO reviews(name_product, arcticul, info, city, photo_check) VALUES (?, ?, ?, ?, ?)
"""

SELECT_CHECKS_REVIEWS = """
    SELECT * FROM reviews
"""