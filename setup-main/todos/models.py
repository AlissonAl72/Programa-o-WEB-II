from datetime import date
from django.db import models


class Todo(models.Model):
    title = models.CharField(verbose_name="Titulo",max_length=100, null=False, blank=False)
    created_at = models.DateTimeField(verbose_name="data de entrega",auto_now_add=True, null=False, blank=False)
    deadline = models.DateField(null=False, blank=False)
    finished_at = models.DateField(null=True,)

    class Meta:
        ordering = ["deadline"]

    def mark_has_completed(self):
        if not self.finished_at:
            self.finished_at = date.today()
            self.save()
