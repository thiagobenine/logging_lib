# Biblioteca LoggingConfigBuilder

## Descrição
Biblioteca para configuração de logging em Python, integrada com New Relic para adicionar IDs de correlação aos logs

## Utilização
- **Default**: Utilize a configuração padrão para um setup rápido
- **Personalizado**: Adicione formatters, handlers e loggers personalizados conforme a necessidade

## Exemplos

### Uso Padrão
```python
from logging_lib.logging_config import LoggingConfigBuilder

config = LoggingConfigBuilder.get_default()
logger_config = config.build()
```

### Uso Personalizado
```python
from logging_lib.logging_config import LoggingConfigBuilder

config = LoggingConfigBuilder()
config.add_formatter('simple', 'logging.Formatter', format='%(levelname)s:%(message)s')
config.add_handler('console', 'logging.StreamHandler', formatter='simple', level='DEBUG')
config.add_logger('my_logger', handlers=['console'], level='DEBUG')
logger_config = config.build()
```

## Contribuição
Contribuições são bem-vindas. Faça um fork, modifique e submeta um pull request

