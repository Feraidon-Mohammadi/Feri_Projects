update irgendeinetabelle
set irgendeinespalte=dbo.irgendeinefunktion()
where...




create function irgendeinefunktion(...)
returns		<datentyp>
as
begin
	...
	set @irgendeinevariable=(	select irgendwas
								from irgendeinetabelle
								where irgendwie)
	...
	return @irgendeinevariable;
end;



/*-----------------m�gliche L�sung

declare @var <datentyp>

set @var=(	select irgendwas
			from irgendeinetabelle
			where irgendwie)

update irgendeinetabelle
set irgendeinespalte=@var
where...

-------------------------------------*/