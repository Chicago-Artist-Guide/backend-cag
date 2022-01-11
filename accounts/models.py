from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.utils import timezone


class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

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

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='profile', blank=True, null=True)
    profile_pic = models.ImageField(upload_to="media/profile-images/", blank=True, null=True)
    what_you_like_doing = models.TextField(blank=True, null=True)
    perform = models.TextField()
    some_details_page = models.TextField()
    category = models.CharField(choices=CategoryChoices.choices, max_length=255)
    basics_18_plus = models.BooleanField(default=False)
    privacy_agreement = models.BooleanField(default=False)

    def __str__(self):
        return self.user.email
