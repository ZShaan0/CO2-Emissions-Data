\c co2_emissions;

CREATE TABLE emissions (
    country VARCHAR,
    region VARCHAR,
    date_year INT,
    kilotons_of_co2 INT,
    tons_per_capita FLOAT,
    PRIMARY KEY (country, date_year)
);