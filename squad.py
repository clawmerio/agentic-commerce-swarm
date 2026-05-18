"""
Interactive CLI for Agentic Commerce Swarm.
"""

from __future__ import annotations

from main import run_swarm

BANNER = """
Agentic Commerce Swarm
Type a commercial automation request, or use:
  status  - show basic status
  help    - show commands
  exit    - quit
"""


def print_help() -> None:
    print(
        """
Commands:
  help      Show this help message
  status    Show CLI status
  exit      Quit

Example requests:
  Create a campaign and website improvement plan for a fictional clinic AI assistant.
  Diagnose a landing page and propose conversion-focused copy improvements.
  Generate a safe campaign proposal with QA review and human approval notes.
"""
    )


def main() -> None:
    print(BANNER)

    while True:
        try:
            user_input = input("acs> ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nExiting.")
            break

        if not user_input:
            continue

        command = user_input.lower()
        if command in {"exit", "quit", "sair"}:
            print("Exiting.")
            break
        if command == "help":
            print_help()
            continue
        if command == "status":
            print("Status: CLI ready. Memory and model availability are checked at run time.")
            continue

        try:
            state = run_swarm(user_input)
            print("\n--- QA Auditor Report ---\n")
            print(state.qa_report)
            print("\n--- Quality Score ---")
            print(f"{state.quality_score}/10")
        except Exception as exc:
            print(f"Run failed: {exc}")


if __name__ == "__main__":
    main()
