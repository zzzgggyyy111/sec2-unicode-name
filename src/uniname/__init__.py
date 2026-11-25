"""Public interface for Unicode identifier checks."""

from .norm import (
    check_charset,
    check_confusable,
    fold_case,
    key_of,
    name_batch,
    normalize,
    strip_invisible,
    validate_policy,
)

__all__ = [
    "check_charset",
    "check_confusable",
    "fold_case",
    "key_of",
    "name_batch",
    "normalize",
    "strip_invisible",
    "validate_policy",
]