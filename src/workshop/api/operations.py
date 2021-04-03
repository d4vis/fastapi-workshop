from typing import Optional
from fastapi import APIRouter, Depends, Response, status

from ..models.operations import Operation, OperationKind, OperationCreate, OperationUpdate
from ..services.operations import OperationsService
from ..services.auth import get_current_user
from ..models.auth import User

router = APIRouter(prefix='/operations')


@router.get('/', response_model=list[Operation])
def get_operations(
        kind: Optional[OperationKind] = None,
        user: User = Depends(get_current_user),
        service: OperationsService = Depends()
):
    return service.get_list(user_id=user.id, kind=kind)


@router.post('/', response_model=Operation)
def create_operation(
    operation_data: OperationCreate,
    user: User = Depends(get_current_user),
    service: OperationsService = Depends()
):
    return service.create_operation(user_id=user.id, operation_data=operation_data)


@router.get('/{operation_id}', response_model=Operation)
def get_operation(
    operation_id: int,
    user: User = Depends(get_current_user),
    service: OperationsService = Depends()
):
    return service.get_operation(user_id=user.id, operation_id=operation_id)


@router.put('/{operation_id}', response_model=Operation)
def update_operation(
    operation_id: int,
    operation_data: OperationUpdate,
    user: User = Depends(get_current_user),
    service: OperationsService = Depends()
):
    return service.update_operation(user_id=user.id, operation_id=operation_id, operation_data=operation_data)


@router.delete('/{operation_id}')
def delete_operation(
    operation_id: int,
    user: User = Depends(get_current_user),
    service: OperationsService = Depends()
):
    service.delete_operation(user_id=user.id, operation_id=operation_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
