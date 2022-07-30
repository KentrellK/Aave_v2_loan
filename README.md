# Aave V2 loan
Python script utilizing Brownie to deposit ETH as collateral in the Aave v2 lending market, and then borrow/repay any supported ERC-20 at 95% of the available borrowing power. This script can be used to create long/short positions.

1. Swap our ETH for WETH
2. Deposit some WETH into Aave
3. Borrow some asset with the ETH collateral
    1. Sell that borrowed asset. (Short selling)
4. Repay everything back


Integration test: Kovan


Unit test: mainnet-fork
# Brownie-config
To borrow an asset other than Dai, change the price feed and token address on the appropriate network.
