"""Export the setup fixture's OpenAPI contract without running an HTTP server."""
import json
from pathlib import Path

from fixtures.api.app import app


def main():
    path = Path(__file__).resolve().parent.parent / "fixtures/api/openapi.json"
    path.write_text(json.dumps(app.openapi(), indent=2, sort_keys=True) + "\n")
    print(f"PASS OpenAPI export: {path.relative_to(path.parents[2])}")


if __name__ == "__main__":
    main()
