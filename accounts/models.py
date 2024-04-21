from django.db import models

# Create your models here.


#anthony
class AnthonyStudent(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    guardian = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

#charles
class CharlesStudent(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    guardian = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

#berchman
class BerchmanStudent(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    guardian = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name
    
#bosco
class BoscoStudent(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    guardian = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name
    
#joseph
class JosephStudent(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    guardian = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

#martin
class MartinStudent(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    guardian = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name
    
#paul
class PaulStudent(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    guardian = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

#anne
class AnneStudent(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    guardian = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

#faustina
class FaustinaStudent(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    guardian = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name
    
#mary
class MaryStudent(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    guardian = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

#rita
class RitaStudent(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    guardian = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

#rose
class RoseStudent(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    guardian = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

#teresa
class TeresaStudent(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    guardian = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name
    
#class Customer(models.Model):
    #name = models.CharField(max_length=200, null=True)
    #phone = models.CharField(max_length=200, null=True)
    #email = models.CharField(max_length=200, null=True)
    #date_created = models.DateTimeField(auto_now_add=True, null=True)

    #def __str__(self):
        #return self.name
    
#PRODUCTS/TYPES OF OFFENSES
    
class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    CATEGORY = (
        ('Minor', 'Minor'),
        ('Major', 'Major'),
    )
    name = models.CharField(max_length=200, null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

#ORDERS/RECORD OF OFFENSES---------------------------------------------

#ANTHONY GOES HERE ----------------------------------------------------
class AnthonyOffense(models.Model):
    CATEGORY = (
        ('Minor', 'Minor'),
        ('Major', 'Major'),
    )

    name = models.ForeignKey(AnthonyStudent, null=True, on_delete=models.SET_NULL)
    offense =  models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    note = models.CharField(max_length=1000, null=True)
    action_given = models.CharField(max_length=1000, null=True)

    def __str__(self):
        return self.offense.name

#CHARLES GOES HERE ----------------------------------------------------
class CharlesOffense(models.Model):
    CATEGORY = (
        ('Minor', 'Minor'),
        ('Major', 'Major'),
    )

    name = models.ForeignKey(CharlesStudent, null=True, on_delete=models.SET_NULL)
    offense =  models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    note = models.CharField(max_length=1000, null=True)
    action_given = models.CharField(max_length=1000, null=True)

    def __str__(self):
        return self.offense.name
    
#BERCHMAN GOES HERE ----------------------------------------------------
class BerchmanOffense(models.Model):
    CATEGORY = (
        ('Minor', 'Minor'),
        ('Major', 'Major'),
    )

    name = models.ForeignKey(BerchmanStudent, null=True, on_delete=models.SET_NULL)
    offense =  models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    note = models.CharField(max_length=1000, null=True)
    action_given = models.CharField(max_length=1000, null=True)

    def __str__(self):
        return self.offense.name

#BOSCO GOES HERE ----------------------------------------------------
class BoscoOffense(models.Model):
    CATEGORY = (
        ('Minor', 'Minor'),
        ('Major', 'Major'),
    )

    name = models.ForeignKey(BoscoStudent, null=True, on_delete=models.SET_NULL)
    offense =  models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    note = models.CharField(max_length=1000, null=True)
    action_given = models.CharField(max_length=1000, null=True)

    def __str__(self):
        return self.offense.name

#JOSEPH GOES HERE ----------------------------------------------------
class JosephOffense(models.Model):
    CATEGORY = (
        ('Minor', 'Minor'),
        ('Major', 'Major'),
    )

    name = models.ForeignKey(JosephStudent, null=True, on_delete=models.SET_NULL)
    offense =  models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    note = models.CharField(max_length=1000, null=True)
    action_given = models.CharField(max_length=1000, null=True)

    def __str__(self):
        return self.offense.name

#MARTIN GOES HERE ----------------------------------------------------
class MartinOffense(models.Model):
    CATEGORY = (
        ('Minor', 'Minor'),
        ('Major', 'Major'),
    )

    name = models.ForeignKey(MartinStudent, null=True, on_delete=models.SET_NULL)
    offense =  models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    note = models.CharField(max_length=1000, null=True)
    action_given = models.CharField(max_length=1000, null=True)

    def __str__(self):
        return self.offense.name

#PAUL GOES HERE ----------------------------------------------------
class PaulOffense(models.Model):
    CATEGORY = (
        ('Minor', 'Minor'),
        ('Major', 'Major'),
    )

    name = models.ForeignKey(PaulStudent, null=True, on_delete=models.SET_NULL)
    offense =  models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    note = models.CharField(max_length=1000, null=True)
    action_given = models.CharField(max_length=1000, null=True)

    def __str__(self):
        return self.offense.name

#ANNE GOES HERE ----------------------------------------------------
class AnneOffense(models.Model):
    CATEGORY = (
        ('Minor', 'Minor'),
        ('Major', 'Major'),
    )

    name = models.ForeignKey(AnneStudent, null=True, on_delete=models.SET_NULL)
    offense =  models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    note = models.CharField(max_length=1000, null=True)
    action_given = models.CharField(max_length=1000, null=True)

    def __str__(self):
        return self.offense.name

#FAUSTINA GOES HERE ----------------------------------------------------
class FaustinaOffense(models.Model):
    CATEGORY = (
        ('Minor', 'Minor'),
        ('Major', 'Major'),
    )

    name = models.ForeignKey(FaustinaStudent, null=True, on_delete=models.SET_NULL)
    offense =  models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    note = models.CharField(max_length=1000, null=True)
    action_given = models.CharField(max_length=1000, null=True)

    def __str__(self):
        return self.offense.name

#MARY GOES HERE ----------------------------------------------------
class MaryOffense(models.Model):
    CATEGORY = (
        ('Minor', 'Minor'),
        ('Major', 'Major'),
    )

    name = models.ForeignKey(MaryStudent, null=True, on_delete=models.SET_NULL)
    offense =  models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    note = models.CharField(max_length=1000, null=True)
    action_given = models.CharField(max_length=1000, null=True)

    def __str__(self):
        return self.offense.name

#RITA GOES HERE ----------------------------------------------------
class RitaOffense(models.Model):
    CATEGORY = (
        ('Minor', 'Minor'),
        ('Major', 'Major'),
    )

    name = models.ForeignKey(RitaStudent, null=True, on_delete=models.SET_NULL)
    offense =  models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    note = models.CharField(max_length=1000, null=True)
    action_given = models.CharField(max_length=1000, null=True)

    def __str__(self):
        return self.offense.name

#ROSE GOES HERE ----------------------------------------------------
class RoseOffense(models.Model):
    CATEGORY = (
        ('Minor', 'Minor'),
        ('Major', 'Major'),
    )

    name = models.ForeignKey(RoseStudent, null=True, on_delete=models.SET_NULL)
    offense =  models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    note = models.CharField(max_length=1000, null=True)
    action_given = models.CharField(max_length=1000, null=True)

    def __str__(self):
        return self.offense.name

#TERESA GOES HERE ----------------------------------------------------
class TeresaOffense(models.Model):
    CATEGORY = (
        ('Minor', 'Minor'),
        ('Major', 'Major'),
    )

    name = models.ForeignKey(TeresaStudent, null=True, on_delete=models.SET_NULL)
    offense =  models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    note = models.CharField(max_length=1000, null=True)
    action_given = models.CharField(max_length=1000, null=True)

    def __str__(self):
        return self.offense.name


#TERESA GOES HERE------------------------------------------------------

#class Order(models.Model):
    #STATUS = (
        ('Pending', 'Pending'),
        ('Out for Delivery', 'Out for Delivery'),
        ('Delivered', 'Delivered'),
    #)

    #customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    #------------------------------------------------------------------
    #product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    #date_created = models.DateTimeField(auto_now_add=True, null=True)
    #status = models.CharField(max_length=200, null=True, choices=STATUS)
    #note = models.CharField(max_length=1000, null=True)

    #def __str__(self):
        #return self.product.name

    
