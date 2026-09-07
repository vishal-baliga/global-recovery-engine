import assert from 'node:assert/strict';
import { setupEcho, type EchoResponse } from '../packages/api-client/src/index';

const baseUrl = process.argv[2];
assert.ok(baseUrl?.startsWith('http://127.0.0.1:'), 'Expected ephemeral local fixture URL');
const result = await setupEcho({
  baseUrl,
  body: { message: 'client-check' },
  throwOnError: true,
  signal: AbortSignal.timeout(5000),
});
const response: EchoResponse = result.data;
assert.deepEqual(response, { message: 'client-check', length: 12 });
const invalid = await setupEcho({ baseUrl, body: { message: '' }, signal: AbortSignal.timeout(5000) });
assert.ok(invalid.response);
assert.equal(invalid.response.status, 422);
assert.ok(invalid.error?.detail?.length);
console.log('PASS generated TypeScript client: live FastAPI response and typed validation error');
