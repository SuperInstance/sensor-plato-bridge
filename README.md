# Sensor PLATO Bridge

> Maritime sensor data → PLATO tiles. Ships the sensor stream to the fleet's spatial awareness layer.

**Part of the [SuperInstance fleet](https://github.com/SuperInstance)** — sensor → PLATO tile pipeline for vessel agents.

## What It Does

Polls maritime sensors (depth, temperature, GPS, AIS) and files observations as PLATO tiles:
- Sensors submit to PLATO via HTTP POST to `/submit`
- Each reading becomes a tile in the vessel's room (`vessel:{name}`)
- Delta recording: only file when value changes from last reading

## Usage

```bash
pip install sensor-plato-bridge
PLATO_URL=http://localhost:8847 VESSEL_NAME=orca sensor-poll
```

## Architecture

```
Sensor → sensor-plato-bridge → PLATO HTTP /submit → {domain, question, answer, tags}
```

Tiles are tagged with `vessel:{name}`, `sensor:{type}`, `location:{coords}`.

## Related

- [PLATO room server](https://github.com/SuperInstance/plato-room-phi) — fleet spatial awareness
- [cocapn-glue-core](https://github.com/SuperInstance/cocapn-glue-core) — keeper↔fleet binary wire