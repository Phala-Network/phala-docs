# Getting Started

The Mirrored Price Feed aims to work well with ChainLink's ABI. This means you can easily use it on any blockchain that supports EVM. To start using it, simply [find the right contract address here](https://docs-git-build-coprocessor-phala.vercel.app/solutions/mirrored-price-feed/feed-addresses).

The learn more about Chainlink's `AggregatorV3Interface`, you can check out their [API Reference](https://docs.chain.link/data-feeds/api-reference).

## Reading data feeds onchain

Here is some code snippets to demostrate how to use Mirrored Price Feed on-chain.

### Getting the latest data

```solidity

// SPDX-License-Identifier: MIT
pragma solidity ^0.8.7;
 
import {AggregatorV3Interface} from "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";
 
/**
 * THIS IS AN EXAMPLE CONTRACT THAT USES HARDCODED
 * VALUES FOR CLARITY.
 * THIS IS AN EXAMPLE CONTRACT THAT USES UN-AUDITED CODE.
 * DO NOT USE THIS CODE IN PRODUCTION.
 */
contract DataConsumerV3 {
    AggregatorV3Interface internal dataFeed;
 
    /**
     * Network: Base Sepolia
     * Aggregator: BTC/USD
     * Address: 0x1e73C20c42a7de166868da4c47963d137030492A
     */
    constructor() {
        dataFeed = AggregatorV3Interface(
            0x1e73C20c42a7de166868da4c47963d137030492A
        );
    }
 
    /**
     * Returns the latest answer.
     */
    function getChainlinkDataFeedLatestAnswer() public view returns (int) {
        // prettier-ignore
        (
            /* uint80 roundID */,
            int answer,
            /*uint startedAt*/,
            /*uint timeStamp*/,
            /*uint80 answeredInRound*/
        ) = dataFeed.latestRoundData();
        return answer;
    }
}
```

### Getting the historial data

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.7;
 
import {AggregatorV3Interface} from "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";
 
/**
 * THIS IS AN EXAMPLE CONTRACT THAT USES HARDCODED VALUES FOR CLARITY.
 * THIS IS AN EXAMPLE CONTRACT THAT USES UN-AUDITED CODE.
 * DO NOT USE THIS CODE IN PRODUCTION.
 */
contract HistoricalDataConsumerV3 {
    AggregatorV3Interface internal dataFeed;
 
    /**
     * Network: Base Sepolia
     * Aggregator: BTC/USD
     * Address: 0x1e73C20c42a7de166868da4c47963d137030492A
     */
    constructor() {
        dataFeed = AggregatorV3Interface(
            0x1e73C20c42a7de166868da4c47963d137030492A
        );
    }
 
    /**
     * Returns historical data for a round ID.
     * roundId is NOT incremental. Not all roundIds are valid.
     * You must know a valid roundId before consuming historical data.
     *
     * ROUNDID VALUES:
     *    InValid:      18446744073709562300
     *    Valid:        18446744073709554683
     *
     * @dev A timestamp with zero value means the round is not complete and should not be used.
     */
    function getHistoricalData(uint80 roundId) public view returns (int256) {
        // prettier-ignore
        (
            /*uint80 roundID*/,
            int answer,
            /*uint startedAt*/,
            /*uint timeStamp*/,
            /*uint80 answeredInRound*/
        ) = dataFeed.getRoundData(roundId);
        return answer;
    }
}
```
