from main import AgenticCommerceSwarm


def test_extract_score_standard_format():
    assert AgenticCommerceSwarm._extract_score("SCORE: 8/10") == 8


def test_extract_score_with_spaces():
    assert AgenticCommerceSwarm._extract_score("SCORE: 9 / 10 | APPROVE") == 9


def test_extract_score_clamps_high_values():
    assert AgenticCommerceSwarm._extract_score("SCORE: 15/10") == 10


def test_extract_score_returns_zero_when_missing():
    assert AgenticCommerceSwarm._extract_score("No score provided") == 0
