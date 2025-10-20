#!/usr/bin/env bash
# Test dstack v0.5 curl API examples
# Usage: export DSTACK_ENDPOINT=https://your-endpoint && ./test-curl.sh

ENDPOINT="${DSTACK_ENDPOINT:-http://localhost}"
PASS=0
FAIL=0

echo "🔗 Testing: ${ENDPOINT}"
echo ""

test_api() {
    local name=$1
    local path=$2
    local data=$3

    if response=$(curl -sf -X POST "${ENDPOINT}${path}" -H 'Content-Type: application/json' -d "$data" 2>&1); then
        echo "✅ ${name}"
        ((PASS++))
        return 0
    else
        echo "❌ ${name}"
        ((FAIL++))
        return 1
    fi
}

# Test GetKey
test_api "GetKey" "/GetKey" '{"path": "my-app/encryption/v1"}'

# Test GetQuote
test_api "GetQuote" "/GetQuote" '{"reportData": "0x1234deadbeef00000000000000000000000000000000000000000000000000"}'

# Test deterministic keys
key1=$(curl -sf -X POST "${ENDPOINT}/GetKey" -H 'Content-Type: application/json' -d '{"path": "test/v1"}' | jq -r .key)
key2=$(curl -sf -X POST "${ENDPOINT}/GetKey" -H 'Content-Type: application/json' -d '{"path": "test/v1"}' | jq -r .key)

if [[ "$key1" == "$key2" && -n "$key1" ]]; then
    echo "✅ GetKey - deterministic"
    ((PASS++))
else
    echo "❌ GetKey - deterministic"
    ((FAIL++))
fi

echo ""
echo "📊 ${PASS} passed, ${FAIL} failed"
[[ $FAIL -eq 0 ]] && exit 0 || exit 1
