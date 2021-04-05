from typing import Optional
from fastapi import APIRouter, Depends, Response, status

from ..models.operations import Operation, OperationKind, OperationCreate, OperationUpdate
from ..services.operations import OperationsService
from ..services.auth import get_current_user
from ..models.auth import User

router = APIRouter(prefix='/operations', tags=['operations'])


@router.get('/', response_model=list[Operation])
def get_operations(
        kind: Optional[OperationKind] = None,
        user: User = Depends(get_current_user),
        service: OperationsService = Depends()
):
    """
    Получение списка операций

    - **kind**: Фильтр по виду операций.
    \f
    Args:
        kind (Optional[OperationKind], optional): Defaults to None.
        user (User, optional): Defaults to Depends(get_current_user).
        service (OperationsService, optional): Defaults to Depends().

    Returns:
    """
    return service.get_list(user_id=user.id, kind=kind)


@router.post('/', response_model=Operation)
def create_operation(
    operation_data: OperationCreate,
    user: User = Depends(get_current_user),
    service: OperationsService = Depends()
):
    """
    Создать операцию
    \f

    Args:
        operation_data (OperationCreate):
        user (User, optional): Defaults to Depends(get_current_user).
        service (OperationsService, optional): Defaults to Depends().

    Returns:
    """
    return service.create_operation(user_id=user.id, operation_data=operation_data)


@router.get('/{operation_id}', response_model=Operation)
def get_operation(
    operation_id: int,
    user: User = Depends(get_current_user),
    service: OperationsService = Depends()
):
    """
    Получить операцию по id
    - **operation_id**: id операции.
    \f

    Args:
        operation_id (int):
        user (User, optional): Defaults to Depends(get_current_user).
        service (OperationsService, optional): Defaults to Depends().

    Returns:
    """
    return service.get_operation(user_id=user.id, operation_id=operation_id)


@router.put('/{operation_id}', response_model=Operation)
def update_operation(
    operation_id: int,
    operation_data: OperationUpdate,
    user: User = Depends(get_current_user),
    service: OperationsService = Depends()
):
    """
    Изменить операцию по id
    - **operation_id**: id операции.
    \f
    Args:
        operation_id (int):
        operation_data (OperationUpdate):
        user (User, optional): Defaults to Depends(get_current_user).
        service (OperationsService, optional): Defaults to Depends().

    Returns:
    """
    return service.update_operation(user_id=user.id, operation_id=operation_id, operation_data=operation_data)


@router.delete('/{operation_id}')
def delete_operation(
    operation_id: int,
    user: User = Depends(get_current_user),
    service: OperationsService = Depends()
):
    """
    Удалить операцию по id
    - **operation_id**: id операции.
    \f

    Args:
        operation_id (int):
        user (User, optional): Defaults to Depends(get_current_user).
        service (OperationsService, optional): Defaults to Depends().

    Returns:
    """
    service.delete_operation(user_id=user.id, operation_id=operation_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
