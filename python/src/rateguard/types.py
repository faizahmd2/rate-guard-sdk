from dataclasses import dataclass
from typing import Literal


DecisionType = Literal["ALLOW", "DENY"]


@dataclass
class CheckRequest:
    service: str
    resource: str
    key: str


@dataclass
class Decision:
    decision: DecisionType
    limit: int
    remaining: int
    retry_after_ms: int