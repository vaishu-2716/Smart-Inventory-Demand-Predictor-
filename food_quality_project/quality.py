import psycopg2

conn = psycopg2.connect(
    database="food_quality_db",
    user="postgres",
    password="your_password",   # 👈 change this
    host="localhost",
    port="5432"
)

cur = conn.cursor()

# Query to get failed products
cur.execute("""
SELECT p.name, q.status, q.defects
FROM quality_checks q
JOIN batches b ON q.batch_id = b.batch_id
JOIN products p ON b.product_id = p.product_id
WHERE q.status = 'Fail';
""")

rows = cur.fetchall()

print("Defective Products:\n")

for row in rows:
    print(f"Product: {row[0]}, Status: {row[1]}, Issue: {row[2]}")

conn.close()