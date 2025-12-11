
"""
This file is responsible for making database queries, which your fastapi endpoints/routes can use.
The reason we split them up is to avoid clutter in the endpoints, so that the endpoints might focus on other tasks 

- Try to return results with cursor.fetchall() or cursor.fetchone() when possible
- Make sure you always give the user response if something went right or wrong, sometimes 
you might need to use the RETURNING keyword to garantuee that something went right / wrong
e.g when making DELETE or UPDATE queries
- No need to use a class here
- Try to raise exceptions to make them more reusable and work a lot with returns
- You will need to decide which parameters each function should receive. All functions 
start with a connection parameter.
- Below, a few inspirational functions exist - feel free to completely ignore how they are structured
- E.g, if you decide to use psycopg3, you'd be able to directly use pydantic models with the cursor, these examples are however using psycopg2 and RealDictCursor
"""


from db_setup import get_connection
from psycopg2.extras import RealDictCursor
from schemas import TreatmentCategoriesCreate, TreatmentsCreate


def add_treatments(item: TreatmentsCreate):
    conn = get_connection()
    if conn is None:
        return None
    with conn:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(
                """
                INSERT INTO treatments (treatment_name, treatment_description, category_id, time_duration, last_min_deal)
                VALUES (%s, %s, %s, %s, %s)
                RETURNING *; 
                """,
                (item.treatment_name, item.treatment_description, item.category_id, item.time_duration, item.last_min_deal),
            )
            inserted =  cur.fetchone()
            return inserted

def add_treatment_categories(item: TreatmentCategoriesCreate):
    conn = get_connection()
    if conn is None:
        return None
    #try:
    with conn:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(
                """
                INSERT INTO treatment_categories (category_name)
                VALUES (%s)
                RETURNING *; 
                """,
                (item.category_name,),
            )
            inserted = cur.fetchone()
            return inserted
    #except 


def get_treatment_categories():
    conn = get_connection()
    if conn is None:
        return None
    with conn:
        with conn.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute("SELECT * FROM treatment_categories;")
            treatment_categories = cursor.fetchall()
    return treatment_categories



### Fetching all data from TREATMENTS table
def get_treatments():
    conn = get_connection()
    if conn is None:
        return None
    with conn:
        with conn.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute("SELECT * FROM treatments;")
            treatments = cursor.fetchall()
    return treatments

    

### THIS IS JUST INSPIRATION FOR A DETAIL OPERATION (FETCHING ONE ENTRY)
# def get_treatment(con, item_id):
#     with con:
#         with con.cursor(cursor_factory=RealDictCursor) as cursor:
#             cursor.execute("""SELECT * FROM items WHERE id = %s""", (item_id,))
#             item = cursor.fetchone()
#             return item


### THIS IS JUST INSPIRATION FOR A CREATE-OPERATION
# def add_item(con, title, description):
#     with con:
#         with con.cursor(cursor_factory=RealDictCursor) as cursor:
#             cursor.execute(
#                 "INSERT INTO items (title, description) VALUES (%s, %s) RETURNING id;",
#                 (title, description),
#             )
#             item_id = cursor.fetchone()["id"]
#     return item_id
