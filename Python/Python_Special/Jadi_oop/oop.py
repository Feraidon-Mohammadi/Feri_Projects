

class Person:
	count = 0
	def __init__(self, name , age):
		self.name = name
		self.age = age
		Person.count = Person.count + 1
	def get_name(self):
		print('name is: %a' %self.name)
	def get_age(self):
		print('age is: %s' %self.age)
	def get_info(self):
		print("name is: %s and age is: %i" %(self.name, self.age))
	def birthdy(self):
		self.age = self.age + 1
		print("happy birthday %s" %(self.name))
	def return_count(self):
		return (Person.count)
	
		
		
jadi = Person('jadi', 40)
jadi.get_name()
jadi.get_age()
jadi.get_info()
jadi.birthdy()
jadi.get_age()

manooch = Person("manoocher", 12)
manooch.get_info()
print("at the moment I have %i persons" %jadi.return_count())



"""
در این بخش به جزئیات بیشتری از شی گرایی در پایتون پیشرفته می‌پردازیم.

در پایتون برای ایجاد یک کلاس از عبارت class استفاده می‌شود.
به عنوان مثال قصد داریم کلاسی به نام person ایجاد کنیم.
در مبحث شی گرایی می‌ توانیم از دو نوع متغیر استفاده کنیم.
نوع اول متغیر کلاس یا class variable ها هستند که برای تمامی اشیا ساخته شده از یک کلاس ثابت اند.
نوع دوم متغیرهای مربوط به اشیا هستند یا object variableها هستند که مربوط به خود objectها هستند.
در ابتدای یک کلاس پس از معرفی متغیرها اولین تابع، سازنده کلاس یا constructor کلاس هست که به صورت متد (____init)  تعریف می‌شود.
این متد هنگام ساخت شی از کلاس به صورت اتوماتیک اجرا می‌شود.
برای ساخت object از یک کلاس، از واژه new استفاده می‌شود.
هنگام استفاده از کلمه new تابع سازنده کلاس اجرا شده و دستورات داخل سازنده اجرا می‌شود.

کلیدواژه مهم دیگری در بحث شی گرایی ر پایتون پیشرفته، عبارت self هست که معادل عبارت this در سایر زبان‌های برنامه نویسی است .

این عبارت در برنامه نویسی اشاره به همین شی دارد.
مثلا self.name به متغیر name شی ایجاد شده اشاره دارد.
معمولا در کلاس‌های برای مقدار دهی و گرفتن مقدار متغیرها توابع setter وgetter تعریف می‌شود
که تابع setter برای مقدار دهی متغیرها استفاده می‌شود و
به عنوان ورودی مقادیری را که قصد داریم در متغیرهای کلاس قرار دهیم دریافت می‌کند.
تابع getter برای گرفتن مقادیر متغیرهای کلاس در زمان مورد نیاز استفاده می‌شود.


"""
















