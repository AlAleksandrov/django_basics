from django.core.exceptions import ValidationError


def validate_email_domain(value):
    allowed_domains = ['university.com', 'university.org']
    domain = value.split('@')[-1]
    if domain not in allowed_domains:
        raise ValidationError(f"Domain '{domain}' is not allowed. Please use one of the following: {', '.join(allowed_domains)}")