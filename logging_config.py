from typing import Any, Dict, Self

class LoggingConfigBuilder:
    def __init__(self):
        self.config: Dict[str, Any] = {
            "version": 1,
            "disable_existing_loggers": False,
            "formatters": {},
            "handlers": {},
            "loggers": {},
        }

    def add_formatter(self, name: str, formatter_class: str, **kwargs) -> Self:
        self.config["formatters"][name] = {
            "()": formatter_class,
            **kwargs
        }
        return self

    def add_handler(self, name: str, handler_class: str, formatter: str, **kwargs) -> Self:
        self.config["handlers"][name] = {
            "class": handler_class,
            "formatter": formatter,
            **kwargs,
        }
        return self

    def add_logger(self, name: str, handlers: list, level: str) -> Self:
        self.config["loggers"][name] = {
            "handlers": handlers, 
            "level": level
        }
        return self

    def build(self) -> Dict[str, Any]:
        return self.config
    
    @classmethod
    def get_default(cls, level: str = "INFO") -> Self:
        builder = cls()
        builder.add_formatter(
            name="json_formatter", 
            formatter_class="logging_lib.formatters.new_relic_correlation.CorrelationIDNewRelicContextFormatter"
        )
        builder.add_handler(
            name="console", 
            handler_class="logging.StreamHandler", 
            formatter="json_formatter"
        )
        builder.add_logger(
            name="", 
            handlers=["console"], 
            level=level
        )
        builder.add_logger(
            name="fastapi", 
            handlers=["console"], 
            level=level
        )
        return builder
