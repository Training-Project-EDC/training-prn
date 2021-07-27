# Generated by Django 3.1.4 on 2021-07-26 23:02

import _socket
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
import django_revision.revision_field
import edc_base.model_fields.custom_fields
import edc_base.model_fields.hostname_modification_field
import edc_base.model_fields.userfield
import edc_base.model_fields.uuid_auto_field
import edc_base.model_validators.date
import edc_base.sites.managers
import edc_base.utils
import edc_protocol.validators
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SubjectOffStudy',
            fields=[
                ('created', models.DateTimeField(blank=True, default=edc_base.utils.get_utcnow)),
                ('modified', models.DateTimeField(blank=True, default=edc_base.utils.get_utcnow)),
                ('user_created', edc_base.model_fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user created')),
                ('user_modified', edc_base.model_fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user modified')),
                ('hostname_created', models.CharField(blank=True, default=_socket.gethostname, help_text='System field. (modified on create only)', max_length=60)),
                ('hostname_modified', edc_base.model_fields.hostname_modification_field.HostnameModificationField(blank=True, help_text='System field. (modified on every save)', max_length=50)),
                ('revision', django_revision.revision_field.RevisionField(blank=True, editable=False, help_text='System field. Git repository tag:branch:commit.', max_length=75, null=True, verbose_name='Revision')),
                ('device_created', models.CharField(blank=True, max_length=10)),
                ('device_modified', models.CharField(blank=True, max_length=10)),
                ('id', edc_base.model_fields.uuid_auto_field.UUIDAutoField(blank=True, editable=False, help_text='System auto field. UUID primary key.', primary_key=True, serialize=False)),
                ('offschedule_datetime', models.DateTimeField(default=edc_base.utils.get_utcnow, validators=[edc_protocol.validators.datetime_not_before_study_start, edc_base.model_validators.date.datetime_not_future], verbose_name='Date and time subject taken off schedule')),
                ('action_identifier', models.CharField(max_length=25, null=True)),
                ('tracking_identifier', models.CharField(max_length=30, null=True)),
                ('related_tracking_identifier', models.CharField(max_length=30, null=True)),
                ('parent_tracking_identifier', models.CharField(max_length=30, null=True)),
                ('subject_identifier', models.CharField(max_length=50, unique=True)),
                ('offstudy_date', models.DateField(default=edc_base.utils.get_utcnow, null=True, validators=[edc_protocol.validators.date_not_before_study_start, edc_base.model_validators.date.date_not_future], verbose_name='Date of completion or discontinuation')),
                ('report_datetime', models.DateTimeField(default=edc_base.utils.get_utcnow, help_text="If reporting today, use today's date/time, otherwise use the date/time this information was reported.", null=True, validators=[edc_protocol.validators.datetime_not_before_study_start, edc_base.model_validators.date.datetime_not_future], verbose_name='Report Date and Time')),
                ('completed_study', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3, verbose_name='Did the subject complete the study?')),
                ('reason', models.CharField(blank=True, choices=[('death', 'Death'), ('ltfu', 'Lost to follow up'), ('sponsor_terminated', 'Study terminated by sponsor'), ('subject_withdrawal', 'Withdrawal by subject'), ('pregnancy', 'Pregnancy'), ('adverse_event', 'Adverse Event'), ('OTHER', 'Other, specify')], max_length=115, null=True, verbose_name='No, primary reason for early discontinuation')),
                ('reason_other', edc_base.model_fields.custom_fields.OtherCharField(blank=True, max_length=35, null=True, verbose_name='If Other, specify ...')),
                ('death_date', models.DateField(blank=True, help_text='(derived, no entry required)', null=True, verbose_name='Date of death')),
                ('comment', models.TextField(blank=True, max_length=250, null=True, verbose_name='Comment')),
                ('site', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, to='sites.site')),
            ],
            options={
                'verbose_name': 'Subject Off Study',
                'verbose_name_plural': 'Subject Off Study',
            },
            managers=[
                ('objects', django.db.models.manager.Manager()),
                ('on_site', edc_base.sites.managers.CurrentSiteManager()),
            ],
        ),
        migrations.CreateModel(
            name='HistoricalSubjectOffStudy',
            fields=[
                ('created', models.DateTimeField(blank=True, default=edc_base.utils.get_utcnow)),
                ('modified', models.DateTimeField(blank=True, default=edc_base.utils.get_utcnow)),
                ('user_created', edc_base.model_fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user created')),
                ('user_modified', edc_base.model_fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user modified')),
                ('hostname_created', models.CharField(blank=True, default=_socket.gethostname, help_text='System field. (modified on create only)', max_length=60)),
                ('hostname_modified', edc_base.model_fields.hostname_modification_field.HostnameModificationField(blank=True, help_text='System field. (modified on every save)', max_length=50)),
                ('revision', django_revision.revision_field.RevisionField(blank=True, editable=False, help_text='System field. Git repository tag:branch:commit.', max_length=75, null=True, verbose_name='Revision')),
                ('device_created', models.CharField(blank=True, max_length=10)),
                ('device_modified', models.CharField(blank=True, max_length=10)),
                ('id', edc_base.model_fields.uuid_auto_field.UUIDAutoField(blank=True, db_index=True, editable=False, help_text='System auto field. UUID primary key.')),
                ('offschedule_datetime', models.DateTimeField(default=edc_base.utils.get_utcnow, validators=[edc_protocol.validators.datetime_not_before_study_start, edc_base.model_validators.date.datetime_not_future], verbose_name='Date and time subject taken off schedule')),
                ('action_identifier', models.CharField(max_length=25, null=True)),
                ('tracking_identifier', models.CharField(max_length=30, null=True)),
                ('related_tracking_identifier', models.CharField(max_length=30, null=True)),
                ('parent_tracking_identifier', models.CharField(max_length=30, null=True)),
                ('subject_identifier', models.CharField(db_index=True, max_length=50)),
                ('offstudy_date', models.DateField(default=edc_base.utils.get_utcnow, null=True, validators=[edc_protocol.validators.date_not_before_study_start, edc_base.model_validators.date.date_not_future], verbose_name='Date of completion or discontinuation')),
                ('report_datetime', models.DateTimeField(default=edc_base.utils.get_utcnow, help_text="If reporting today, use today's date/time, otherwise use the date/time this information was reported.", null=True, validators=[edc_protocol.validators.datetime_not_before_study_start, edc_base.model_validators.date.datetime_not_future], verbose_name='Report Date and Time')),
                ('completed_study', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3, verbose_name='Did the subject complete the study?')),
                ('reason', models.CharField(blank=True, choices=[('death', 'Death'), ('ltfu', 'Lost to follow up'), ('sponsor_terminated', 'Study terminated by sponsor'), ('subject_withdrawal', 'Withdrawal by subject'), ('pregnancy', 'Pregnancy'), ('adverse_event', 'Adverse Event'), ('OTHER', 'Other, specify')], max_length=115, null=True, verbose_name='No, primary reason for early discontinuation')),
                ('reason_other', edc_base.model_fields.custom_fields.OtherCharField(blank=True, max_length=35, null=True, verbose_name='If Other, specify ...')),
                ('death_date', models.DateField(blank=True, help_text='(derived, no entry required)', null=True, verbose_name='Date of death')),
                ('comment', models.TextField(blank=True, max_length=250, null=True, verbose_name='Comment')),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_id', edc_base.model_fields.uuid_auto_field.UUIDAutoField(primary_key=True, serialize=False)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('site', models.ForeignKey(blank=True, db_constraint=False, editable=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='sites.site')),
            ],
            options={
                'verbose_name': 'historical Subject Off Study',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='DeathReport',
            fields=[
                ('created', models.DateTimeField(blank=True, default=edc_base.utils.get_utcnow)),
                ('modified', models.DateTimeField(blank=True, default=edc_base.utils.get_utcnow)),
                ('user_created', edc_base.model_fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user created')),
                ('user_modified', edc_base.model_fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user modified')),
                ('hostname_created', models.CharField(blank=True, default=_socket.gethostname, help_text='System field. (modified on create only)', max_length=60)),
                ('hostname_modified', edc_base.model_fields.hostname_modification_field.HostnameModificationField(blank=True, help_text='System field. (modified on every save)', max_length=50)),
                ('revision', django_revision.revision_field.RevisionField(blank=True, editable=False, help_text='System field. Git repository tag:branch:commit.', max_length=75, null=True, verbose_name='Revision')),
                ('device_created', models.CharField(blank=True, max_length=10)),
                ('device_modified', models.CharField(blank=True, max_length=10)),
                ('id', edc_base.model_fields.uuid_auto_field.UUIDAutoField(blank=True, editable=False, help_text='System auto field. UUID primary key.', primary_key=True, serialize=False)),
                ('action_identifier', models.CharField(max_length=25, null=True)),
                ('subject_identifier', models.CharField(max_length=50)),
                ('tracking_identifier', models.CharField(max_length=30, null=True)),
                ('related_tracking_identifier', models.CharField(max_length=30, null=True)),
                ('parent_tracking_identifier', models.CharField(max_length=30, null=True)),
                ('report_datetime', models.DateTimeField(default=edc_base.utils.get_utcnow, help_text='Date and time of report.', verbose_name='Report Date and Time')),
                ('death_date', models.DateField(default=edc_base.utils.get_utcnow, verbose_name='Death date')),
                ('cause_of_death', models.CharField(choices=[('autopsy', 'Autopsy'), ('clinical_records', 'Clinical records'), ('information', 'Information from study care taker staff prior participant death'), ('contact', 'Contact with other (non-study) physician/nurse/other health care provider'), ('death_certificate', 'Death Certificate'), ('participants_relatives', 'Information from participants relatives or friends Obituary'), ('information_requested', 'Information requested, still pending'), ('no_information', 'No information will ever be available'), ('OTHER', 'Other')], max_length=50, verbose_name='What is the primary source of cause of death information?')),
                ('cause_of_death_other', models.CharField(max_length=50, verbose_name='Other, specify')),
                ('perform_autopsy', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=20, verbose_name='Will an autopsy be performed later')),
                ('major_cause_of_death', models.TextField(help_text='(Note: Cardiac and pulmonary arrest are not major reasons and should not be used to describe major cause) ', max_length=50, verbose_name='Describe the major cause of death (including pertinent autopsy information if available), starting with the first noticeable illness thought to be related to death, continuing to time of death.')),
                ('description', models.CharField(choices=[('study_drug', 'Toxicity from Study Drug'), ('non_study_drug', 'Toxicity from non-Study drug'), ('trauma', 'Trauma/Accident'), ('no_info', 'No information available'), ('OTHER', 'Other, specify')], max_length=50, verbose_name='Based on the description above, what category bestdefines the major cause of death?')),
                ('description_other', models.CharField(max_length=50, verbose_name='Other, specify')),
                ('duration_acute_illness', models.IntegerField(help_text='(in days (If unknown enter -1))', verbose_name='Duration of acute illness directly causing death')),
                ('medical_responsibility', models.CharField(choices=[('doctor', 'Doctor'), ('nurse', 'Nurse'), ('traditional', 'Traditional Healer'), ('all', 'Both Doctor or Nurse and Traditional Healer'), ('none', 'No known medical care received (family/friends only)')], max_length=50, verbose_name='Who was responsible for primary medical care of the participant during the month prior to death?')),
                ('participant_hospitalized', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3, verbose_name='Was the participant hospitalised before death?')),
                ('reason_participant_hospitalized', models.CharField(choices=[('respiratory illness(unspecified)', 'Respiratory Illness(unspecified)'), ('respiratory illness, cxr confirmed', 'Respiratory Illness, CXR confirmed'), ('respiratory illness, cxr confirmed, bacterial pathogen, specify', 'Respiratory Illness, CXR confirmed, bacterial pathogen, specify'), ('respiratory illness, cxr confirmed, tb or probable tb', 'Respiratory Illness, CXR confirmed, TB or probable TB'), ('diarrhea illness(unspecified)', 'Diarrhea Illness(unspecified)'), ('diarrhea illness, viral or bacterial pathogen, specify', 'Diarrhea Illness, viral or bacterial pathogen, specify'), ('sepsis(unspecified)', 'Sepsis(unspecified)'), ('sepsis, pathogen specified, specify', 'Sepsis, pathogen specified, specify'), ('mengitis(unspecified)', 'Mengitis(unspecified)'), ('mengitis, pathogen specified, specify', 'Mengitis, pathogen specified, specify'), ('non-infectious reason for hospitalization, specify', 'Non-infectious reason for hospitalization, specify'), ('OTHER', 'Other infection, specify')], max_length=65, verbose_name='Was the participant hospitalised before death?')),
                ('reason_participant_hospitalized_other', models.CharField(max_length=50, verbose_name='If other illness or pathogen specify or non infectious reason, please specify')),
                ('period_hospitalized', models.IntegerField(verbose_name='For how many days was the participant hospitalised during the illness immediately before death?')),
                ('comments', models.TextField(verbose_name='Comments')),
                ('site', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, to='sites.site')),
            ],
            options={
                'verbose_name': 'Death Report',
                'verbose_name_plural': 'Death Report',
            },
        ),
    ]
