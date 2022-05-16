from django.db import models


class Adresses(models.Model):
    id = models.BigAutoField(primary_key=True)
    type_of_adress = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    entity = models.CharField(max_length=255, blank=True, null=True)
    number_and_street = models.CharField(max_length=255, blank=True, null=True)
    suite_or_appartment = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    postal_code = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    notes = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    state = models.CharField(max_length=255, blank=True, null=True)
    latitude = models.CharField(max_length=255, blank=True, null=True)
    longitude = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'adresses'


class ArInternalMetadata(models.Model):
    key = models.CharField(primary_key=True, max_length=255)
    value = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ar_internal_metadata'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Batteries(models.Model):
    id = models.BigAutoField(primary_key=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    date_of_commissioning = models.DateField(blank=True, null=True)
    date_of_last_inspection = models.DateField(blank=True, null=True)
    certificate_of_operations = models.CharField(max_length=255, blank=True, null=True)
    information = models.CharField(max_length=255, blank=True, null=True)
    notes = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    building = models.ForeignKey('Buildings', models.DO_NOTHING, blank=True, null=True)
    employee_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'batteries'


class Buildings(models.Model):
    id = models.BigAutoField(primary_key=True)
    full_name_of_the_building_administrator = models.CharField(db_column='Full_Name_of_the_building_administrator', max_length=255, blank=True, null=True)  # Field name made lowercase.
    email_of_the_administrator_of_the_building = models.CharField(db_column='Email_of_the_administrator_of_the_building', max_length=255, blank=True, null=True)  # Field name made lowercase.
    phone_number_of_the_building_administrator = models.CharField(db_column='Phone_number_of_the_building_administrator', max_length=255, blank=True, null=True)  # Field name made lowercase.
    full_name_of_the_technical_contact_for_the_building = models.CharField(db_column='Full_Name_of_the_technical_contact_for_the_building', max_length=255, blank=True, null=True)  # Field name made lowercase.
    technical_contact_email_for_the_building = models.CharField(db_column='Technical_contact_email_for_the_building', max_length=255, blank=True, null=True)  # Field name made lowercase.
    technical_contact_phone_for_the_building = models.CharField(db_column='Technical_contact_phone_for_the_building', max_length=255, blank=True, null=True)  # Field name made lowercase.
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    customer = models.ForeignKey('Customers', models.DO_NOTHING, blank=True, null=True)
    adress = models.ForeignKey(Adresses, models.DO_NOTHING, blank=True, null=True)
    no_of_floors = models.IntegerField(db_column='No_of_floors', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'buildings'


class Columns(models.Model):
    id = models.BigAutoField(primary_key=True)
    set_type = models.CharField(max_length=255, blank=True, null=True)
    nb_of_floors_served = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    information = models.CharField(max_length=255, blank=True, null=True)
    notes = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    battery = models.ForeignKey(Batteries, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'columns'


class Customer(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer'


class Customers(models.Model):
    id = models.BigAutoField(primary_key=True)
    customers_creation_date = models.CharField(db_column='Customers_Creation_Date', max_length=255, blank=True, null=True)  # Field name made lowercase.
    company_name = models.CharField(db_column='Company_Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    full_name_of_the_company_contact = models.CharField(db_column='Full_Name_of_the_company_contact', max_length=255, blank=True, null=True)  # Field name made lowercase.
    company_contact_phone = models.CharField(db_column='Company_contact_phone', max_length=255, blank=True, null=True)  # Field name made lowercase.
    email_of_the_company_contact = models.CharField(db_column='Email_of_the_company_contact', max_length=255, blank=True, null=True)  # Field name made lowercase.
    company_description = models.CharField(db_column='Company_Description', max_length=255, blank=True, null=True)  # Field name made lowercase.
    full_name_of_servive_technical_authority = models.CharField(db_column='Full_Name_of_servive_Technical_Authority', max_length=255, blank=True, null=True)  # Field name made lowercase.
    technical_manager_email_for_servive = models.CharField(db_column='Technical_Manager_Email_for_Servive', max_length=255, blank=True, null=True)  # Field name made lowercase.
    technical_manager_email_for_service = models.CharField(db_column='Technical_Manager_Email_for_Service', max_length=255, blank=True, null=True)  # Field name made lowercase.
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    adress = models.ForeignKey(Adresses, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customers'


class Detailsbuildings(models.Model):
    id = models.BigAutoField(primary_key=True)
    information_key = models.CharField(max_length=255, blank=True, null=True)
    value = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    building = models.ForeignKey(Buildings, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'detailsbuildings'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Elevators(models.Model):
    id = models.BigAutoField(primary_key=True)
    serial_number = models.CharField(db_column='Serial_number', max_length=255, blank=True, null=True)  # Field name made lowercase.
    model = models.CharField(db_column='Model', max_length=255, blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=255, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=255, blank=True, null=True)  # Field name made lowercase.
    date_of_commissioning = models.CharField(db_column='Date_of_commissioning', max_length=255, blank=True, null=True)  # Field name made lowercase.
    date_of_last_inspection = models.CharField(db_column='Date_of_last_inspection', max_length=255, blank=True, null=True)  # Field name made lowercase.
    certificate_of_inspection = models.CharField(db_column='Certificate_of_inspection', max_length=255, blank=True, null=True)  # Field name made lowercase.
    information = models.CharField(db_column='Information', max_length=255, blank=True, null=True)  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=255, blank=True, null=True)  # Field name made lowercase.
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    column = models.ForeignKey(Columns, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'elevators'


class Employee(models.Model):
    id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    facial_keypoints = models.CharField(max_length=255, blank=True, null=True)
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employees'


class HibernateSequence(models.Model):
    next_val = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hibernate_sequence'


class InterventionServiceCustomer(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'intervention_service$customer'


class Interventions(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    author = models.CharField(max_length=255, blank=True, null=True)
    customerid = models.CharField(db_column='customerID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    buildingid = models.CharField(db_column='buildingID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    batteryid = models.CharField(db_column='batteryID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    columnid = models.CharField(db_column='columnID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    elevatorid = models.CharField(db_column='elevatorID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    start_intervention = models.DateTimeField(blank=True, null=True)
    end_intervention = models.DateTimeField(blank=True, null=True)
    result = models.CharField(max_length=255, blank=True, null=True)
    report = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    employee = models.CharField(max_length=255, blank=True, null=True)
    employeeid = models.IntegerField(db_column='employeeID', blank=True, null=True)  # Field name made lowercase.
    end_date_and_time_of_the_intervention = models.DateTimeField(blank=True, null=True)
    start_date_and_time_of_the_intervention = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'interventions'


class Leads(models.Model):
    id = models.BigAutoField(primary_key=True)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    cie_name = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    project_name = models.CharField(max_length=255, blank=True, null=True)
    project_description = models.CharField(max_length=255, blank=True, null=True)
    department_in_charge = models.CharField(max_length=255, blank=True, null=True)
    message = models.CharField(max_length=255, blank=True, null=True)
    attached_files = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'leads'


class Maps(models.Model):
    id = models.BigAutoField(primary_key=True)
    location_of_the_building = models.CharField(max_length=255, blank=True, null=True)
    no_of_floors_in_the_building = models.IntegerField(blank=True, null=True)
    client_name = models.CharField(max_length=255, blank=True, null=True)
    no_of_batteries = models.IntegerField(blank=True, null=True)
    no_of_columns = models.IntegerField(blank=True, null=True)
    no_of_elevators = models.IntegerField(blank=True, null=True)
    full_name_of_technical_contact = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    latitude = models.CharField(max_length=255, blank=True, null=True)
    longitude = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'maps'


class Mytests(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'mytests'


class Quotes(models.Model):
    id = models.BigAutoField(primary_key=True)
    building_type = models.CharField(max_length=255, blank=True, null=True)
    product_line = models.CharField(max_length=255, blank=True, null=True)
    no_of_apartments = models.IntegerField(blank=True, null=True)
    no_of_floors = models.IntegerField(blank=True, null=True)
    no_of_basements = models.IntegerField(blank=True, null=True)
    no_of_businesses = models.IntegerField(blank=True, null=True)
    no_of_parking_spaces = models.IntegerField(blank=True, null=True)
    no_of_elevator_cages = models.IntegerField(blank=True, null=True)
    max_of_occupants_per_floor = models.IntegerField(blank=True, null=True)
    no_of_hours_of_activities = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    no_of_elevators_needed = models.IntegerField(blank=True, null=True)
    unit_price = models.IntegerField(blank=True, null=True)
    total_price_of_elevators = models.IntegerField(blank=True, null=True)
    installation_fees = models.IntegerField(blank=True, null=True)
    final_price = models.IntegerField(blank=True, null=True)
    companyname = models.CharField(db_column='companyName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(max_length=255, blank=True, null=True)
    fullname = models.CharField(db_column='fullName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(max_length=255, blank=True, null=True)
    department = models.CharField(max_length=255, blank=True, null=True)
    projectname = models.CharField(db_column='projectName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    projectdesc = models.CharField(db_column='projectDesc', max_length=255, blank=True, null=True)  # Field name made lowercase.
    message = models.CharField(max_length=255, blank=True, null=True)
    processed = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'quotes'


class SchemaMigrations(models.Model):
    version = models.CharField(primary_key=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'schema_migrations'


class User(models.Model):
    id = models.BigAutoField(primary_key=True)
    email = models.CharField(unique=True, max_length=255)
    encrypted_password = models.CharField(max_length=255)
    reset_password_token = models.CharField(unique=True, max_length=255, blank=True, null=True)
    reset_password_sent_at = models.DateTimeField(blank=True, null=True)
    remember_created_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    admin = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'
