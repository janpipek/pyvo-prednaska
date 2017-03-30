Tento adresář obsahuje uložené 3D histogramy (mesic, hodina, teplota) pro jednotlivé městské části Brna.

Pro načtení použijte následující kód:

```python
from physt.io import load_json
histogram = load_json("Žabovřesky.json")
```
