-- 1. What query would you run to get the total revenue for March of 2012?

-- SELECT MONTHNAME(billing.charged_datetime) AS month, SUM(billing.amount) AS total_revenue
-- FROM billing
-- WHERE billing.charged_datetime >= "2012-03-01 00:00:00" AND billing.charged_datetime <= "2012-03-31 23:59:59"

-- 2. What query would you run to get total revenue collected from the client with an id of 2?

-- SELECT clients.client_id, SUM(billing.amount) AS total_revenue
-- FROM clients
-- JOIN billing ON clients.client_id = billing.client_id
-- WHERE billing.client_id = 2
 
-- 3. What query would you run to get all the sites that client=10 owns?

-- SELECT clients.client_id, sites.domain_name
-- FROM clients
-- JOIN sites ON clients.client_id = sites.client_id
-- WHERE clients.client_id = 10

-- 4. What query would you run to get total # of sites created per month per year for the client with an id of 1? What about for client=20?

-- SELECT clients.client_id, COUNT(sites.domain_name) AS websites, MONTHNAME(sites.created_datetime) AS month_created, YEAR(sites.created_datetime) AS year_created
-- FROM sites
-- JOIN clients on sites.client_id = clients.client_id
-- WHERE clients.client_id = 1
-- GROUP BY sites.domain_name

-- SELECT clients.client_id, COUNT(sites.domain_name) AS websites, MONTHNAME(sites.created_datetime) AS month_created, YEAR(sites.created_datetime) AS year_created
-- FROM sites
-- JOIN clients on sites.client_id = clients.client_id
-- WHERE clients.client_id = 20
-- GROUP BY sites.domain_name

-- 5. What query would you run to get the total # of leads generated for each of the sites between January 1, 2011 to February 15, 2011?

-- SELECT sites.domain_name AS website, COUNT(leads.leads_id) AS number_of_leads, DATE_FORMAT(leads.registered_datetime, "%M %d, %Y")
-- FROM leads
-- JOIN sites ON leads.site_id = sites.site_id
-- WHERE leads.registered_datetime >= "2011-01-01 00:00:00" AND leads.registered_datetime <= "2011-02-14 23:59:59"
-- GROUP BY sites.domain_name

-- 6. What query would you run to get a list of client names and the total # of leads we've generated for each of our clients between January 1, 2011 to December 31, 2011?

-- SELECT CONCAT_WS(" ", clients.first_name, clients.last_name), COUNT(leads.leads_id) AS number_of_leads, DATE_FORMAT(leads.registered_datetime, "%M %d, %Y") AS date_registered
-- FROM clients
-- JOIN sites ON clients.client_id = sites.client_id
-- JOIN leads ON sites.site_id = leads.site_id
-- WHERE leads.registered_datetime >= "2011-01-01 00:00:00" AND leads.registered_datetime <= "2011-12-31 23:59:59"
-- GROUP BY clients.client_id

-- 7. What query would you run to get a list of client names and the total # of leads we've generated for each client each month between months 1 - 6 of Year 2011?

-- SELECT CONCAT_WS(" ", clients.first_name, clients.last_name) AS client_name, COUNT(leads.leads_id) AS number_of_leads, DATE_FORMAT(leads.registered_datetime, "%M") AS month_registered
-- FROM clients
-- JOIN sites ON clients.client_id = sites.client_id
-- JOIN leads ON sites.site_id = leads.site_id
-- WHERE leads.registered_datetime >= "2011-01-01 00:00:00" AND leads.registered_datetime <= "2011-06-30 23:59:59"
-- GROUP BY sites.site_id
 
-- 8. What query would you run to get a list of client names and the total # of leads we've generated for each of our clients' sites between January 1, 2011 to December 31, 2011? Order this query by client id.  Come up with a second query that shows all the clients, the site name(s), and the total number of leads generated from each site for all time.

-- SELECT CONCAT_WS(" ", clients.first_name, clients.last_name) AS client_name, sites.domain_name, COUNT(leads.leads_id) AS number_of_leads, DATE_FORMAT(leads.registered_datetime, "%M %d, %Y") AS date_registered
-- FROM clients
-- JOIN sites ON clients.client_id = sites.client_id
-- JOIN leads ON sites.site_id = leads.site_id
-- WHERE leads.registered_datetime >= "2011-01-01 00:00:00" AND leads.registered_datetime <= "2011-12-31 23:59:59"
-- GROUP BY sites.domain_name
-- ORDER BY clients.client_id

-- SELECT CONCAT_WS(" ", clients.first_name, clients.last_name) AS client_name, sites.domain_name, COUNT(leads.leads_id) AS number_of_leads, DATE_FORMAT(leads.registered_datetime, "%M %d, %Y") AS date_registered
-- FROM clients
-- JOIN sites ON clients.client_id = sites.client_id
-- JOIN leads ON sites.site_id = leads.site_id
-- GROUP BY sites.domain_name
-- ORDER BY clients.client_id

-- 9. Write a single query that retrieves total revenue collected from each client for each month of the year. Order it by client id.

-- SELECT CONCAT_WS(" ", clients.first_name, clients.last_name) AS client_name, SUM(billing.amount) AS total_revenue, 
-- DATE_FORMAT(billing.charged_datetime, "%M") AS month_charged, DATE_FORMAT(billing.charged_datetime, "%Y") AS year_charged
-- FROM clients
-- JOIN billing ON clients.client_id = billing.client_id
-- GROUP BY month_charged, client_name
-- ORDER BY clients.client_id, billing.charged_datetime
-- 
-- 10. Write a single query that retrieves all the sites that each client owns. Group the results so that each row shows a new client. It will become clearer when you add a new field called 'sites' that has all the sites that the client owns. (HINT: use GROUP_CONCAT)

-- SELECT CONCAT_WS(" ", clients.first_name, clients.last_name) AS client_name, GROUP_CONCAT("  ", sites.domain_name) AS sites
-- FROM clients
-- LEFT JOIN sites on clients.client_id = sites.client_id
-- GROUP BY clients.client_id