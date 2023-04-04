


create procedure p1
@par1	int,
@par2	varchar(10) out
as
begin
	set @par2=concat('X', @par1);
	return; 
end;



declare	@var1	int=99,
		@var2	varchar(10);
				


execute p1 @var1, @var2 out ;	


select @var1, @var2;

print concat(@var1,', ', @var2);


--declare @x int;

--set @x=execute proc1;