"""Žurnāla servisa skelets."""


class LogService:
    """Reģistrē lietotnes darbības un kļūdas lokālā žurnālā."""

    def configure(self) -> None:
        """Inicializē žurnāla konfigurāciju."""

        raise NotImplementedError("Logēšanas konfigurācija vēl nav izveidota.")

    def info(self, message: str) -> None:
        """Saglabā informatīvu ierakstu.

        Args:
            message: Ziņojuma teksts.
        """

        raise NotImplementedError("Info ieraksts vēl nav izveidots.")

    def warning(self, message: str) -> None:
        """Saglabā brīdinājuma ierakstu.

        Args:
            message: Ziņojuma teksts.
        """

        raise NotImplementedError("Warning ieraksts vēl nav izveidots.")

    def error(self, message: str, exc: Exception | None = None) -> None:
        """Saglabā kļūdas ierakstu.

        Args:
            message: Ziņojuma teksts.
            exc: Papildu izņēmuma objekts, ja pieejams.
        """

        raise NotImplementedError("Error ieraksts vēl nav izveidots.")
