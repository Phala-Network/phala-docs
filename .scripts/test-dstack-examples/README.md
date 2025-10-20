# Dstack v0.5 API Tests

This directory contains test scripts to validate the dstack v0.5 SDK examples in our documentation.

## Architecture

1. **Nginx Proxy** (`docker-compose.yml`) - Deploys to Phala Cloud to expose `/var/run/dstack.sock` as HTTP
2. **Test Scripts** - Run locally to verify all v0.5 API patterns work correctly

## Step 1: Deploy the Proxy to Phala Cloud

1. Go to <https://cloud.phala.network/dashboard>
2. Click **Deploy** → **docker-compose.yml**
3. Copy and paste the entire contents of `docker-compose.yml` from this directory
4. Set a name (e.g., "dstack-api-proxy")
5. Click **Deploy**
6. Once deployed, go to the **Network** tab and copy your public endpoint:

   ```text
   https://[app-id]-80.dstack-prod7.phala.network
   ```

## Step 2: Run Tests Locally

### JavaScript Tests

```bash
cd .scripts/test-dstack-examples

# Install dependencies
npm install

# Set your endpoint
export DSTACK_ENDPOINT=https://[app-id]-80.dstack-prod7.phala.network

# Run tests
npm test
```

### Python Tests

```bash
cd .scripts/test-dstack-examples

# Install dependencies
pip install -r requirements.txt

# Set your endpoint
export DSTACK_ENDPOINT=https://[app-id]-80.dstack-prod7.phala.network

# Run tests
python test-py.py
```

## What the Tests Validate

### JavaScript (`test-js.mjs`)

- ✅ `DstackClient` initialization with HTTP endpoint
- ✅ `isReachable()` - Service connectivity check
- ✅ `info()` - Get TEE information (app_id, tcb_info)
- ✅ `getKey()` - Derive deterministic 32-byte key
- ✅ `getQuote()` - Generate TDX quote with manual SHA256 hashing

### Python (`test-py.py`)

- ✅ `DstackClient` initialization with HTTP endpoint
- ✅ `info()` - Get TEE information (app_id, tcb_info)
- ✅ `get_key()` - Derive deterministic 32-byte key
- ✅ `get_quote()` - Generate TDX quote with manual SHA256 hashing

## Expected Output

### Successful Run

```text
🔗 Testing dstack v0.5 JavaScript SDK against: https://abc123-80.dstack-prod7.phala.network

🧪 Running JavaScript Tests

════════════════════════════════════════════════════════════
✅ isReachable() - Check service availability
   App ID: abc123...
✅ info() - Get TEE information
   Key length: 32 bytes
✅ getKey() - Derive deterministic key
   Quote length: 8192 chars
✅ getQuote() - Generate TDX quote with manual hashing
════════════════════════════════════════════════════════════

📊 Results: 4 passed, 0 failed
```

## Troubleshooting

**Error: Service not reachable**

- Verify the CVM is running in Phala Cloud dashboard
- Check the endpoint URL is correct
- Ensure port 80 is exposed in the Network tab

**Error: Connection refused**

- The nginx proxy may not have started correctly
- Check CVM logs in Phala Cloud dashboard
- Verify `/var/run/dstack.sock` exists in the container

**Error: Missing signature_chain**

- This indicates the API response structure doesn't match v0.5
- Check if the SDK version is correct: `@phala/dstack-sdk@latest`

## Files

- `docker-compose.yml` - Single-file nginx proxy (deploy this to Phala Cloud)
- `test-js.mjs` - JavaScript test suite
- `test-py.py` - Python test suite
- `package.json` - JavaScript dependencies
- `requirements.txt` - Python dependencies

## Cleanup

When done testing, delete the CVM from Phala Cloud dashboard to stop incurring costs.
