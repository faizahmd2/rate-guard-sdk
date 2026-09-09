# RateGuard SDKs

Official SDKs for [RateGuard](https://github.com/faizahmd2/rate-guard).

## SDKs

| Language | Package                    |
| -------- | -------------------------- |
| Node.js  | `@faizahmd2/rateguard-sdk` |
| Python   | `rateguard-sdk`            |

## Node.js

Install:

```bash
npm install @faizahmd2/rateguard-sdk
```

Example:

```ts
import { RateGuard } from '@faizahmd2/rateguard-sdk'

const rateGuard = new RateGuard({
  baseUrl: process.env.RATEGUARD_URL!,
  token: process.env.RATEGUARD_TOKEN!,
})

const decision = await rateGuard.check({
  service: 'payments',
  resource: 'create-payment',
  key: 'account:123',
})

if (decision.decision === 'DENY') {
  console.log(
    `Rate limited. Retry after ${decision.retry_after_ms}ms`,
  )
  return
}

console.log('Request allowed')
```

## Python

Install:

```bash
pip install rateguard-sdk
```

Example:

```python
from rateguard import CheckRequest, RateGuard

rate_guard = RateGuard(
    base_url="http://localhost:4215",
    token="rg_...",
)

decision = rate_guard.check(
    CheckRequest(
        service="payments",
        resource="create-payment",
        key="account:123",
    )
)

if decision.decision == "DENY":
    print(
        f"Rate limited. Retry after "
        f"{decision.retry_after_ms}ms"
    )
else:
    print("Request allowed")
```


Each SDK is independently packaged and published to its respective language ecosystem.

## License

MIT
