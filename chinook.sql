--1
SELECT Name
FROM Artist
WHERE ArtistId = 51;
--2
SELECT Title
FROM Album
ORDER BY Title
LIMIT 5 OFFSET 47;
--3
SELECT Title
FROM Album
WHERE Title LIKE '%Hit%';
--4
SELECT Name, Milliseconds
FROM Track
WHERE Milliseconds BETWEEN 350000 AND 360000;
--5
SELECT Name, Composer
FROM Track
WHERE Composer IS NULL
--6
SELECT Name
FROM Track
WHERE AlbumId = 108;
--7
SELECT
    SUM(Milliseconds) / 1000 AS TotalSeconds,
    (SUM(Milliseconds) / 1000) / 60 AS Minutes,
    (SUM(Milliseconds) / 1000) % 60 AS Seconds
FROM Track
WHERE AlbumId = 77;
--8
SELECT MAX(Total)
FROM Invoice;
--9
SELECT SUM(Total)
FROM Invoice;