#!/usr/bin/env node
// Test dstack v0.5 JavaScript SDK
// Usage: export DSTACK_ENDPOINT=https://your-endpoint && npm test

import { DstackClient } from '@phala/dstack-sdk';
import crypto from 'crypto';

const endpoint = process.env.DSTACK_ENDPOINT || 'http://localhost';
const client = new DstackClient(endpoint);
let pass = 0, fail = 0;

console.log(`🔗 Testing: ${endpoint}\n`);

async function test(name, fn) {
  try {
    await fn();
    console.log(`✅ ${name}`);
    pass++;
  } catch (error) {
    console.log(`❌ ${name}: ${error.message}`);
    fail++;
  }
}

await test('info()', async () => {
  const info = await client.info();
  if (!info.app_id || !info.tcb_info) throw new Error('Invalid response');
});

await test('getKey()', async () => {
  const result = await client.getKey('test/js/v1');
  if (!(result.key instanceof Uint8Array) || result.key.length !== 32)
    throw new Error('Invalid key');
});

await test('getQuote()', async () => {
  const hash = crypto.createHash('sha256').update('test').digest();
  const result = await client.getQuote(hash.slice(0, 32));
  if (!result.quote || !result.event_log) throw new Error('Invalid response');
});

await test('getKey() - deterministic', async () => {
  const k1 = await client.getKey('test/v1');
  const k2 = await client.getKey('test/v1');
  if (k1.key.toString() !== k2.key.toString()) throw new Error('Keys differ');
});

console.log(`\n📊 ${pass} passed, ${fail} failed`);
process.exit(fail > 0 ? 1 : 0);
