#Project Renmo
Jasper Wu, Shohei Kishiya, Bayon Lee, JJ Tsao, Peach Lertpraival

What is it?
    Web application for peer-to-peer currency exchange
    In this initial stage, we will solely target CBS students looking to buy Chinese Renminbi (with USD) or sell Chinese Renminbi (for USD)

Why is it a good idea?
CBS students come from around the world and travel around the world. We have constant needs of currency exchange, say for chazen tours, global immersion programs, fall break, thanksgiving break, winter break, spring break, and many more! However, going to a bank is time-consuming and exchanging at airport is a rip off. There is also the hassle of figuring out which bank account (or perhaps Venmo or Paypal or Alipay) we actually need the money in and how to get it there. We definitely need a simpler, easier process with a fair rate. Maybe on-campus with our clustermates? We first imagine a RMB/USD exchange since the majority of international students at Columbia are Chinese. This can of course be expanded to more currencies in the future.

Target Audience
    Chinese or Chinese-American students and faculty at Columbia, or those who are travelling to China in the near future.

Initial thoughts on user flow and data structure

Flow for seller (selling RMB for USD)
    Signup (with email & Facebook)
    Login
    Connect with bank account (source and target)
    List RMB amount available for sale
    List preferred rate (provide mkt rate as ref)
    Wait for potential buyers
    If buyer accepts offer, RMB is withdrawn from source account and placed into target account.
Flow for buyer (buying RMB with USD)
    Signup (with email & Facebook)
    Login
    Browse/ search the listings
    Choose the seller
    Connect with bank account (source/target)
    Complete transaction (USD withdrawn from “source” account, RMB deposited to “target” account)

Data tables
    User (user id, email, username, password)
    Bank info (user id, routing, account number, account name)
    Listings (RMB amount, time, rate on the day listed, seller ID)
    Transactions (USD, RMB, time, amount, rate, seller ID, buyer ID)

Website design - Peach / Jasper
Login system (email/ FB) + user table - Shohei
Connect to bank account + bank info table - Jasper
List a listing & get FX - JJ
Search listings - Bayon
Transaction
