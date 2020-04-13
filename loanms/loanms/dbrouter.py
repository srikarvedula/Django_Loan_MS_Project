from django.conf import settings

class AppRouter:

    def db_for_read(self, model, **hints):
        """
        Attempts to read user models go to mysql_db.
        """
        if model._meta.app_label == 'webservices':
            return 'mysql_db'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write user models go to mysql_db.
        """
        if model._meta.app_label == 'webservices':
            return 'mysql_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):

        if obj1._meta.app_label == 'webservices' or \
           obj2._meta.app_label == 'webservices':
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'webservices':
            return db == 'mysql_db'
        return None