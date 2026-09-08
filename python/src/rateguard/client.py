import json
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

from .errors import RateGuardError
from .types import CheckRequest, Decision


class RateGuard:
    def __init__(self, base_url: str, token: str):
        self.base_url = base_url.rstrip("/")
        self.token = token

    def check(self, request: CheckRequest) -> Decision:
        url = f"{self.base_url}/v1/check"

        payload = json.dumps(
            {
                "service": request.service,
                "resource": request.resource,
                "key": request.key,
            }
        ).encode("utf-8")

        http_request = Request(
            url,
            data=payload,
            method="POST",
            headers={
                "Authorization": f"Bearer {self.token}",
                "Content-Type": "application/json",
            },
        )

        try:
            with urlopen(http_request) as response:
                body = response.read().decode("utf-8")

        except HTTPError as error:
            message = error.read().decode("utf-8")

            raise RateGuardError(
                message or "RateGuard request failed",
                error.code,
            ) from error

        except URLError as error:
            raise RateGuardError(
                "Unable to connect to RateGuard"
            ) from error

        try:
            data = json.loads(body)
        except json.JSONDecodeError as error:
            raise RateGuardError(
                "Invalid response from RateGuard"
            ) from error

        return Decision(
            decision=data["decision"],
            limit=data["limit"],
            remaining=data["remaining"],
            retry_after_ms=data["retry_after_ms"],
        )