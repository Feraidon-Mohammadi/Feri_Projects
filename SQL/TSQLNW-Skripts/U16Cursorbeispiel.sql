create schema funct_zugriff;


							--CursorDeklaration
declare c_fn_name cursor for	select name 
								from sys.objects 
								where type='fn' or type='if';

							--einfache Variablendeklaration
declare @fn_name	varchar(50),
		@stmt		nvarchar(200);

							--Öffnen des Cursors
							--(Ausführen des Select)
open c_fn_name;

							--Zeiger bewegen in der Treffermenge
fetch next from c_fn_name into @fn_name;

while @@fetch_status=0
begin
	set @fn_name='dbo.'+ @fn_name;
							
	set @stmt='alter schema funct_zugriff transfer '+@fn_name;
							
	exec sp_executesql @stmt; 

	fetch next from c_fn_name into @fn_name

end
																	--Schließen des Cursors
close c_fn_name
																	--Speicherbereich freigeben
deallocate c_fn_name

