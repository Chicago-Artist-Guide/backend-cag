from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.contrib.postgres.fields import ArrayField
from django.db.models import JSONField



class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class UserManager(BaseUserManager):
    """
    Creating a manager for custom user model.
    """

    def _create_user(self, email: str, password: str = None, **kwargs):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            **kwargs
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email: str = None, password=None, **kwargs):
        kwargs.setdefault('is_superuser', False)
        return self._create_user(email=email, password=password, **kwargs)

    def create_superuser(self, email, password, **kwargs):
        """
        Create and return a `User` with superuser permissions.
        """
        kwargs.setdefault('is_superuser', True)
        if kwargs.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self._create_user(email=email, password=password, **kwargs)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin, BaseModel):
    class UserStatus(models.TextChoices):
        Active = 'active', 'Active',
        In_Active = 'inactive', 'In Active'

    email = models.EmailField(
        'email address',
        max_length=255,
        unique=True,
        error_messages={'unique': "A user with that email already exists.", }
    )

    username = models.CharField(max_length=100, blank=True, unique=True, null=True)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    is_active = models.BooleanField(('active'),
                                    default=True,
                                    help_text=('Designates whether this user should be treated as active. '
                                               'Unselect this instead of deleting accounts.'
                                               ),
                                    )
    is_staff = models.BooleanField(('staff status'),
                                   default=False,
                                   help_text=('Designates whether the user can log into this admin site.'),
                                   )
    status = models.CharField(choices=UserStatus.choices, max_length=255, default=UserStatus.Active)
    date_joined = models.DateTimeField(('date joined'), default=timezone.now)
    USERNAME_FIELD = 'email'

    # Tells Django that the UserManager class defined above should manage
    # objects of this type.
    objects = UserManager()

    def __str__(self):
        return self.email

    class Meta:
        """
        to set table name in database
        """
        db_table = "custom_user"
        verbose_name = 'user'
        verbose_name_plural = 'users'


class Profile(BaseModel):
    class CategoryChoices(models.TextChoices):
        Individual_Artist = 'individual_artist', 'Individual Artist',
        Theatre_Group = 'theatre_group', 'Theatre Group'

    class Perform(models.TextChoices):
        On_Stage = 'on_stage', 'On Stage',
        Off_Stage = 'off_stage', 'Off Stage'
        Both = 'both', 'Both'

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='profile', blank=True, null=True)
    profile_pic = models.ImageField(upload_to="media/profile-images/", blank=True, null=True)
    category = models.CharField(choices=CategoryChoices.choices, max_length=255, default=CategoryChoices.Individual_Artist)
    perform = models.CharField(choices=Perform.choices, max_length=255, default=Perform.On_Stage)
    basics_18_plus = models.BooleanField(default=False)
    privacy_agreement = models.BooleanField(default=False)

    def __str__(self):
        return self.user.email


class BasicProfile(BaseModel):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    pronouns = models.CharField(max_length=255)
    lgbtqia = models.CharField(max_length=255)
    ethnicities = ArrayField(models.CharField(max_length=200))
    height_feet = models.IntegerField(blank=True, null=True)
    height_inches = models.IntegerField(blank=True, null=True)
    height_no_answer = models.BooleanField(default=False)
    age_range = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    gender_roles = ArrayField(models.CharField(max_length=200))
    gender_transition = ArrayField(models.CharField(max_length=200))
    offstage_general = ArrayField(models.CharField(max_length=200))
    offstage_production = ArrayField(models.CharField(max_length=200))
    offstage_scenic_and_properties = ArrayField(models.CharField(max_length=200))
    offstage_lighting = ArrayField(models.CharField(max_length=200))
    offstage_sound = ArrayField(models.CharField(max_length=200))
    offstage_hair_makeup_costumes = ArrayField(models.CharField(max_length=200))
    profile_image_url = models.TextField(null=True, blank=True)
    union_status = models.CharField(max_length=255)
    agency = models.CharField(max_length=255)
    websites = JSONField()
    bio = models.TextField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.user.email