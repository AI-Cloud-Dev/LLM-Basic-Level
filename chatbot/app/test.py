import asyncio
from app.service.services import get_ai_response

async def test():
    res = await get_ai_response("Hello AI")
    print(res)

asyncio.run(test())