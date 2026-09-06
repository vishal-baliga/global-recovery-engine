# Contract reference package

[recovery-contracts.zip](recovery-contracts.zip) preserves the earlier domain/data-contract reference package unchanged.

It contains:

- `recovery-contracts.schema.json`
- `worked-case.json`
- `validate_contracts.py`
- `test_contracts.py`
- `requirements.txt`

The package illustrates the earlier contract baseline and synthetic validation. It is not a running GRE application, and its validation results do not establish either pilot journey's readiness. Its dependency file does not select the application dependencies.

Read [Domain and data contracts](../docs/05-domain-data-contracts.md) for the original package description and [Current decisions](../docs/00-start-here.md) for current scope. Extract and run the reference only when relevant to an active task, using an isolated environment. Reconcile or replace its contracts when the selected implementation requires it.

Archive SHA-256: `14d24f856ade2c0b508a208d32a98c14a37723f4708b43c82f58213396bfaf72`.
