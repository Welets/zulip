from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("zerver", "0699_set_default_for_can_create_topics_group"),
    ]

    operations = [
        migrations.AlterField(
            model_name="stream",
            name="can_create_topics_group",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.RESTRICT,
                related_name="+",
                to="zerver.usergroup",
            ),
        ),
    ]