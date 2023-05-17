from quart import Quart

app = Quart(__name__)


@app.route('/')
async def home():
    return "I'm alive"


async def run_server():
  await app.run_task()
