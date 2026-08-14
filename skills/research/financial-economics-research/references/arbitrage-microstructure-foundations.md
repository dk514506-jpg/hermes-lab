# Session-tested foundation set: arbitrage, microstructure, execution

## Primary papers and stable records

- Shleifer & Vishny (1997), “The Limits of Arbitrage,” *Journal of Finance* 52(1), 35–55. DOI: 10.1111/j.1540-6261.1997.tb03807.x. Core lesson: capital, convergence-horizon, noise-trader, and forced-liquidation risk.
- Kyle (1985), “Continuous Auctions and Insider Trading,” *Econometrica* 53(6), 1315–1336. Econometric Society/JSTOR stable URL: https://www.jstor.org/stable/1913210. Core lesson: order flow, depth, and gradual information incorporation are endogenous.
- Glosten & Milgrom (1985), “Bid, ask and transaction prices in a specialist market with heterogeneously informed traders,” *Journal of Financial Economics* 14, 71–100. DOI: 10.1016/0304-405X(85)90044-3. Core lesson: asymmetric information is a structural spread component.
- Hasbrouck (1991), “Measuring the Information Content of Stock Trades,” *Journal of Finance* 46(1), 179–207. DOI: 10.1111/j.1540-6261.1991.tb03749.x. Core lesson: lagged and concave trade impact; use trade/quote VAR-style markouts.
- Amihud (2002), “Illiquidity and stock returns,” *Journal of Financial Markets* 5(1), 31–56. DOI: 10.1016/S1386-4181(01)00024-6. Core lesson: absolute return per dollar volume is a screening proxy, not a tick-level execution model.
- Hendershott, Jones & Menkveld (2011), “Does Algorithmic Trading Improve Liquidity,” *Journal of Finance* 66(1), 1–33. DOI: 10.1111/j.1540-6261.2010.01624.x. Core lesson: market-structure and technology regimes change spreads, adverse selection, and price discovery.
- Budish, Cramton & Shim (2015), “The High-Frequency Trading Arms Race,” *Quarterly Journal of Economics* 130(4), 1547–1621. Oxford Academic: https://academic.oup.com/qje/article/130/4/1547/1916146. Core lesson: latency advantages can create mechanical rents; retain exchange/receipt clocks and sequence data.
- Obizhaeva & Wang (2013), “Optimal trading strategy and supply/demand dynamics,” *Journal of Financial Markets* 16(1), 1–32. NBER record: https://www.nber.org/papers/w11444; working-paper DOI 10.3386/w11444. Core lesson: dynamic book resiliency affects execution schedule and cost.
- Keim & Madhavan (1997), “Transactions costs and investment style,” *Journal of Financial Economics* 46(3), 265–292. DOI: 10.1016/S0304-405X(97)00031-7. Core lesson: costs vary by difficulty, style, instrument, exchange, and order strategy.
- Gatev, Goetzmann & Rouwenhorst (2006), “Pairs Trading: Performance of a Relative-Value Arbitrage Rule,” *Review of Financial Studies* 19(3), 797–827. DOI: 10.1093/rfs/hhj020. Core lesson: formation/trading windows and out-of-sample discipline are essential.
- Avellaneda & Lee (2010), “Statistical Arbitrage in the US Equities Market,” *Quantitative Finance* 10(7), 761–782. DOI: 10.1080/14697680903124632. Core lesson: mean-reverting portfolios require versioned universe, factor/residual, and cost assumptions.
- Almgren & Chriss (2000/2001), “Optimal Execution of Portfolio Transactions,” *Journal of Risk*. DOI: 10.21314/JOR.2001.041. Core lesson: execution balances volatility risk and market-impact cost.

## Minimum evidence-to-schema mapping

| Mechanism | Required fields |
|---|---|
| Adverse selection | Signed trade, quote at decision, venue, exchange/receipt time, post-trade midpoint markouts |
| Latency | Exchange timestamp, local receive timestamp, sequence number, signal time, submit/ack/cancel/fill times, clock offset |
| Impact | Full depth or message events, order size/depth and ADV ratios, participation, replenishment, recovery/resiliency |
| Statistical arbitrage | Point-in-time universe, data-availability time, formation/trading window, hedge ratio, residual, parameters, delistings, corporate actions |
| Funding/limits | Borrow fee/availability, financing, margin, capital, drawdown, liquidation and forced-exit rules |
| Net execution | Arrival/mid/VWAP benchmarks, spread, temporary/permanent impact, commissions, rebates, FX, taxes, borrow, financing |

## Citation-ledger lesson

Register URLs before drafting. Put key claims in prose as well as tables because coverage tools may exclude table rows. Keep no more than three source IDs per sentence. Duplicate authoritative and DOI landing pages should not be piled into one sentence; cite the primary record and use a separate bibliographic sentence if the duplicate record is needed. Remove or cite every ledger entry before strict verification.
