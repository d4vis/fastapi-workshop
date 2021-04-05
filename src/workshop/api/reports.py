from fastapi import APIRouter, Depends, File, UploadFile, BackgroundTasks
from fastapi.responses import StreamingResponse

from ..services.reports import ReportsService
from ..services.auth import get_current_user
from ..models.auth import User


router = APIRouter(prefix='/reports', tags=['reports'])


@router.post('/import')
def import_csv(
    background_tasks: BackgroundTasks,
    file: UploadFile = File(...),
    user: User = Depends(get_current_user),
    reports_service: ReportsService = Depends(),
):
    """
    Импорт из csv файла
    \f

    Args:
        background_tasks (BackgroundTasks): 
        file (UploadFile, optional):  Defaults to File(...).
        user (User, optional):  Defaults to Depends(get_current_user).
        reports_service (ReportsService, optional):  Defaults to Depends().
    """
    background_tasks.add_task(
        reports_service.import_csv,
        user_id=user.id,
        file=file.file,
    )
    return ''


@router.get('/export')
def export_csv(
        user: User = Depends(get_current_user),
        reports_service: ReportsService = Depends()
):
    """
    Экспорт в csv файл
    \f

    Args:
        user (User, optional): [description]. Defaults to Depends(get_current_user).
        reports_service (ReportsService, optional): [description]. Defaults to Depends().

    Returns:
    """
    report = reports_service.export_csv(user_id=user.id)
    return StreamingResponse(
        content=report,
        media_type='text/csv',
        headers={
            'Content-Disposition': 'attachment; filename=report.csv'
        }
    )
