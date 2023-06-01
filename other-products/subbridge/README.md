# SubBridge

## What is SubBridge? <a href="#what-is-subbridge" id="what-is-subbridge"></a>

SubBridge is the cross-chain router of the parachains, bridging Dotsama and Ethereum and assets in other ecosystems.

SubBridge is based on the “XCM + ChainBridge cross-chain protocol” to realize cross-chain transmission of assets and information.

In August 2021, Phala launched the first parachain-Ethereum smart contract bridge on Substrate, which can support the mutual transfer of parachain assets between Ethereum and parachain. In the future, parachains in the Substrate ecosystem can integrate and use SubBridge to achieve asset transaction and messages migration with other ecosystems (e.g., EVM) , and promote the prosperity of the Polkadot’s ecosystem.

## Security Concern <a href="#security-concern" id="security-concern"></a>

The security of the SubBridge is of prior concern. In terms of EVM compatibility, SubBridge has its own solution with the following security advantages:

* SubBridge has passed an audit by Certik, a top blockchain security company (Per the audit report, there are no critical or major errors or known vulnerabilities; some minor concerns have been solved or addressed);
* Admin takes multi-signature management to guarantee asset security;
* SubBridge consists of several relayers, the operation is guaranteed when there is a single node out of service.

Read the [following section](technical-details.md#code-auditing) for more details on code auditing.
