# Inventory Project (Lab 3 - Status Accounting & Auditing)

Reads items from `inventory.py`, calculates total stock value and prints a report.

## Structure
```
inventory.py      # Item dataclass + inventory data + low_stock()
app.py            # report + total_stock_value()
utils/helpers.py  # highest_stock_item / lowest_stock_item
tests/            # pytest tests
changelog.txt     # exported Git history
CSA.md            # configuration status accounting record
```

## Run
```
pip install -r requirements.txt
python app.py
pytest
```
