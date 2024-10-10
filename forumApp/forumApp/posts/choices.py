from django.db import models


class LanguageChoices(models.TextChoices):

    PYTHON = "py", "Python"
    JAVA = "java", "Java"
    JAVASCRIPT = "js", "JavaScript"
    C_PLUS_PLUS = "c++", "C++"
    C = "c", "C"
    OTHER = "other", "Other"