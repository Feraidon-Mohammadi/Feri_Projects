DECLARE @sqlCommand varchar(1000); 
DECLARE @columnList varchar(75); 
DECLARE @city_var varchar(75);

SET @columnList = 'AddressID, AddressLine1, City'; 
SET @city_var = '''London'''; 
SET @sqlCommand = 'SELECT ' + @columnList + ' FROM Person.Address WHERE City = ' + @city_var;

EXEC (@sqlCommand); 






DECLARE @sqlCommand nvarchar(1000); 
DECLARE @columnList varchar(75);
DECLARE @city_var varchar(75);

SET @columnList = 'AddressID, AddressLine1, City'; 
SET @city_var = 'London'; 
SET @sqlCommand = 'SELECT ' + @columnList + ' FROM Person.Address WHERE City = @city_par'; 

EXECUTE sp_executesql @sqlCommand, N'@city_par nvarchar(75)', @city_par = @city_var ;

