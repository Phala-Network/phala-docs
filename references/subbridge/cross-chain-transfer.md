# Cross-chain Transfer

### Transfer PHA: Ethereum <-> Khala <a href="#transfer-pha-ethereum---khala" id="transfer-pha-ethereum---khala"></a>

This tutorial takes the transfer of PHA from Ethereum to Khala as an example. You can also refer to this tutorial for other EVM <-> parachain bridge transfers.\
![](../../.gitbook/assets/subbridge-eth-khala.png)

1. Open [SubBridge](https://subbridge.io/), switch _From_ chain to Ethereum, _To_ chain to Khala, and choose `PHA` as the currency;
2. Press _Connect Wallet_ and connect to Metamask;
3. Fill in the amount of ERC-20 PHA that you want to transfer from Ethereum;
4. Enter the receiving account on Khala, note that it should be the Khala address;
5. If it’s the first time you are transferring your PHA assets, you may need to click on the _Approve_ button and sign with Metamask to confirm;\
   <img src="../../.gitbook/assets/subbridge-metamask.png" alt="" data-size="original">
6. Then confirm and click the _Transfer_ button;
7. Double-check your accounts and figures and then click _Submit_ in the pop-up window, sign with Metamask, and submit your cross-chain asset transaction;
8. You can go to Etherscan to check the sending details on the Etherscan block explorer when your transaction is sent; if you have any questions, you can consult our [Discord](https://discord.gg/phala-network).

### Transfer PHA: Khala <-> Karura <a href="#transfer-pha-khala---karura" id="transfer-pha-khala---karura"></a>

This tutorial takes the transfer of PHA from Khala to Karura as an example, and vice versa for transferring from Karura to Khala. You can also refer to this tutorial for other parachain bridge transfers.\
![](../../.gitbook/assets/subbridge-transfer.png)

1. Open [SubBridge](https://subbridge.io/), switch _From_ chain to Khala, _To_ chain to Karura, and choose `PHA` as the currency;
2.  Connect the Source Chain (Khala)’s account, enter the transfer amount;

    > Note: Do not transfer all the token, you need to keep a certain fee in the account to ensure that it is not deleted.
3. Enter the receiving account on destination chain (Karura), note that it should be the Karura address. The destination account is your source account by default, you can click _Edit manually_ to use other addresses;
4. Click _Transfer_;
5.  Confirm pop-up window;

    > Note: A transfer fee of 0.0512 PHA will be charged for transferring from Khala to Karura. The bridge itself is completely free. This fee is used to pay the XCM fee of the Karura chain. It does not include the transaction fee of the Khala chain.
6. Click _Submit_ to sign;\
   ![](../../.gitbook/assets/subbridge-confirm.png)
7. The transaction is sent from Khala, wait for the transaction to be confirmed;
8. Then you can go to destination chain’s wallet (in this case, [Karura Apps](https://apps.karura.network/portfolio)) to check whether you have received the token (PHA). If it is not received within 1 minute, you can go to the Khala chain explorer ([Subscan](https://khala.subscan.io/)) to check whether you have sent a transaction; if you have any questions, you can consult our [Discord](https://discord.gg/phala-network).
