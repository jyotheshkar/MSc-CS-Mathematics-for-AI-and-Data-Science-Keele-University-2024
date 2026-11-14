# Repository guidance

This is Jyothesh Karnam's CSC-40072 Keele University mathematics portfolio.

- Preserve the distinction between the 2023/24 student assignment and the AI-assisted 2026 reproduction.
- The final module mark is 91%, 15 CATS; do not infer separate assignment marks or claim university endorsement.
- Read `docs/original/README.md` and `docs/ENGINEERING.md` before changes.
- Keep student identifiers, original transcript and unredacted coursework out of commits.
- Do not restore personalised Part 1(B) matrix data; it encodes an identifier.
- Treat the public assignment copy and provenance hash as historical evidence. Explain intentional changes and update its receipt.
- Use the standard-library runtime unless a concrete requirement justifies a dependency.

Checks from the repository root:

```sh
python scripts/verify_repository.py
python -m unittest discover -s tests -v
python -m src.workbench
```

These checks verify selected examples and artifact integrity, not the complete original coursework or office-document layout.
