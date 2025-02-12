import functools
import uuid

from django.conf import settings
from django.core.files.storage import default_storage



def upload_file_to(
    instance,
    filename: str,
    main_folder_name: str,
) -> str:
    """Upload instance's `file` to unique folder.

    Args:
        instance (typing.Union[ImportJob, ExportJob]): instance of job model
        main_folder_name(str): main folder -> import or export
        filename (str): file name of document's file

    Returns:
        str: Generated path for document's file.

    """
    return (
        "import_export_extensions/"
        f"{main_folder_name}/{uuid.uuid4()}/{filename}"
    )

def select_storage(key):
    """Return a storage callable from settings if it exists.

    Returns:
        Storage: A storage instance to handle file operations

    """
    custom_storage = getattr(
        settings,
        key,
        None,
    )
    if custom_storage is not None and callable(custom_storage):
        return custom_storage()

    return default_storage


upload_export_file_to = functools.partial(
    upload_file_to,
    main_folder_name="export",
)
upload_import_file_to = functools.partial(
    upload_file_to,
    main_folder_name="import",
)
upload_import_error_file_to = functools.partial(
    upload_file_to,
    main_folder_name="errors",
)
