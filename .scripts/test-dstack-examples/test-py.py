#!/usr/bin/env python3
"""
Test dstack v0.5 Python SDK examples

Usage:
    export DSTACK_ENDPOINT=https://your-app-id-80.dstack-prod7.phala.network
    python test-py.py
"""

import os
import sys
import hashlib
from dstack_sdk import DstackClient

endpoint = os.environ.get('DSTACK_ENDPOINT', 'http://localhost')
print(f"🔗 Testing dstack v0.5 Python SDK against: {endpoint}\n")

pass_count = 0
fail_count = 0


def test_pass(test):
    global pass_count
    print(f"✅ {test}")
    pass_count += 1


def test_fail(test, error):
    global fail_count
    print(f"❌ {test}")
    print(f"   Error: {error}")
    fail_count += 1


def test_info():
    try:
        client = DstackClient(endpoint)
        info = client.info()

        if not hasattr(info, 'app_id'):
            raise ValueError('Missing app_id')
        if not hasattr(info, 'tcb_info'):
            raise ValueError('Missing tcb_info')

        print(f"   App ID: {info.app_id[:16]}...")
        test_pass('info() - Get TEE information')
    except Exception as error:
        test_fail('info() - Get TEE information', error)


def test_get_key():
    try:
        client = DstackClient(endpoint)
        key_result = client.get_key('test/python/v1')

        if not hasattr(key_result, 'key'):
            raise ValueError('Missing key')
        if not hasattr(key_result, 'signature_chain'):
            raise ValueError('Missing signature_chain')

        # Key is returned as hex string, convert to bytes
        key_hex = key_result.key.replace('0x', '', 1)
        key_bytes = bytes.fromhex(key_hex)
        if len(key_bytes) != 32:
            raise ValueError(f'Expected 32 bytes, got {len(key_bytes)}')

        print(f"   Key length: {len(key_bytes)} bytes")
        test_pass('get_key() - Derive deterministic key')
    except Exception as error:
        test_fail('get_key() - Derive deterministic key', error)


def test_get_quote():
    try:
        client = DstackClient(endpoint)

        # Test with manual hashing (v0.5 pattern)
        user_data = b'test-data-python'
        hash_value = hashlib.sha256(user_data).digest()
        quote_result = client.get_quote(hash_value[:32])

        if not hasattr(quote_result, 'quote'):
            raise ValueError('Missing quote')
        if not hasattr(quote_result, 'event_log'):
            raise ValueError('Missing event_log')

        # Verify quote is hex string (may or may not have 0x prefix)
        quote_hex = quote_result.quote.replace('0x', '', 1)
        if len(quote_hex) < 100:
            raise ValueError('Quote seems too short')

        print(f"   Quote length: {len(quote_hex)} chars")
        test_pass('get_quote() - Generate TDX quote with manual hashing')
    except Exception as error:
        test_fail('get_quote() - Generate TDX quote with manual hashing', error)


def run_all_tests():
    print("🧪 Running Python Tests\n")
    print("=" * 60)

    test_info()
    test_get_key()
    test_get_quote()

    print("=" * 60)
    print(f"\n📊 Results: {pass_count} passed, {fail_count} failed\n")

    if fail_count > 0:
        sys.exit(1)


if __name__ == '__main__':
    try:
        run_all_tests()
    except Exception as error:
        print(f"Fatal error: {error}")
        sys.exit(1)
