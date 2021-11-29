import django_tables2 as tables
from .models import Staff


class StaffTable(tables.Table):
    activate = {
        'td': {'data-href': lambda record: record.activate_user}
    }
    editable = {
        'td': {'data-href': lambda record: record.get_absolute_url}
    }
    deletable = {
        'td': {'data-href': lambda record: record.delete_staff}
    }
    is_active = tables.Column(
        attrs=activate,
    )
    edit = tables.Column(
        attrs=editable, orderable=False,
        default='edit'
    )
    delete = tables.Column(
        attrs=deletable, orderable=False,
        default='delete'
    )

    class Meta:
        model = Staff
        template_name = 'django_tables2/bootstrap4.html'
        fields = (
            'user', 'department', 'phone', 'address',
            'is_active', 'edit', 'delete',
        )
