export interface CheckRequest {
  service: string
  resource: string
  key: string
}

export type DecisionType = 'ALLOW' | 'DENY'

export interface Decision {
  decision: DecisionType
  limit: number
  remaining: number
  retry_after_ms: number
}