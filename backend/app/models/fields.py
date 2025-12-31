from peewee import (
    CharField as PCharField,
    IntegerField as PIntegerField,
    FloatField as PFloatField,
    BooleanField as PBooleanField,
    DateField as PDateField,
    TimestampField as PTimestampField,
    TextField as PTextField,
    SQL
)

class CommentMixin:
    def __init__(self, *args, **kwargs):
        comment = kwargs.pop('comment', None)
        if comment:
            constraints = kwargs.get('constraints', [])
            if constraints is None:
                constraints = []
            # Ensure comment is escaped properly if needed, but simple string substitution is risky for SQL injection
            # However, these are developer-provided strings. We should ideally escape quotes.
            # A simple replace "'" with "''" might suffice for SQL strings.
            safe_comment = comment.replace("'", "''")
            constraints.append(SQL(f"COMMENT '{safe_comment}'"))
            kwargs['constraints'] = constraints
        super().__init__(*args, **kwargs)

class CharField(CommentMixin, PCharField):
    pass

class IntegerField(CommentMixin, PIntegerField):
    pass

class FloatField(CommentMixin, PFloatField):
    pass

class BooleanField(CommentMixin, PBooleanField):
    pass

class DateField(CommentMixin, PDateField):
    pass

class TimestampField(CommentMixin, PTimestampField):
    pass

class TextField(CommentMixin, PTextField):
    pass
