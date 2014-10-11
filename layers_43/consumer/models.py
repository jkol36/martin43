from django.db import models

from django.contrib.auth.models import User


class Project(models.Model):
    user = models.ForeignKey(User, related_name='projects', null=True)
    title = models.CharField(max_length=255, null=True)
    description = models.CharField(max_length=255, null=True)
    budget = models.DecimalField(max_digits=10, decimal_places=2)


class ProjectUpdate(models.Model):
    """
    Conversation around an object
    """
    UPDATE_TYPES = (
        ('searching', 'Finding a designer'),
        ('designer_found', 'Proposed designer'),
        ('message_from', 'Message From'),
        ('message_to', 'Message To'),
        ('designer_accepted', 'Designer selected'),
        ('deposit', 'Awaiting Deposit'),
        ('inspiration_board', 'Inspiration Board'),
        ('proposal', 'Proposal from designer'),
        ('change_request', 'Change request'),
        ('picture', 'Picture'),
        ('final_payment', 'Final Payment'),
        ('receipt', 'Order receipt'),
        ('status', 'Order status'),
    )

    project = models.ForeignKey(Project, related_name='updates', null=True)
    user = models.ForeignKey(User, related_name='updates', null=True)
    update_type = models.CharField(max_length=6, choices=UPDATE_TYPES)
    message = models.CharField(max_length=255, null=True)
    amount_required = models.DecimalField(max_digits=10, decimal_places=2)
    current_status = models.CharField(max_length=255, null=True)


class ProjectUpdateItem(models.Model):
    """
    stores pictures and captions for inspiration boards,
    uploads for pictures,
    line items for receipts,
    info for proposals, etc
    etc
    """
    key = models.CharField(max_length=255, null=True)
    value = models.CharField(max_length=255, null=True)
    upload = models.FileField(upload_to="project_images")
    update = models.ForeignKey(ProjectUpdate, related_name='items', null=True)


class Payment(models.Model):
    project = models.ForeignKey(Project, related_name='updates', null=True)
    success = models.BooleanField(default=False)
    external_id = models.CharField(max_length=255, null=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
