from django.contrib.admin import AdminSite as DjangoAdminSite


class AdminSite(DjangoAdminSite):
    site_url = '/administration/'
    enable_nav_sidebar = False
    site_header = 'Training PRN'
    site_title = 'Training PRN'
    index_title = 'Training PRN'


training_prn_admin = AdminSite(name='training_prn_admin')
