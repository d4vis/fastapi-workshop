from typing import Optional
from fastapi import APIRouter, Depends

from ..database import get_session
from ..models.operations import Operation, OperationKind
from ..services.operations import OperationsService

router = APIRouter(prefix='/operations')


@router.get('/', response_model=list[Operation])
def get_operations(
        kind: Optional[OperationKind] = None,
        service: OperationsService = Depends()
):
    return service.get_list(kind=kind)
