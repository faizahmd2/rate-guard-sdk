import { RateGuardError } from './errors.js'
import type { CheckRequest, Decision } from './types.js'

export interface RateGuardOptions {
  baseUrl: string
  token: string
}

export class RateGuard {
  private readonly baseUrl: string
  private readonly token: string

  constructor(options: RateGuardOptions) {
    this.baseUrl = options.baseUrl.replace(/\/+$/, '')
    this.token = options.token
  }

  async check(request: CheckRequest): Promise<Decision> {
    let response: Response

    try {
      response = await fetch(`${this.baseUrl}/v1/check`, {
        method: 'POST',
        headers: {
          Authorization: `Bearer ${this.token}`,
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(request),
      })
    } catch {
      throw new RateGuardError(
        'Unable to connect to RateGuard',
      )
    }

    if (!response.ok) {
      const message = await response.text()

      throw new RateGuardError(
        message || `RateGuard request failed`,
        response.status,
      )
    }

    return response.json() as Promise<Decision>
  }
}