CREATE TABLE crime (
    x INT,
    city VARCHAR NOT NULL,
	state VARCHAR NOT NULL,
	country VARCHAR NOT NULL,
	crime_index FLOAT,
	safety_index FLOAT,
    PRIMARY KEY (city)
);

SELECT * FROM crime

CREATE TABLE quality_life (
    rank INT,
    city VARCHAR NOT NULL,
	state VARCHAR NOT NULL,
	country VARCHAR NOT NULL,
	quality_of_life_index FLOAT,
	purchasing_power_index FLOAT,
	safety_index FLOAT,
	health_care_index FLOAT,
	cost_of_living_index FLOAT,
	property_price_to_income_ratio FLOAT,
	traffic_commute_time_index FLOAT,
	pollution_index FLOAT,
	climate_index FLOAT,
    PRIMARY KEY (city)
);

select * from quality_life;

CREATE TABLE property (
    rank INT,
    city VARCHAR NOT NULL,
	state VARCHAR NOT NULL,
	country VARCHAR NOT NULL,
	price_to_income_ratio FLOAT,
	gross_rental_yield_city_centre FLOAT,
	gross_rental_yield_outside_of_centre FLOAT,
	price_to_rent_ratio_city_centre FLOAT,
	price_to_rent_ratio_outside_of_city_centre FLOAT,
	mortgage_as_a_percentage_of_income FLOAT,
	affordability_index FLOAT,
    PRIMARY KEY (city)
);

select * from property;

DROP TABLE city_join;

SELECT p.city, p.state, p.country, c.crime_index, c.safety_index, 
	q_l.quality_of_life_index, q_l.purchasing_power_index, q_l.health_care_index, q_l.cost_of_living_index,
	q_l.traffic_commute_time_index, q_l.pollution_index, p.price_to_income_ratio, p.affordability_index
	INTO city_join
FROM crime AS c
JOIN quality_life AS q_l
ON c.city = q_l.city
	JOIN property AS p
	ON q_l.city = p.city;
	
select * from city_join