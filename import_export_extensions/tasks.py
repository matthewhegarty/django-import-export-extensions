import logging

from celery import shared_task

from . import models

logger = logging.getLogger(__name__)


@shared_task()
def parse_data_task(job_id: int):
    """Async task for starting data parsing."""
    logger.debug("Starting data parse")
    try:
        models.ImportJob.objects.get(pk=job_id).parse_data()
        logger.debug("Completed data parse")
    except Exception:
        logger.exception("parse failed")


@shared_task()
def import_data_task(job_id: int):
    """Async task for starting data import."""
    logger.debug("Starting data import")
    try:
        models.ImportJob.objects.get(pk=job_id).import_data()
        logger.debug("Completed data import")
    except Exception:
        logger.exception("import failed")


@shared_task()
def export_data_task(job_id: int):
    """Async task for starting data export."""
    job = models.ExportJob.objects.get(id=job_id)
    job.export_data()
