from memory import SwarmMemory


def test_memory_search_falls_back_safely(tmp_path):
    memory = SwarmMemory(persist_dir=str(tmp_path / "chroma"))
    results = memory.search("anything")
    assert isinstance(results, list)


def test_memory_save_run_does_not_raise(tmp_path):
    memory = SwarmMemory(persist_dir=str(tmp_path / "chroma"))
    memory.save_run(
        task="Create a demo campaign",
        strategy="Focus on operational pain",
        final_copy="Demo copy",
        qa_report="PASS",
        quality_score=8,
    )
