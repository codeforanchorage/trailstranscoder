-- Create lookup table for poi amenities

CREATE TABLE point_amenities_flags (
    flag INTEGER PRIMARY KEY ASC,
    name VARCHAR);

-- Insert some defaults into usage_flags
INSERT INTO point_amenities_flags
VALUES
    (1, 'Parking'),
    (2, 'Bathrooms'),
    (4, 'Shelter'),
    (8, 'Water'),
    (16, 'Refreshments'),
    (32, 'Scenic'),
    (64, 'Of Interest')

