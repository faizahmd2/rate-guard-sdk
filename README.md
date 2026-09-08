# RateGuard SDKs

Official client SDKs for [RateGuard](https://github.com/faizahmd2/rate-limitter-service).

RateGuard is a centralized API rate-limiting service. These SDKs provide small HTTP clients for integrating applications with a RateGuard server.

## SDKs

| Language | Package                    | Status      |
| -------- | -------------------------- | ----------- |
| Node.js  | `@faizahmd2/rateguard-sdk` | Available   |
| Python   | `rateguard`                | Coming soon |

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
  service: 'xoxoday',
  resource: 'purchase',
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

## Repository Structure

```text
rate-guard-sdk/
├── node/
├── python/
```

Each SDK is independently packaged and published to its respective language ecosystem.

## License

MIT
