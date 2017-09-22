SELECT languages.language, countries.name AS country FROM countries
JOIN languages ON languages.country_id = countries.id
WHERE language = "Spanish"



-- SELECT MAX(cities.population), cities.name, cities.district AS state FROM cities
-- WHERE country_code = "USA"
-- GROUP BY cities.district;

-- SELECT SUM(cities.population) AS population_sum, cities.district AS state FROM cities
-- WHERE country_code = "USA"
-- GROUP BY state
-- ORDER BY population_sum DESC;

-- SELECT COUNT(*)  FROM cities
-- JOIN countries ON cities.country_id = countries.id
-- WHERE countries.id = 42;
-- 
-- SELECT * FROM countries
-- ORDER BY population DESC LIMIT 1;