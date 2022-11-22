from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class CoinBoard(models.Model):
    write_time = models.DateTimeField(auto_now_add=True)
    board_title = models.CharField(max_length=100)
    write_user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return f"게시글 제목은 {self.board_title}이고, 내용은 {self.content}"
