import uuid
from contextvars import ContextVar
from newrelic.api.log import NewRelicContextFormatter

NO_CORRELATION = "NO_CORRELATION"


class CorrelationEntity:
    id: str

    __slots__ = ("id",)

    def __init__(self, value: str | None = "") -> None:
        self.id = value or str(uuid.uuid4())


_context: ContextVar[CorrelationEntity] = ContextVar(
    "correlation", default=CorrelationEntity(NO_CORRELATION)
)


class Correlation:
    HEADER_KEY = "X-Correlation-ID"

    @classmethod
    def get_id(cls) -> str:
        return _context.get().id

    @staticmethod
    def set_id(value: str | None) -> None:
        _context.set(CorrelationEntity(value))

    @classmethod
    def build_header(cls) -> dict[str, str]:
        return {cls.HEADER_KEY: cls.get_id()}
    

class CorrelationIDNewRelicContextFormatter(NewRelicContextFormatter):
    @classmethod
    def log_record_to_dict(cls, record):
        output = super().log_record_to_dict(record)
        output.update({"correlation_id": Correlation.get_id()})
        return output

