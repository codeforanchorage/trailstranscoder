-- Create lookup table for trail usage

CREATE TABLE usage_flags (
    flag INTEGER PRIMARY KEY ASC,
    name VARCHAR);

-- Insert some defaults into usage_flags
INSERT INTO usage_flags
VALUES
    (1, 'Run/Walk'),
    (2, 'Bike'),
    (4, 'Ski'),
    (8, 'Snowshoe'),
    (16, 'Skijor'),
    (32, 'Mush'),
    (64, 'On-leash Dogs'),
    (128, 'Off-leash Dogs')

