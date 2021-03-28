from typing import Optional
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from .. import tables
from ..database import get_session
from ..models.operations import OperationCreate, OperationKind


class OperationsService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def get_list(self, kind: Optional[OperationKind] = None) -> list[tables.Operation]:
        query = self.session.query(tables.Operation)
        if kind:
            query = query.filter_by(kind=kind)
        operations = query.all()
        return operations

    def get_operation(self, operation_id: int) -> tables.Operation:
        operation = self.session.query(
            tables.Operation).filter_by(id=operation_id).first()
        if not operation:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        return operation

    def create_operation(self, operation_data: OperationCreate) -> tables.Operation:
        operation = tables.Operation(**operation_data.dict())
        self.session.add(operation)
        self.session.commit()
        return operation
