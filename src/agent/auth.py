import typing as tp

if tp.TYPE_CHECKING:
    from .agent import TelegramAgent


class AuthMixin:
    async def start_session(self: "TelegramAgent") -> None:
        if not self.client.is_connected():
            await self.client.connect()

        if not await self.client.is_user_authorized():
            raise ValueError()
