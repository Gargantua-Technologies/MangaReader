from django.db import models


# NOTE source not many to many?
class Manga(models.Model):
    name = models.CharField(max_length=128)
    volume_cnt = models.IntegerField()
    chapters_cnt = models.IntegerField()
    source_name = models.ManyToManyField(to='MangaSource')  # FIXME source
    url = models.CharField(max_length=1024)

    def __str__(self):  # [ ] delete
        return self.name


class Frame(models.Model):
    chapter = models.ForeignKey(to='Chapter', on_delete=models.CASCADE)
    serial = models.IntegerField()
    external_url = models.CharField(max_length=1024)  # [ ] Delete
    internal_url = models.CharField(max_length=1024)
    img = models.BinaryField()


class Chapter(models.Model):
    source_name = models.ForeignKey(
        to='MangaSource', on_delete=models.CASCADE)  # FIXME source
    manga_id = models.ForeignKey(to='Manga', on_delete=models.CASCADE)
    volume_id = models.ForeignKey(to='Volume', on_delete=models.CASCADE)
    serial = models.IntegerField()
    frames_cnt = models.IntegerField()


class MangaSource(models.Model):
    name = models.CharField(max_length=128)
    url = models.CharField(max_length=1024)

    def __str__(self) -> str:  # [ ] delete
        return self.name


class Volume(models.Model):
    manga_id = models.ForeignKey(
        to='Manga', on_delete=models.CASCADE)  # FIXME manga
    serial = models.IntegerField()
    chapter_start_serial = models.IntegerField()
    chapter_end_serial = models.IntegerField()
