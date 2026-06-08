import asyncio

# async def my_async_function():
#     print("Task started")
#     await asyncio.sleep(2)
#     print("Task completed")

# asyncio.run(my_async_function())

# async def task_1():
#     await asyncio.sleep(2)
#     return "Task 1 complete"

# async def task_2():
#     await asyncio.sleep(3)
#     return "Task 2 complete"

# async def main():
#     results = await asyncio.gather(task_1(),task_2())
#     print(results)

# asyncio.run(main())

from flask import Flask
import asyncio

app = Flask(__name__)

async def background_task():
    await asyncio.sleep(5)
    print("Background task completed")

@app.route('/start-task')
def start_task():
    asyncio.run(background_task())
    return {"message":"Task started"}

if __name__ == '__main__':
    app.run(debug=True)