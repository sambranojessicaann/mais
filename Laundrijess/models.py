from django.db import models





APPLIANCES_CHOICES=(('Washing Machine', 'washing machine'), 
	('Dryer', 'dryer'), 
	('Washing Machine With Dryer', 'washing machine with dryer'),
	('Extension', 'extension'),
	('Automatic Washing Machine', 'automatic washing machine'))

class SignUp(models.Model):
	pass

class S1(models.Model):
	kamote = models.ForeignKey(SignUp, default=None, on_delete=models.CASCADE)
	text = models.TextField(default="")

	Name = models.TextField(max_length=800, null=True)
	Address = models.TextField(max_length=800, null=True)
	Contact_Number = models.CharField(default="", max_length=12)
	Email = models.TextField(max_length=800, null=True)
	Contact_Person = models.TextField(max_length=800, null=True)
#DATE
	Date = models.DateTimeField(auto_now_add=True, null=True)

class Client(models.Model):
	Carrot = models.ForeignKey(S1, default=None, on_delete=models.CASCADE)
	Char = models.CharField(max_length=800)

class Transaction(models.Model):
    Referrence_Number = models.Charfield(
            max_length = 10,
            blank=True,
            editable=False,
            unique=True,
            default=create_new_ref_number
        )

class Item(models.Model):
	title = models.CharField(max_length=800)
	price = models.FloatField()
	Patatas = models.ManyToManyField(S1, null=True)
	Char = models.CharField(max_length=100, choices=APPLIANCES_CHOICES)
	description = models.TextField()


class Delivery(models.Model):
	Carrot = models.ForeignKey(S1, default=None, null=True, on_delete=models.CASCADE)
	Char = models.CharField(max_length=800, null=True)
	For_Deliver = models.CharField(max_length=800, null=True)
	For_Pickup = models.CharField(max_length=800, null=True)

class Bayad(models.Model):
	Banana = models.ForeignKey(Delivery, default=None, on_delete=models.CASCADE)
	Char = models.CharField(max_length=800, null=True)
	Payment = models.TextField(max_length=800, null=True)
	

class Payment(models.Model):
	stripe_charge_id = models.CharField(max_length=50)
	user = models.ForeignKey(SignUp, default=None, on_delete=models.CASCADE)
	amount = models.FloatField()
	timestamp = models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return self.user.username