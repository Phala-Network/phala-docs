#!/usr/bin/env python3
# Test dstack v0.5 Python SDK
# Usage: export DSTACK_ENDPOINT=https://your-endpoint && python test-py.py

import os
import sys
import hashlib
from dstack_sdk import DstackClient

endpoint = os.environ.get('DSTACK_ENDPOINT', 'http://localhost')
client = DstackClient(endpoint)
pass_count = 0
fail_count = 0

print(f"🔗 Testing: {endpoint}\n")

def test(name, fn):
    global pass_count, fail_count
    try:
        fn()
        print(f"✅ {name}")
        pass_count += 1
    except Exception as e:
        print(f"❌ {name}: {e}")
        fail_count += 1

test('info()', lambda: (
    info := client.info(),
    None if hasattr(info, 'app_id') and hasattr(info, 'tcb_info') else (_ for _ in ()).throw(ValueError('Invalid response'))
)[1])

test('get_key()', lambda: (
    result := client.get_key('test/py/v1'),
    key_bytes := bytes.fromhex(result.key.replace('0x', '', 1)),
    None if len(key_bytes) == 32 else (_ for _ in ()).throw(ValueError('Invalid key'))
)[2])

test('get_quote()', lambda: (
    hash_val := hashlib.sha256(b'test').digest(),
    result := client.get_quote(hash_val[:32]),
    None if hasattr(result, 'quote') and hasattr(result, 'event_log') else (_ for _ in ()).throw(ValueError('Invalid response'))
)[2])

test('get_key() - deterministic', lambda: (
    k1 := client.get_key('test/v1'),
    k2 := client.get_key('test/v1'),
    None if k1.key == k2.key else (_ for _ in ()).throw(ValueError('Keys differ'))
)[2])

print(f"\n📊 {pass_count} passed, {fail_count} failed")
sys.exit(1 if fail_count > 0 else 0)
