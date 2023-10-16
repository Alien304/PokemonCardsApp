-- Active: 1697285249220@@127.0.0.1@5432@pokemoncards
CREATE TABLE Card (
    CardID INT PRIMARY KEY,
    CardName VARCHAR(255),
    PokemonName VARCHAR(255),
    ImageURL VARCHAR(255),
    owned BOOLEAN
);

CREATE TABLE Set (
    SetID INT PRIMARY KEY,
    SetName VARCHAR(255),
    TotalCards INT
);