```mermaid
  sequenceDiagram
      participant Main
      participant kone
      participant FuelTank
      participant Engine
      Main ->> kone: Machine()
      Main ->> kone: drive()
      kone ->> Engine: start()
```
