from django.contrib.auth.models import AbstractUser
from django.db import models

from apps.accounts.managers import UserManager


class User(AbstractUser):
    """
    Custom user model for the Enterprise AI Support Engineering Platform.

    This user model is designed for:
    - multi-tenant SaaS access
    - support engineers
    - platform administrators
    - human approval workflows
    - AI governance controls
    """

    username = None

    email = models.EmailField(
        unique=True,
        db_index=True,
        help_text="Primary login identifier for the user.",
    )

    first_name = models.CharField(
        max_length=150,
        blank=True,
    )

    last_name = models.CharField(
        max_length=150,
        blank=True,
    )

    job_title = models.CharField(
        max_length=255,
        blank=True,
        help_text="User job title, such as Support Engineer or Platform Admin.",
    )

    department = models.CharField(
        max_length=255,
        blank=True,
        help_text="Department the user belongs to.",
    )

    is_support_engineer = models.BooleanField(
        default=False,
        help_text="Allows the user to work support tickets.",
    )

    is_security_reviewer = models.BooleanField(
        default=False,
        help_text="Allows the user to review security-sensitive escalations.",
    )

    is_platform_admin = models.BooleanField(
        default=False,
        help_text="Allows the user to manage platform-level configuration.",
    )

    can_approve_ai_responses = models.BooleanField(
        default=False,
        help_text="Allows the user to approve AI-generated customer responses.",
    )

    can_approve_code_fixes = models.BooleanField(
        default=False,
        help_text="Allows the user to approve AI-generated code changes.",
    )

    can_override_policies = models.BooleanField(
        default=False,
        help_text="Allows the user to override governance policies.",
    )

    last_seen_at = models.DateTimeField(
        null=True,
        blank=True,
        help_text="Last time the user was active in the platform.",
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        ordering = ["email"]
        indexes = [
            models.Index(fields=["email"]),
            models.Index(fields=["is_platform_admin"]),
            models.Index(fields=["is_support_engineer"]),
        ]

    @property
    def full_name(self) -> str:
        """
        Return the user's full name if available.
        """

        name = f"{self.first_name} {self.last_name}".strip()

        if name:
            return name

        return self.email

    @property
    def is_ai_approval_user(self) -> bool:
        """
        Return True if the user can approve any AI-generated action.
        """

        return any(
            [
                self.can_approve_ai_responses,
                self.can_approve_code_fixes,
                self.can_override_policies,
            ]
        )

    def __str__(self) -> str:
        return self.email