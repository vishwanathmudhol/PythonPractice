import xml.etree.ElementTree as ET
import pandas as pd
import xml.dom.minidom as md

df = pd.read_excel("Input.xlsx", sheet_name="Sheet1", dtype=object)

# LIST OF DATA FRAME SPLITS
df_list = [g for i,g in df.groupby(
    ["Name", "BaseCurrency2", "TradingPower", "ValidationProfile", "CommissionProfile"]
)]

# ROOT LEVEL
root = ET.Element('trading-data')
root.set('xmlns:xsi', 'http://www.w3.org/2001/XMLSchema-instance')

# ROOT CHILD LEVEL
Portfolios = ET.SubElement(root, "Portfolios")
Defaults = ET.SubElement(Portfolios, "Defaults", BaseCurrency="USD")

# GROUP LEVEL ITERATION
for df in df_list:
    Portfolio = ET.SubElement(
        Portfolios,
        "Portfolio",
        Name = df["Name"][0],
        BaseCurrency = df["BaseCurrency2"][0],
        TradingPower = str(df["TradingPower"][0]),
        ValidationProfile = df["ValidationProfile"][0],
        CommissionProfile = df["CommissionProfile"][0]
    )

    PortfolioPositions = ET.SubElement(Portfolio, "PortfolioPositions")

    # ROW LEVEL ITERATION
    for row in df.itertuples():
        if row.Type == "Cash":
            PortfolioPosition = ET.SubElement(
                PortfolioPositions,
                "PortfolioPosition",
                Type = row.Type,
                Volume = str(row.Volume)
            )
            Cash = ET.SubElement(
                PortfolioPosition,
                "Cash",
                Currency = str(row.Currency)
            )
        else:
            PortfolioPosition = ET.SubElement(
                 PortfolioPositions,
                 "PortfolioPosition",
                 Type = row.Type,
                 Volume = str(row.Volume),
                 Invested = str(row.Invested),
                 BaseInvested = str(row.BaseInvested)
            )
            Instrument = ET.SubElement(
                 PortfolioPosition,
                 "Instrument",
                 Ticker = str(row.Ticker),
                 ISIN = str(row.ISIN),
                 Market = str(row.Market),
                 Currency = str(row.Currency2),
                 CFI = str(row.CFI)
            )

# SAVE PRETTY PRINT OUTPUT
with open("Output.xml", "wb") as f:
    dom = md.parseString(ET.tostring(root))
    f.write(dom.toprettyxml().encode("utf-8"))