# Supported Assets

Currently, we have supported the following assets with the corresponding transfer routes. The table below shows which chains have been supported for each asset. For example, we can transfer ZLK between parachains and Moonriver EVM, but we cannot transfer it between parachains and Ethereum.

An asset id of type _uint32_ is allocated for each registered asset. Each asset except PHA on Khala/Phala will have an unique asset id. You can use [pallet-assets](https://github.com/paritytech/substrate/tree/master/frame/assets) to transfer asset to any accounts within Khala/Phala Network.

* Assets on Khala network

| Name | Location                                     | Asset ID | Parachains | Ethereum | Moonriver EVM |
| ---- | -------------------------------------------- | -------- | ---------- | -------- | ------------- |
| PHA  | (1, X1(Parachain(2004)))                     | null     | ✅          | ✅        | ❌             |
| KSM  | (1, Here)                                    | 0        | ✅          | ❌        | ❌             |
| KAR  | (1, X2(Parachain(2000), GeneralKey(0x0080))) | 1        | ✅          | ❌        | ❌             |
| BNC  | (1, X2(Parachain(2001), GeneralKey(0x0001))) | 2        | ✅          | ❌        | ❌             |
| ZLK  | (1, X2(Parachain(2001), GeneralKey(0x0207))) | 3        | ✅          | ❌        | ✅             |
| AUSD | (1, X2(Parachain(2000), GeneralKey(0x0081))) | 4        | ✅          | ❌        | ❌             |
| MOVR | (1, X2(Parachain(2023), PalletInstance(10))) | 6        | ✅          | ❌        | ❌             |
| HKO  | (1, X2(Parachain(2085), GeneralKey(“HKO”)))  | 7        | ✅          | ❌        | ❌             |
| KMA  | (1, X1(Parachain(2084)                       | 8        | ✅          | ❌        | ❌             |
| BSX  | (1, X2(Parachain(2090), GeneralIndex(0)))    | 9        | ✅          | ❌        | ❌             |
| TUR  | (1, X1(Parachain(2114)                       | 10       | ✅          | ❌        | ❌             |
| CRAB | (1, X2(Parachain(2105), PalletInstance(5)))  | 11       | ✅          | ❌        | ❌             |

* Assets on Phala network

| Name | Location                                     | Asset ID | Parachains | Ethereum | Moonriver EVM |
| ---- | -------------------------------------------- | -------- | ---------- | -------- | ------------- |
| PHA  | (1, X1(Parachain(2035)))                     | null     | ✅          | ✅        | ❌             |
| DOT  | (1, Here)                                    | 0        | ✅          | ❌        | ❌             |
| GLMR | (1, X2(Parachain(2004), PalletInstance(10))) | 1        | ✅          | ❌        | ❌             |
| PARA | (1, X2(Parachain(2012), GeneralKey(“PARA”))) | 2        | ✅          | ❌        | ❌             |
| AUSD | (1, X2(Parachain(2000), GeneralKey(0x0001))) | 3        | ✅          | ❌        | ❌             |
| LDOT | (1, X2(Parachain(2000), GeneralKey(0x0003))) | 4        | ✅          | ❌        | ❌             |
| ACA  | (1, X2(Parachain(2000), GeneralKey(0x0000))) | 5        | ✅          | ❌        | ❌             |
