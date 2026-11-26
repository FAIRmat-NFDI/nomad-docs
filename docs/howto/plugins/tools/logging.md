# How to write logs

NOMAD uses *structured* logging based on [structlog](https://structlog.readthedocs.io/en/stable/){:target="_blank" rel="noopener"}. Instead of encoding information in the log message, you log a short *event* together with key-value pairs that give it context. Each log entry is stored as a JSON dictionary with `@timestamp`, `level`, `logger_name`, and `event`, plus your context data. In NOMAD deployments, log entries are collected in a central Elasticsearch database. To keep that database useful, log entries need to be sensible in size, frequency, meaning, level, and logger name.

## Get a logger

In many places, a logger is already provided to you. For example, parsers receive one in `parse(mainfile, archive, logger)` and normalizers in `normalize(archive, logger)`. These loggers already have context bound to them, such as the upload and entry being processed, so always use them instead of creating your own. Look for `get_logger` methods or `logger` attributes.

If no logger is provided, use `nomad.utils.get_logger`. Never use Python's built-in `logging` module directly.

```python
from nomad.utils import get_logger

logger = get_logger(__name__)
```

These loggers work like standard Python loggers, but also accept keyword arguments with context data:

```python
logger.warning('unknown unit', unit=unit_name, quantity='temperature')
```

## Write good log events

- **Keep events short.** The event is what is usually called the *message*, for example `file uploaded` or `extraction failed`. Put all other information into the context.
- **Structure your context keys.** The set of all keys across all log entries can become large. Prefix keys with your module or plugin name, for example `myparser_version` instead of `version`, so that they are easy to find.
- **Log the state of the software, not user behaviour.** Choose the log level based on what it says about NOMAD itself, not about user input or data. For example, a user uploading an invalid file should never be logged as an error.
- **Do not log everything.** Think about how you would use the logs to investigate a bug or failure, and log what helps with that.
- **Do not log sensitive data.**
- **Think before logging large data**, such as dictionaries, lists, or NumPy arrays.
- **Do not use logs for `print`-style debugging.**

## Keys in the final logs

The final logs are piped to Logstash. Key names are formed by a separate formatter, so they may differ from the names used in the log call.

Keys that are added to all logs:

- `@timestamp`: timestamp of the log entry
- `@version`: version of the logger
- `host`: host name the log entry originated from
- `path`: path of the module that created the log entry
- `tags`: tags for this log entry
- `type`: *message_type* as set in the `LogstashFormatter`
- `level`: log level: `DEBUG`, `INFO`, `WARNING`, or `ERROR`
- `logger_name`: name of the logger
- `nomad.service`: service name as configured in the NOMAD configuration
- `nomad.release`: release name as configured in the NOMAD configuration

Keys that are added to events related to processing an entry:

- `nomad.upload_id`: ID of the upload being processed
- `nomad.entry_id`: ID of the entry being processed
- `nomad.mainfile`: mainfile of the entry being processed

Keys that are added to events related to exceptions:

- `exc_info`: the full Python exception. All uncaught exceptions are stored here automatically.
- `digest`: the last 256 characters of the exception message. Unlike `exc_info`, this key is indexed, so use it to search for exceptions in [Kibana](https://www.elastic.co/kibana){:target="_blank" rel="noopener"}.
