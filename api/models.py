
from sqlalchemy import create_engine, String, Column, DateTime, Integer
from app import athena_connection

class backup(athena_connection.Model):
    id = athena_connection.Column(athena_connection.String, primary_key=True)
    name= athena_connection.Column(athena_connection.String)
    source_id= athena_connection.Column(athena_connection.String)
    backup_type= athena_connection.Column(athena_connection.String)
    app_type= athena_connection.Column(athena_connection.String)
    backup_mode= athena_connection.Column(athena_connection.String)
    backup_granularity= athena_connection.Column(athena_connection.String)
    point_in_time= athena_connection.Column(athena_connection.String)
    expires_at= athena_connection.Column(athena_connection.String)
    protection_store_id= athena_connection.Column(athena_connection.String)
    protection_store_type= athena_connection.Column(athena_connection.String)
    dataorchestrator_id= athena_connection.Column(athena_connection.String)
    target_system_id= athena_connection.Column(athena_connection.String)
    target_system_name= athena_connection.Column(athena_connection.String)
    target_system_type= athena_connection.Column(athena_connection.String)
    time_stamp= athena_connection.Column(athena_connection.DateTime)
    size_in_bytes= athena_connection.Column(athena_connection.Integer)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "source_id": self.source_id,
            "backup_type": self.backup_type,
            "app_type": self.app_type,
            "backup_mode": self.backup_mode,
            "backup_granularity": self.backup_granularity,
            "point_in_time": self.point_in_time,
            "expires_at": self.expires_at,
            "protection_store_id": self.protection_store_id,
            "protection_store_type": self.protection_store_type,
            "dataorchestrator_id": self.dataorchestrator_id,
            "target_system_id": self.target_system_id,
            "target_system_name": self.target_system_name,
            "target_system_type": self.target_system_type,
            "time_stamp": self.time_stamp,
            "size_in_bytes": self.size_in_bytes

        }
