"""Public tests for the Unicode identifier checks."""

from __future__ import annotations

import pytest

from uniname import fold_case, key_of, name_batch, normalize, strip_invisible


def _policy(**overrides):
    policy = {
        "normalization": "NFKC",
        "confusable_check": True,
        "charset": "abcdefghijklmnopqrstuvwxyz0123456789._-",
    }
    policy.update(overrides)
    return policy


def test_normalized_forms_are_equal():
    assert normalize("\u00e9") == normalize("e\u0301")


def test_case_folding_is_stable():
    assert fold_case("Stra\u00dfe") == "strasse"
    assert fold_case("ss") == "ss"


def test_zero_width_character_is_rejected():
    with pytest.raises(ValueError):
        strip_invisible("ad\u200dmin")


def test_unique_key_is_stable():
    policy = _policy()
    assert key_of("\uff21lice", policy) == key_of("alice", policy)


def test_batch_names_are_independent():
    report = name_batch(["alice", "bob"], _policy())
    assert report["alice"]["key"] == "alice"
    assert report["bob"]["key"] == "bob"