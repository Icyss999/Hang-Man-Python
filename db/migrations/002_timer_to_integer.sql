BEGIN TRANSACTION;


CREATE TABLE events_new (
    id TEXT PRIMARY KEY NOT NULL,
    user_id TEXT NOT NULL,
    timer INTEGER NOT NULL, 
    score INTEGER NOT NULL,
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (user_id) REFERENCES users(id) 

);

INSERT INTO events_new (id,user_id,timer,score,created_at,updated_at) 
SELECT id,user_id,timer,score,created_at,updated_at FROM events;



DROP TABLE events;


ALTER TABLE events_new RENAME TO events;

CREATE INDEX idx_events_timer_and_score ON events(timer ASC,score DESC);
CREATE INDEX idx_events_user_id ON events(user_id);

COMMIT; 
