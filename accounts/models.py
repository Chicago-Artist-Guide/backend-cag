from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.utils import timezone


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


class GetSomeDetails(BaseModel):
    class PronounsChoices(models.TextChoices):
        x1 = 'x1', 'X1',
        x2 = 'x2', 'X2'

    class LGBTQIACommunityIdentificationChoices(models.TextChoices):
        Yes = 'yes', 'Yes',
        No = 'no', 'No'
        Do_Not_Wish = 'do_not_wish', 'Do_Not_Wish'

    class GenderIdentity(models.TextChoices):
        Male = 'male', 'Male',
        Female = 'female', 'Female'

    class AgeRange(models.TextChoices):
        eighteen_to_twenty_two = '18-22', 'Eighteen to Twenty Two',
        twenty_three_to_twenty_seven = '23-27', 'Twenty Three to Twenty Seven'
        twenty_eight_to_thirty_two = '28-32', 'Twenty Eight to Thirty Two'
        thirty_three_to_thirty_seven = '33-37', 'Thirty Three to Thirty Seven'
        thirty_eight_to_fourty_two = '38-42', 'Thirty Eight to Fourty Two'
        fourty_three_to_fourty_seven = '43-47', 'Fourty Three to Fourty Seven'
        fourty_eight_to_fifty_two = '48-52', 'Fourty Eight to Fifty Two'
        fifty_three_to_fifty_seven = '53-57', 'Fifty Three to Fifty Seven'
        fifty_eight_to_sixty_two = '58-62', 'Fifty Eight to Sixty Two'
        sixty_two_plus = '62+', 'Sixty Two Plus'

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='user_get_some_details', blank=True, null=True)
    pronouns = models.CharField(choices=PronounsChoices.choices, max_length=255, default=PronounsChoices.x1)
    other = models.CharField(max_length=255, null=True, blank=True)
    lgbtqia_community_identification = models.CharField(choices=LGBTQIACommunityIdentificationChoices.choices, max_length=255, default=LGBTQIACommunityIdentificationChoices.Yes)
    
    # Your identity fields
    # asian = models.ForeignKey(AsianIdentity, on_delete=models.CASCADE, blank=True, null=True)
    black_or_african_american = models.BooleanField(default=False)
    indigenous = models.BooleanField(default=False)
    latinx = models.BooleanField(default=False)
    mena = models.BooleanField(default=False)
    native_hawailan_or_other_pacific_islander = models.BooleanField(default=False)
    white = models.BooleanField(default=False)

    # height
    feet = models.IntegerField(default=0)
    inches = models.FloatField(default=0.0)
    i_do_not_wish_to_answer = models.BooleanField(default=False)

    # Age RAnge
    age_range = models.CharField(choices=AgeRange.choices, max_length=255, default=AgeRange.eighteen_to_twenty_two)

    # Gender Identity
    gender_identity = models.CharField(choices=GenderIdentity.choices, max_length=255, default=GenderIdentity.Male)

    # Comfortable Playing Roles
    women = models.BooleanField(default=False)
    men = models.BooleanField(default=False)
    neither = models.BooleanField(default=False)

    # Playing Character through transition
    playing_character_throgh_transition = models.BooleanField(default=False)

    def __str__(self):
        return self.user.email


class AsianIdentity(models.Model):
    get_some_details = models.ForeignKey(GetSomeDetails, on_delete=models.CASCADE, blank=True, null=True)
    east_asian = models.BooleanField(default=False)
    south_east_asian = models.BooleanField(default=False)
    south_asian = models.BooleanField(default=False)
    central_west_asian = models.BooleanField(default=False)


class WhatDoYouLikeDoing(BaseModel):

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='user_what_you_like_doing', blank=True, null=True)
    
    # General
    directing = models.BooleanField(default=False)
    violence_fight_design = models.BooleanField(default=False)
    intimacy_design = models.BooleanField(default=False)
    choreography = models.BooleanField(default=False)
    casting = models.BooleanField(default=False)
    dramaturgy = models.BooleanField(default=False)
    dialect_coaching = models.BooleanField(default=False)
    musical_directing = models.BooleanField(default=False)

    # Production
    stage_management = models.BooleanField(default=False)
    production_management = models.BooleanField(default=False)
    board_op = models.BooleanField(default=False)
    run_crew = models.BooleanField(default=False)

    # Scenic & Properties
    set_design = models.BooleanField(default=False)
    technical_direction = models.BooleanField(default=False)
    properties_designer = models.BooleanField(default=False)
    scenic_carpentery = models.BooleanField(default=False)
    charge_artist = models.BooleanField(default=False)

    # Lighting
    light_design = models.BooleanField(default=False)
    projection_design = models.BooleanField(default=False)
    special_effect_design = models.BooleanField(default=False)
    master_electrician = models.BooleanField(default=False)

    # Sound
    sound_design = models.BooleanField(default=False)
    sound_mixer_engineer = models.BooleanField(default=False)

    # Hair, makeup, costumes
    costume_design = models.BooleanField(default=False)
    hair_and_wig_design = models.BooleanField(default=False)
    makeup_design = models.BooleanField(default=False)


    def __str__(self):
        return self.user.email


class AlmostDone(BaseModel):
    class UnionChoices(models.TextChoices):
        Agency = 'agency', 'Agency'

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='user_almost_done', blank=True, null=True)
    union = models.CharField(choices=UnionChoices.choices, max_length=255, default=UnionChoices.Agency)
    other = models.CharField(max_length=255, null=True, blank=True)
    url = models.URLField(max_length=255, null=True, blank=True)
    type = models.CharField(max_length=255, null=True, blank=True)
