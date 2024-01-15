from .models import backup
from ariadne import convert_kwargs_to_snake_case


def listBackups_resolver(obj, info):
    try:
        backups = [bkup.to_dict() for bkup in backup.query.all()]
        print(backups)
        payload = {
            "success": True,
            "backups": backups
        }
    except Exception as error:
        print(error)
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload

@convert_kwargs_to_snake_case
def getBackup_resolver(obj, info, id):
    try:
        bkup = backup.query.get(id)
        payload = {
            "success": True,
            "backup": bkup.to_dict()
        }
    except AttributeError:  # todo not found
        payload = {
            "success": False,
            "errors": ["Backup matching {id} not found"]
        }
    return payload