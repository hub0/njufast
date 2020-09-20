class DataRouter:
    """
    A router to control all HIFAST data related operations on models
    in the database application.  Point all operation on database model
    to data.
    """

    route_app_labels = {'database'}

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'data'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'data'
        return None
             
    def allow_relation(self, obj1, obj2, **hints):
        """
        Relations between two objects both in 'data' db is allowed,
        between a data db model and a non 'data' db model is not 
        allowed, otherwise no opinion.
        """
        db_set = {'data',}
        if obj1._state.db in db_set and obj2._state.db in db_set:
            return True
        elif obj1._state.db in db_set or obj2._state.db in db_set:
            return False
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Ensure database model appears only in the 'data' database 
        """
        if app_label in self.route_app_labels:
            return db == 'data'
        return None


class PrimaryRouter:
    """
    The default router
    """
    def db_for_read(self, model, **hints):
        return 'primary'
    
    def db_for_write(self, model, **hints):
        return 'primary'

    def allow_relation(self, obj1, obj2, **hints):
        return True

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        return True

    
