-- Script that lists all cities contained in the database hbtn_0d_usa
FROM cities JOIN states
ON cities.state_id = states.id;
