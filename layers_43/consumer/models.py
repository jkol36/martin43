from django.db import models
from sorl.thumbnail import ImageField
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.ForeignKey(User)
    description = models.CharField(max_length=250, null=True, blank=True)
    photo = ImageField(upload_to='images/profile_pics', null=True, blank=True, default=None)
    has_profile_pic = models.BooleanField(default=False, blank=True)
    def __unicode__(self):
        return self.description
class Project(models.Model):
    user = models.ForeignKey(User, related_name='projects', null=True)
    title = models.CharField(max_length=255, null=True)
    zipcode = models.CharField(max_length=255, null=True)
    product_type = models.CharField(max_length=255, null=True)
    order_quantity = models.IntegerField(default=0)
    materials = models.CharField(max_length=255, null=True)
    deadline = models.DateField(null = True, blank=True)
    description = models.CharField(max_length=255, null=True)
    budget = models.DecimalField(max_digits=10, null=True, blank=True, decimal_places=2)
    is_submitted = models.BooleanField(default=False)
    shipping = models.BooleanField(blank=True, default=False)
    designer = models.ForeignKey(User, null=True, blank=True)
    def __unicode__(self):
        return self.title
    def get_budget(self):
        return self.budget

    def get_title(self):
        return __unicode__(self.title)

    def get_deadline(self):
        return self.deadline

    def get_submitted(self):
        return self.submitted

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
    name = models.CharField(max_length=255, blank=True)
    project = models.ForeignKey(Project, related_name='updates', null=True)
    user = models.ForeignKey(User, related_name='updates', null=True)
    update_type = models.CharField(max_length=6, choices=UPDATE_TYPES)
    message = models.CharField(max_length=255, null=True)
    amount_required = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    current_status = models.CharField(max_length=255, null=True)

    def __unicode__(self):
        return self.update_type


class ProjectUpdateItem(models.Model):
    """
    stores pictures and captions for inspiration boards,
    uploads for pictures,
    line items for receipts,
    info for proposals, etc
    etc
    """
    photo = ImageField(upload_to="images/project_pics", null = True, blank = True, default = False)
    update = models.ForeignKey(ProjectUpdate, related_name='items', null=True)


    def __unicode__(self):
        return self.update.name

class Payment(models.Model):
    project = models.ForeignKey(Project, related_name='payments', null=True)
    success = models.BooleanField(default=False)
    external_id = models.CharField(max_length=255, null=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    update = models.ForeignKey(ProjectUpdate, related_name='pmts', null=True)


# need to add a post save to send msg to pusher