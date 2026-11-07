from db.index import get_db
import uuid

db = get_db()
def is_valid_uuid(uuid):
    try:
        uuid.UUID(str(uuid))
        return True
    except ValueError:
        return False


def store_user (user_name):
    

    # Edge case for bad input from user
    if user_name == None or len(user_name) == 0:
        raise ValueError("Name cannot be empty")
    if len(user_name) > 100:
        raise ValueError("It is impossible for a name to be longer than 100 characters!")
    
    existing_name = db.execute("""
    SELECT * 
    FROM users 
    WHERE name = ?
    LIMIT 1
    """,(user_name,)).fetchone()

    if existing_name:
        raise ValueError("Name is already taken, please choose other name")
    # Ill generate user id in uuid format rather than auto increment which is easily guessed
    user_id = str(uuid.uuid4())
    # insert user_name into user row 
    name_insert_row = db.execute("""
    INSERT INTO users (id,name)
    VALUES (?,?)
    RETURNING *
    """,(user_id,user_name)).fetchone()

    db.commit()
    return dict(name_insert_row)


# def fetch_user_id ():
#
#     return
#
def store_game_event(user_id, timestamp,score):

    if (not is_valid_uuid(user_id)):
        raise ValueError("Invalid user_id")

    if (timestamp == None or not isinstance(timestamp,int) or timestamp < 0):
        raise ValueError("Invalid duration")

    if (score == None or not isinstance(score,int) or score < 0):
        raise ValueError("Invalid score input")
    

    event_id = str(uuid.uuid4())

    event_insert = db.execute("""
    INSERT INTO events (id,user_id,timer,score)
    VALUES (?,?,?,?)
    RETURNING *
    """,(event_id,user_id,timestamp,score)).fetchone()

    db.commit()
    return dict(event_insert)


def display_leaderboard():
    data_row = db.execute("""
    SELECT events.id,users.id,users.name,events.timer, events.score
    FROM events
    JOIN users ON events.user_id = users.id
    ORDER BY events.timer ASC, events.score DESC
    LIMIT 10   
    """).fetchall()

    if len(data_row) == 0:
        raise ValueError("There's no player available")

    
    return [dict(r) for r in data_row]

# def fetch_user_game_history(user_id):
#     return



