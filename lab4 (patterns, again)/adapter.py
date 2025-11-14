class ExternalLogger:
    """Сторонний логгер с несовместимым интерфейсом."""
    def log_message(self, msg):
        print(f"[ExternalLogger] {msg}")


class Logger:
    """Интерфейс логгера, который ожидает наш код."""
    def log(self, message):
        raise NotImplementedError


class LoggerAdapter(Logger):
    """Адаптер: делает ExternalLogger совместимым с Logger."""
    def __init__(self, external_logger):
        self._external_logger = external_logger

    def log(self, message):
        # Адаптируем вызов к нужному методу
        self._external_logger.log_message(message)

if __name__ == "__main__":
    print("=== ADAPTER ===")
    external = ExternalLogger()
    logger = LoggerAdapter(external)

    logger.log("Приложение запущено")
    logger.log("Ошибка: что-то пошло не так")
