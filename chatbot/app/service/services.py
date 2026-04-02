# LLM SERVICE LAYER

import os
from dotenv import load_dotenv
from openai import AsyncOpenAI
import asyncio

load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")
print("DEBUG API:", os.getenv("OPENAI_API_KEY"))
if not API_KEY:
    raise RuntimeError("OPENAI_API_KEY not found. Please set it in .env file.")

client = AsyncOpenAI(api_key=API_KEY)
async def get_ai_response(message: str) -> str:
    try:
        response = await client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user",
                 "content": message}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        raise RuntimeError(f"LLM Error: {str(e)}")
    


# async def test():
#     res = await get_ai_response("Hello AI")
#     print(res)

# asyncio.run(test())