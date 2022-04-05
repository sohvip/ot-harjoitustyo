```mermaid
  sequenceDiagram
      participant Main
      participant machine
      participant tank
      participant engine
      Main ->> machine: Machine()
      machine ->> tank: FuelTank()
      machine ->> tank: fill(40)
      machine ->> engine: Engine(tank)
      Main ->> machine: drive()
      machine ->> Engine: start()
```
