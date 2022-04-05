```mermaid
  sequenceDiagram
      participant Main
      participant machine
      participant tank
      participant Engine
      Main ->> machine: Machine()
      machine ->> tank: FuelTank()
      Main ->> machine: drive()
      machine ->> Engine: start()
```
