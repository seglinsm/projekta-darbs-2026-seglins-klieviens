"""Pielāgotie izņēmumi failu drošības lietotnei."""


class AppError(Exception):
    """Bāzes izņēmums visai lietotnei."""


class ValidationError(AppError, ValueError):
    """Nepareiza lietotāja ievade vai nederīgs pieprasījums."""


class FileAccessError(AppError, FileNotFoundError):
    """Kļūda, piekļūstot failam vai mapei."""


class KeyErrorInvalid(AppError, ValueError):
    """Atslēga ir nederīga vai bojāta."""


class EncryptionProcessError(AppError, ValueError):
    """Kļūda šifrēšanas vai atšifrēšanas laikā."""
