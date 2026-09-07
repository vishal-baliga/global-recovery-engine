# Contract references

The current source-readable [v0.2 baseline](v0.2/README.md) implements bounded offline reference semantics for Foundation plus Trade Pilot. It includes the schema, synthetic fixtures, six contract compositions, complete 29-record/23-operation migration crosswalk, validator and 42 conformance tests. It is not the application or proof of a released service.

[Domain and data contracts](../docs/05-domain-data-contracts.md) owns the current contract meanings; [Current decisions](../docs/00-start-here.md) owns project scope.

[recovery-contracts.zip](recovery-contracts.zip) preserves the immutable historical 0.1.0 package:

- `recovery-contracts.schema.json`
- `worked-case.json`
- `validate_contracts.py`
- `test_contracts.py`
- `requirements.txt`

Its 89-record/four-checkpoint fixture and 51 tests remain runnable separately. Its old settlement-offer commit harness is historical and does not authorize GRE collection in the current Pilot. Extract each reference into a separate environment/import path and follow its commands. Reference dependencies do not select application dependencies.

Original archive SHA-256: `14d24f856ade2c0b508a208d32a98c14a37723f4708b43c82f58213396bfaf72`.
