from django.db import models

BUG_IMPORTANCE = (
    ('pending', 'Waiting for set'),
    ('low', 'Low'),
    ('minor', 'Minor'),
    ('major', 'Major'),
    ('critical', 'Critical'),
    ('blocker', 'Blocker')
)

BUG_STATUS = (
    ('in progress', 'Working on a problem'),
    ('not touched', 'Not reviewed'),
    ('resolved', 'Bug fixed')
)


class BugDescription(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    screen_shoot = models.ImageField(upload_to='uploads/% Y/% m/% d/', blank=True, null=True)
    importance_level = models.CharField(choices=BUG_IMPORTANCE, max_length=30, default='Not set...')


class SolvingStatus(models.Model):
    status = models.CharField(choices=BUG_STATUS, max_length=30, default='Pending...')
    bug = models.ForeignKey(BugDescription, on_delete=models.CASCADE)
