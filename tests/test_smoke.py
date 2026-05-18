from pathlib import Path

from main import AgenticCommerceSwarm, SwarmState
from memory import SwarmMemory


def test_extract_score_parses_score() -> None:
    assert AgenticCommerceSwarm._extract_score("SCORE: 8/10") == 8


def test_extract_score_defaults_to_zero() -> None:
    assert AgenticCommerceSwarm._extract_score("no score available") == 0


def test_memory_fallback_search_returns_list(tmp_path: Path) -> None:
    memory = SwarmMemory(persist_dir=str(tmp_path / "memory"))
    result = memory.search("fictional query")
    assert isinstance(result, list)


def test_swarm_state_defaults() -> None:
    state = SwarmState(task="Create a fictional demo campaign")
    assert state.task == "Create a fictional demo campaign"
    assert state.messages == []
    assert state.quality_score == 0
    assert state.approved_for_human_review is False
