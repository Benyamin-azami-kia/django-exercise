from django.db import models
from django.core.validators import MinLengthValidator




class Tag(models.Model):
	caption=models.CharField(max_length=10)

	def __str__(self):
		return f"{self.caption}"

	class Meta:
		verbose_name="Tag"



class Author(models.Model):
	first_name=models.CharField(max_length=100)
	last_name=models.CharField(max_length=100)
	email=models.EmailField()

	def __str__(self):
		return f"{self.first_name} {self.last_name}"

	class Meta:
		verbose_name="Author"



class Post(models.Model):
	title=models.CharField(max_length=100)
	excert=models.CharField(max_length=200)
	image_name=models.ImageField(upload_to='image', null=True)
	author=models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name='posts')
	slug=models.SlugField(db_index=True, unique=True)
	date=models.DateField(auto_now=True)
	tag=models.ManyToManyField(Tag)
	content=models.TextField(validators=[MinLengthValidator(20)])


	class Meta:
		verbose_name="Post"


	def __str__(self):
		return f"{self.title}"


class Comment(models.Model):
	name=models.CharField(max_length=120)
	email=models.EmailField()
	text=models.TextField(max_length=300)
	post=models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')


	def __str__(self):
		return self.name+' '+self.post.title