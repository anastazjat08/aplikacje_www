from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.


from django.contrib.auth.models import User


class Species(models.Model):
	name = models.CharField(max_length=200, unique=True)
	image = models.ImageField(upload_to = "animals") #folder na images

	def __str__(self):
		return f"{self.name}"

class Chromosome(models.Model):
	species = models.ForeignKey(Species, on_delete=models.CASCADE) 
	number = models.IntegerField()
	start_position = models.IntegerField()
	end_position = models.IntegerField()

	def __str__(self):
		return f"Chromosome {self.number} for {self.species}"


class Snp(models.Model):
	chromosome = models.ForeignKey(Chromosome, on_delete=models.CASCADE)
	position = models.IntegerField()
	REF_allele = models.CharField(max_length=1, choices=[("A","A"), ("C", "C"), ("T", "T"), ("G", "G") ])
	ALT_allele = models.CharField(max_length=1, choices=[("A","A"), ("C", "C"), ("T", "T"), ("G", "G") ])
	MAF = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(1.0)])

	def __str__(self):
		return f"SNP at position {self.position} on chromosome {self.chromosome.number}"
	



class Annotation(models.Model):
	snp = models.ForeignKey(Snp, on_delete=models.CASCADE)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	text = models.TextField()

	def __str__(self):
		return f"Annotation for {self.snp.position} on chromosome {self.snp.chromosome.number} by {self.author}"

