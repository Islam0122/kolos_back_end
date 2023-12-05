from django.utils.html import format_html


class ChangeHistoryMixin:
    def list_changes(self, obj):
        fields = ""
        if obj.prev_record:
            delta = obj.diff_against(obj.prev_record)

            for change in delta.changes:
                field_verbose_name = obj._meta.get_field(change.field).verbose_name
                fields += str(
                    "Изменено <strong>{}</strong> с <span style='background-color:#ffb5ad'>{}</span> на "
                    "<span style='background-color:#b3f7ab'>{}</span> . <br/>".format(
                        field_verbose_name, change.old, change.new))
            return format_html(fields)
        return None

    history_list_display = ["list_changes"]
