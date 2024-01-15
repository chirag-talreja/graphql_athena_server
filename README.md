# graphql_athena_server

pip install -r requirements.txt

To start the server:
flask run

http://localhost:5000/graphql


To get all backups:

query AllBackups{
  listBackups{
    success
    errors
    backups{
      id
      name
      source_id
      backup_type
      target_system_name
      target_system_type
      time_stamp
      size_in_bytes
    }
  }
}

To get backup with specific id:

query GetBackup {
  getBackup(id: "<backup_id>") {
    backup {
      id
      name
      source_id
      backup_type
      target_system_name
      target_system_type
      time_stamp
      size_in_bytes
    }
    success
    errors
  }
}